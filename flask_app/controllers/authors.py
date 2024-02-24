from flask import render_template,request, redirect
from flask_app import app
from flask_app.models import author,book

@app.route('/')
def index():
    return redirect('/authors')

@app.route('/authors')
def authors():
    return render_template("authors.html",authors =author.Author.get_author())

@app.route("/authors/add_author", methods=['POST'])
def add_author():
    data= {
        "name": request.form["name"]
    }
    author.Author.add_author(data)
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
    return render_template("author_fav_book.html",author=author.Author.get_author_with_book(data),books = book.Book.get_book())

@app.route("/authors/add_fav/<int:id>")
def add_fav(id):
    data={
        "id":id
    }
    return redirect('/authors')