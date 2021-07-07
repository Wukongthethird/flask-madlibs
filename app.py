from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension


from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)


@app.route("/")
def question():
    """Render questions.html template and pass Story.prompts as an argument"""

    return render_template("questions.html",
                           prompts=silly_story.prompts
                           )


@app.route("/results")
def result():
    """Render story.html when the form is submitted, given a dictionary of prompts"""

    return render_template("story.html", story=silly_story.generate(request.args))
