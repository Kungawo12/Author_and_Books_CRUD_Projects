from flask import render_template,request, redirect
from flask_app import app
from flask_app.models import author,book

@app.route('/')
def index():
    return redirect('/authors')

@app.route('/authors')
def authors():
    return render_template("authors.html",authors =author.Author.get_all())

@app.route("/create/author", methods=['POST'])
def create():
    data= {
        "name": request.form["name"]
    }
    author.Author.save(data)
    return redirect('/authors')

@app.route("/authors/delete/<int:id>")
def delete(id):
    data={
        "id": id
    }
    author.Author.delete(data)
    return redirect("/authors")

@app.route("/authors/<int:id>")
def show_fav_books(id):
    data={
        "id": id
    }
    return render_template("author_fav_book.html",author=author.Author.get_author_with_book(data),unfavorited_books= book.Book.unfavorited_books(data))

@app.route("/authors/add_fav_authors", methods=['POST'])
def add_fav_authors():
    data= {
        'author_id': request.form['author_id'],
        'book_id': request.form['book_id']
    }
    author.Author.add_favorite(data)
    return redirect(f'/authors/{request.form['author_id']}')