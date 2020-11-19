from flask import Flask, render_template, request
from jinja2 import Template
import json

app = Flask(__name__)
book=[
  {
      'id': 1,
      'titre' : 'A la recherche du temps perdu',
  },
  {
      'id': 2,
      'titre': 'Les identités meutrières',
  }
]

book_json = json.loads(book)

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
    return json.dumps(book)

@app.route("/api/books/numero")
def numero():
    return book_json

if __name__ == '__main__':
    app.run(debug=True)
