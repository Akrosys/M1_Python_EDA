from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome to my app"

books=[
    {
        'id': 1,
        'titre' : 'un titre',
    },
    {
        'id': 2,
        'titre': 'un autre titre random',
    }
]

#Création de route avec un book instancié
@app.route("/api/books/", methods=['GET'])
def booklist() :
	return jsonify(books)

@app.route('/api/books/<int:book_id>', methods=['GET'])
def book_id_search(book_id):
    #On parcourt les instance du json
    for book in books:
        if book['id'] == book_id:
            return jsonify(book)
    return "Aucun livre"

@app.route('/api/books/<string:book_title>', methods=['GET'])
def book_title_search(book_title) :
    for book in books :
        if book['titre'] == book_title :
            return jsonify(book)
    return "Aucun livre"

##Création de route avec le book JSON
##Import du bookJSON
def loadJson(path):
    f = open(path)
    loadedJson = json.load(f)
    f.close()
    return loadedJson

booksJSON= loadJson('data/books.json')

@app.route("/api/booksJSON/", methods=['GET'])
def booklistJSON() :
	return jsonify(booksJSON)

@app.route('/api/booksJSON/isbn/<string:book_isbn>', methods=['GET'])
def bookJSON_isbn_search(book_isbn):
    #On parcourt les instance du json
    for bookJSON in booksJSON:
        if bookJSON['isbn'] == book_isbn:
            return jsonify(bookJSON)
    return "Aucun livre"

@app.route('/api/booksJSON/titre/<string:book_title>', methods=['GET'])
def bookJSON_title_search(book_title) :
    for book in booksJSON :
        if book['title'] == book_title :
            return jsonify(book)
    return "Aucun livre"

#Exec du code
if __name__ == '__main__':
    app.run(debug=True)