# Imports

import os
from flask import Flask, render_template, redirect, request, url_for
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


# EMAILJS_KEY' stored in Enviroment Variables

EMAILJS_KEY = os.environ.get("EMAILJS_KEY")


# Function to load 'Home' page as default

@app.route('/')
def home():
    return render_template("index.html")


# Function to load 'Contact' page

@app.route('/contact')
def contact():
    return render_template("contact.html",
                           EMAILJS_KEY=EMAILJS_KEY)


# Functions to handle 404 & 500 errors


@app.errorhandler(404)
def page_not_found(error):
    return render_template('error-messages/404.html'), 404


@app.errorhandler(500)
def something_wrong(error):
    return render_template('error-messages/500.html'), 500


# IP and PORT

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=False)
