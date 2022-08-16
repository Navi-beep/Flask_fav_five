from app import app
from flask import render_template


@app.route('/')
def index():

    favorite_artists = ['Aphex Twin', 'Carpenter Brut', 'Boards of Canada', 'deadmau5', 'Joe Hisaishi', 'Pink Floyd']


    return render_template('index.html', artists=favorite_artists)


@app.route('/cats')
def cats():

    favorite_drinks = ['Iced Blonde Vanilla Latte', 'Brown Sugar Cream Cold Brew', 'Iced Mocha with cinnamon', 'Iced Matcha Vanilla Latte', 'Cold Brew']

    return render_template('cats.html', drinks= favorite_drinks)