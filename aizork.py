#!/usr/bin/env python3

# import pandas as pd

import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import json 
from flask import Flask, render_template, redirect, url_for, request, jsonify
app = Flask(__name__)


scenarios = {
    "scenes":["It was a warm night at Castle Caladan, and the ancient pile of stone that had served the Atreides family as home for twenty-six generations bore that cooled-sweat feeling it acquired before a change in the weather.",
    "A long time ago in a galaxy far, far away…A NEW HOPE It is a period of civil war. Rebel spaceships, striking from a hidden base, have won their first victory against the evil Galactic Empire. During the battle, Rebel spies managed to steal secret plans to the Empire’s ultimate weapon, the DEATH STAR, an armored space station with enough power to destroy an entire planet. Pursued by the Empire’s sinister agents, Princess Leia races home aboard her starship, custodian of the stolen plans that can save her people and restore freedom to the galaxy….", 
    "The house stood on a slight rise just on the edge of the village. It stood on its own and looked out over a broad spread of West Country farmland. Not a remarkable house by any means—it was about thirty years old, squattish, squarish, made of brick, and had four windows set in the front of a size and proportion which more or less exactly failed to please the eye."
    ]
}



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/input", methods = ["POST"])
def sendScene():
    # tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
    # model = GPT2LMHeadModel.from_pretrained('gpt2')
    scene = "Hello World!"
    choice = ""

    if request.form.get("choice"): # if nm was assigned via the POST
        choice = request.form.get("choice") # grab the value of nm from the POST
    
    if(choice == 'Dune'):
        scene = scenarios["scenes"][0]
    elif(choice == 'Star Wars'):
        scene = scenarios["scenes"][1]
    elif(choice == "HitchHikers"):
        scene = scenarios["scenes"][2]
    else:
        scene = "Goodbye World!"




    # scene = "West of House. You are standing in an open field west of a white house, with a boarded front door.  There is a small mailbox here."
    # inputs = tokenizer.encode(scene, return_tensors='pt')
    # outputs = model.generate(inputs, max_length=200, do_sample=True)
    # text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    text = scene
    # scenariosData = jsonify({"newScene": text})
    scenariosData = json.dumps({"newScene": text})
    # return redirect(url_for("getresults", results2 = text))
    return redirect(url_for("getresults", results2 = scenariosData))

# def sendGenre():
    # movie_File = 'movies.xls'
    # movies1 = pd.read_excel(movie_File, sheet_name=0, index_col= 0, usecols=['Title', 'Year', 'Genres', 'Language', 'Content Rating', 'Duration', 'Budget', 'Actor 1', 'Actor 2', 'Actor 3', 'IMDB Score'])
    # movies2 = pd.read_excel(movie_File, sheet_name=1, index_col= 0, usecols=['Title', 'Year', 'Genres', 'Language', 'Content Rating', 'Duration', 'Budget', 'Actor 1', 'Actor 2', 'Actor 3', 'IMDB Score'])
    # movies3 = pd.read_excel(movie_File, sheet_name=2, index_col= 0, usecols=['Title', 'Year', 'Genres', 'Language', 'Content Rating', 'Duration', 'Budget', 'Actor 1', 'Actor 2', 'Actor 3', 'IMDB Score'])
    # movies = pd.concat([movies1, movies2, movies3])
    # #takes panda dataframe and searches by genre, then converts to json objects organized by column
    # results1 = json.loads(movies.query("Genres== 'Action'").to_json(orient='columns'))
    # return redirect(url_for("getresults", results2 = results1))
    # #return json.dumps(movies.groupby(by='Genres')) #.to_json(orient = 'columns')   
    #  #movies1 = pd.read_excel(movie_File, sheet_name=0, index_col= 0, usecols=['Genres'])

@app.route("/results/<results2>")
def getresults(results2):
    return render_template('results.html', results3 = results2)


def main():
    #import movie spreasheet
    movie_File = 'movies.xls'
    #create a dataframe and read moviefile and all sheets in
    # make Title column the index w/ index_col 0
    #multiple sheets added at once create a dict
    #reduce the number of columns to only those used by the app
    movies = pd.read_excel(movie_File, sheet_name=['1900s', '2000s', '2010s'], index_col= 0, usecols=['Title', 'Year', 'Genres', 'Language', 'Content Rating', 'Duration', 'Budget', 'Actor 1', 'Actor 2', 'Actor 3', 'IMDB Score'])
    #test print of movies dict
    print(movies)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
    #main()
