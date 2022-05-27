#!/usr/bin/env python3

# import pandas as pd

import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import json 
from flask import Flask, render_template, redirect, url_for, request, session, jsonify

app = Flask(__name__)#boilerplate, needed for flask to work
app.secret_key = "Secret Key" #secret key is needed for flask session to work, its a boilerplate

#We kept the dictionary structure simple, so we can just access it via key.  scenarios[key]
scenarios = {
    "Dune" : "It was a warm night at Castle Caladan, and the ancient pile of stone that had served the Atreides family as home for twenty-six generations bore that cooled-sweat feeling it acquired before a change in the weather.",
    "Star Wars": "A long time ago in a galaxy far, far away…A NEW HOPE It is a period of civil war. Rebel spaceships, striking from a hidden base, have won their first victory against the evil Galactic Empire. During the battle, Rebel spies managed to steal secret plans to the Empire’s ultimate weapon, the DEATH STAR, an armored space station with enough power to destroy an entire planet. Pursued by the Empire’s sinister agents, Princess Leia races home aboard her starship, custodian of the stolen plans that can save her people and restore freedom to the galaxy….", 
    "Hitchhikers":"The house stood on a slight rise just on the edge of the village. It stood on its own and looked out over a broad spread of West Country farmland. Not a remarkable house by any means—it was about thirty years old, squattish, squarish, made of brick, and had four windows set in the front of a size and proportion which more or less exactly failed to please the eye."
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/scenarios")
def showscenarios():
    if request.method == 'GET':
        return jsonify(scenarios)

@app.route("/input", methods = ["POST"])
def sendScene():
    # tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
    # model = GPT2LMHeadModel.from_pretrained('gpt2')

    if request.method == "POST":
        scene = ""
        choice = ""
        username = ""
        dostuff = ""
        text = {}

        if request.form.get("choice"): # if choice input field isn't empty
            choice = request.form.get("choice") # grab the value from choice input field and assign it to choice variable
        if request.form.get("username"):
            username = request.form.get("username")
        if request.form.get("dostuff"):
            dostuff = request.form.get("dostuff")
        
        # Our session data will look like this {"Scenes": ["old scene", "scne 2", "scn 3", "scn 4"]}

        if username in session: #a session can contain keys associated with a users, if the user already exists in the session, then grab the session data and do stuff with it
            sessionData = session[username] #sessionData is a temporary variable to reference the session of the user, when they do exist
            sessionData["Scenes"].append(scene)#we decide how our session data is structered, in this case, our session data is in the form of a list, so we can append more stuff to it
            session[username] = sessionData #we cannot modify the list from the session directly, so we have to reassign the session data to our temporary sessionData that we appended stuff to
            text = session[username] #set the text to our new updated session data
            # text["Scenes"].append(dostuff)
            scene = " ".join(text)
            # scene = " ".join(text["Scenes"])
            print(scene)
        else:
            if (choice in scenarios.keys()): #if the choice that the user selected is in the scenarios dictionary, key() just returns a list of keys from the dictionary
                scene = scenarios[choice] #assign a scenario to the scene
            else:
                scene = "No Scene Selected"
            session[username] = {"Scenes":[scene]} #if the session doesn't exist for the user, create one.  This is how we create one

        # textoutput = "dummy"
        # inputs = tokenizer.encode(scene, return_tensors='pt')
        # outputs = model.generate(inputs, max_length=200, do_sample=True)
        # textoutput = tokenizer.decode(outputs[0], skip_special_tokens=True)
        textoutput = scene + dostuff
        result = {"Old Scene": scene, "New Scene": textoutput}
        return redirect(url_for("getresults", text = result))


@app.route("/results/<text>")
def getresults(text):
    #Because we are using url_for, text will come in as a string and not a dictionary
    #The string uses single quotes, so replace it with double quotes to make it a json string
    text = text.replace("\'", "\"")
    jsonresp = json.loads(text)
    return render_template('results.html', results3 = jsonresp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
