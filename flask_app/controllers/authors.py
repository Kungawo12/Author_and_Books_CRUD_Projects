from flask import render_template,request, redirect
from flask_app import app
from flask_app.models.author import Author

@app.route('/')
def index():
    return redirect('/authors')

@app.route('/authors')
def authors():
    return render_template("authors.html",authors =Author.get_author())

@app.route("/authors/add_author", methods=['POST'])
def add_author():
    data= {
        "name": request.form["name"]
    }
    Author.add_author(data)
    return redirect('/authors')

@app.route("/authors/delete/<int:id>")
def delete(id):
    data={
        "id": id
    }
    Author.delete(data)
    return redirect("/authors")