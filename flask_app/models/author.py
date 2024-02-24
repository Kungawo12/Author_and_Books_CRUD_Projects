from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.book import Book

class Author:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.books = []
    @classmethod
    def get_author(cls):
        query= "SELECT * FROM authors"
        results = connectToMySQL("book_db").query_db(query)
        authors= []
        for author in results:
            authors.append(cls(author))
        return authors

    @classmethod
    def get_one_author(cls,data):
        query = """SELECT * FROM authors
                WHERE id = %(id)s;
        """
        results = connectToMySQL("book_db").query_db(query,data)
        return cls(results[0])
    
    @classmethod
    def add_author(cls,data):
        query = """INSERT INTO authors(name)
                VALUE (%(name)s);
        """
        return connectToMySQL("book_db").query_db(query,data)
    
    @classmethod
    def delete(cls,data):
        query=""" DELETE FROM authors 
                WHERE id = %(id)s;
        """
        results = connectToMySQL("book_db").query_db(query,data)
        return results
    
    @classmethod
    def get_author_with_book(cls,data):
        query= """SELECT * FROM authors LEFT JOIN favourites ON favourites.author_id= authors.id
                LEFT JOIN books ON favourites.book_id = books.id WHERE authors.id = %(id)s;
        """
        results = connectToMySQL("book_db").query_db(query,data)
        author = cls(results[0])
        for row in results:
            book = {
                'id': row['books.id'],
                'title': row['title'],
                'num_of_page': row['num_of_page'],
                'created_at': row['created_at'],
                'updated_at': row['updated_at']
            }
            author.books.append(Book(book))
        return author
    