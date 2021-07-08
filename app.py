from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension


import stories

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)


# change to variable
@app.route("/")
def menu():
    """Render dropdown menu for storytype"""
    return render_template("menu.html")


@app.route("/questions")
def question():
    """Render questions.html template and pass Story.prompts as an argument"""

    story_type = request.args["dropdown"]
    story = stories.type_of_stories[story_type]

    return render_template("questions.html",
                           prompts=story.prompts, storytypes=story_type
                           )


@app.route("/results")
def result():
    """Render story.html when the form is submitted, given a dictionary of prompts"""

    story = stories.type_of_stories[request.args["storytype"]]
    return render_template("story.html", story=story.generate(request.args))
