#!/usr/bin/env python

"""
Main file for running word-challenge game
"""

# Imports
from flask import Flask, render_template, request

# Make a flask app class instance for running the game
app = Flask(__name__)
app.config['DEBUG'] = True # debugging mode on or off

# Create home URL route
@app.route('/')
#def ui():
#   return render_template("ui.html")


# Adding another page if wanted
#@app.route('/page2')

if __name__ == '__main__':
   app.run()
