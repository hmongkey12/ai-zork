#!/usr/bin/env python3

import pandas as pd
import json 
from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/input", methods = ["POST"])
def sendGenre():
    movie_File = 'movies.xls'
    movies1 = pd.read_excel(movie_File, sheet_name=0, index_col= 0, usecols=['Title', 'Year', 'Genres', 'Language', 'Content Rating', 'Duration', 'Budget', 'Actor 1', 'Actor 2', 'Actor 3', 'IMDB Score'])
    movies2 = pd.read_excel(movie_File, sheet_name=1, index_col= 0, usecols=['Title', 'Year', 'Genres', 'Language', 'Content Rating', 'Duration', 'Budget', 'Actor 1', 'Actor 2', 'Actor 3', 'IMDB Score'])
    movies3 = pd.read_excel(movie_File, sheet_name=2, index_col= 0, usecols=['Title', 'Year', 'Genres', 'Language', 'Content Rating', 'Duration', 'Budget', 'Actor 1', 'Actor 2', 'Actor 3', 'IMDB Score'])
    movies = pd.concat([movies1, movies2, movies3])
    #takes panda dataframe and searches by genre, then converts to json objects organized by column
    results1 = json.loads(movies.query("Genres== 'Action'").to_json(orient='columns'))
    return redirect(url_for("getresults", results2 = results1))
    #return json.dumps(movies.groupby(by='Genres')) #.to_json(orient = 'columns')   

     #movies1 = pd.read_excel(movie_File, sheet_name=0, index_col= 0, usecols=['Genres'])

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
