from flask import render_template,request, redirect
from flask_app import app
from flask_app.models import book,author

@app.route('/books')
def books():
    return render_template("books.html",books= book.Book.get_all())

@app.route("/create/book", methods=["POST"])
def save():
    data= {
        'title': request.form['title'],
        'num_of_page': request.form['num_of_page']
    }
    book.Book.save(data)
    return redirect('/books')

@app.route("/books/<int:id>")
def author_fav(id):
    data={
        "id": id
    }
    return render_template("show_fav_books.html",book = book.Book.get_books_with_authors(data),unfavorited_author=author.Author.unfavorited_authors(data))

@app.route("/books/add_fav_books", methods=['POST'])
def add_fav_books():
    data= {
        'author_id': request.form['author_id'],
        'book_id': request.form['book_id']
    }
    author.Author.add_favorite(data)
    return redirect(f'/books/{request.form['book_id']}')