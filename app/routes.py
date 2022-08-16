from app import app
from flask import render_template


@app.route('/')
def index():

    favorite_artists = ['Aphex Twin', 'Carpenter Brut', 'Boards of Canada', 'deadmau5', 'Joe Hisaishi', 'Pink Floyd']

    favorite_drinks = ['Iced Blonde Vanilla Latte', 'Brown Sugar Cream Cold Brew', 'Iced Mocha with cinnamon', 'Iced Matcha Vanilla Latte', 'Cold Brew']

    return render_template('index.html', drinks= favorite_drinks, artists=favorite_artists)