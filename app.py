# Imports

import os
from flask import Flask, render_template, request, url_for
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


# EMAILJS_KEY' stored in Enviroment Variables

app.secret_key = os.environ.get("SECRET_KEY")
EMAILJS_KEY = os.environ.get("EMAILJS_KEY")


# Function to load 'Home' page as default

@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html")


# Function to load 'Gallery' page

@app.route('/gallery')
def gallery():
    return render_template("gallery.html")


# Function to load 'Showreels' page

@app.route('/showreels')
def showreels():
    return render_template("showreels.html")


# Function to load 'Bio' page

@app.route('/bio')
def bio():
    return render_template("bio.html")


# Function to load 'Profile' page

@app.route('/profile')
def profile():
    return render_template("profile.html")


# Function to load 'Profile' page

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
