from flask import Flask, render_template, request
from jinja2 import Template
import json

##Import du book.json
def loadJson(path):
    f = open(path)
    loadedJson = json.load(f)
    f.close()
    return loadedJson

books = loadJson('data/books.json')

app = Flask(__name__)
##Page d'accueil
@app.route("/")
@app.route("/index/")
def index():
    return render_template('index.html')

@app.route("/about/")
def about():
    return render_template('about.html', name='Onizuka')

@app.route("/api/books/", methods=["GET"])
def books():
    return 'lol'

@app.route("/api/books/numero")
def numero():
    for book in books:
        return book['titre']

if __name__ == '__main__':
    app.run(debug=True)
