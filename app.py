from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
import stories

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.route("/")
def question():
    return render_template( "questions.html",
        prompts = silly_story.prompts
     )

@app.route("/results")
def result():
    
