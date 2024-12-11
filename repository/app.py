from flask import Flask, request, jsonify
from repository import get_all_books, add_book, delete_book

app = Flask(__name__)

@app.route('/')
def hello():
    return "try /books"


@app.route('/books', methods=['GET'])
def list_books():
    books = get_all_books() 
    return jsonify(books)

@app.route('/books', methods=['POST'])
def create_book():
    data = request.json
    add_book(data['title'], data['author'])
    return jsonify({"message": "Book added successfully!"})

@app.route('/books/<int:book_id>', methods=['DELETE'])
def remove_book(book_id):
    delete_book(book_id)
    return jsonify({"message": "Book deleted successfully!"})

if __name__ == '__main__':
    app.run(debug=True)
