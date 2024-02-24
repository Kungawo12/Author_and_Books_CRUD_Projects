from flask import render_template,request, redirect
from flask_app import app
from flask_app.models.book import Book

@app.route('/books')
def books():
    return render_template("books.html",books= Book.get_book())

@app.route("/books/add_books", methods=["POST"])
def add_books():
    data= {
        'title': request.form['title'],
        'num_of_page': request.form['num_of_page']
    }
    Book.add_book(data)
    return redirect('/books')

@app.route("/books/<int:id>")
def author_fav(id):
    data={
        "id": id
    }
    return render_template("author_fav.html",book = Book.get_books_with_authors(data))