from flask_frozen import Freezer
from flask import Flask, render_template
from app import app

#app=Flask(__name__)
freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()