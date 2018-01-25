# imports
import os
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash


app = Flask(__name__)  # create the application instance
app.config.from_object(__name__)  # load config from this file , OGvis.py

# Load default config and override config from an environment variable
app.config.update(dict(
))


@app.route('/')
def homepage():
    """
    Shows the user the homepage
    """
    return render_template('index.html')


@app.route('/gallery')
def gallery():
    """
    Serve up the gallery page
    """
    return render_template('gallery/gallery.html')