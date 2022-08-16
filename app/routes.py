from app import app
from flask import render_template


@app.route('/')
def index():

    favorite_artists = ['Aphex Twin', 'Carpenter Brut', 'Boards of Canada', 'deadmau5', 'Joe Hisaishi']
    return render_template('index.html', artists=favorite_artists)