from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension


import stories 

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)


#change to variable
@app.route("/")
def menu():
    """Render dropdown menu for storytype"""
    storytype = request.args.get("dropdown")
    return render_template("menu.html")

@app.route("/questions/")
def question():
    """Render questions.html template and pass Story.prompts as an argument"""

    storytype = request.args.get("dropdown")
    story = stories.type_of_stories.get(storytype)
    return render_template("questions.html",
                           prompts=story.prompts
                           )


@app.route("/questions/results")
def result():
    """Render story.html when the form is submitted, given a dictionary of prompts"""
    storytype = request.args.get("dropdown")
    story = stories.type_of_stories.get(storytype)
    return render_template("story.html", story=story.generate(request.args))
