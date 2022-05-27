#!/usr/bin/env python3

# import pandas as pd

import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import json 
from flask import Flask, render_template, redirect, url_for, request, session
app = Flask(__name__)
app.secret_key = "Secret Key"


scenarios = {
    "Dune" : "It was a warm night at Castle Caladan, and the ancient pile of stone that had served the Atreides family as home for twenty-six generations bore that cooled-sweat feeling it acquired before a change in the weather.",
    "Star Wars": "A long time ago in a galaxy far, far away…A NEW HOPE It is a period of civil war. Rebel spaceships, striking from a hidden base, have won their first victory against the evil Galactic Empire. During the battle, Rebel spies managed to steal secret plans to the Empire’s ultimate weapon, the DEATH STAR, an armored space station with enough power to destroy an entire planet. Pursued by the Empire’s sinister agents, Princess Leia races home aboard her starship, custodian of the stolen plans that can save her people and restore freedom to the galaxy….", 
    "Hitchhikers":"The house stood on a slight rise just on the edge of the village. It stood on its own and looked out over a broad spread of West Country farmland. Not a remarkable house by any means—it was about thirty years old, squattish, squarish, made of brick, and had four windows set in the front of a size and proportion which more or less exactly failed to please the eye."
}



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/input", methods = ["POST"])
def sendScene():
    # tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
    # model = GPT2LMHeadModel.from_pretrained('gpt2')
    scene = ""
    choice = ""
    username = ""
    text = []

    if request.form.get("choice"): # if nm was assigned via the POST
        choice = request.form.get("choice") # grab the value of nm from the POST
    if request.form.get("username"):
        username = request.form.get("username")
    
    if (choice in scenarios.keys()):
        scene = scenarios[choice]
    else:
        scene = "No Scene Selected"

    if username in session:
        sessionData = session[username]
        sessionData.append(scene)
        session[username] = sessionData
        text = session[username]
    else:
        session[username] = []

    # scene = "West of House. You are standing in an open field west of a white house, with a boarded front door.  There is a small mailbox here."
    # inputs = tokenizer.encode(scene, return_tensors='pt')
    # outputs = model.generate(inputs, max_length=200, do_sample=True)
    # text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    # scenariosData = text
    # scenariosData = jsonify({"newScene": text})
    return redirect(url_for("getresults", text = text))



@app.route("/results/<text>")
def getresults(text):
    # produce_list = [{"Name": "Potato", "Type": "Vegetable"}, {"Name": "Cherry", "Type": "Fruit"}]
    return render_template('results.html', results3 = text)
    # return render_template('results.html', results3 = produce_list)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
