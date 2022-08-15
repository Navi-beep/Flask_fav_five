from app import app
from flask import render_template


@app.route('/')
def index():
    my_info = {
        'name': 'Elise',
        'nickname': 'Nav-beep'
    }
    favorite_artists = ['Aphex Twin', 'Carpenter Brut', 'Boards of Canada', 'deadmau5', 'Joe Hisaishi']
    return render_template('index.html',me=my_info, artists=favorite_artists)