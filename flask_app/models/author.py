from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book

class Author:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.books = []
    @classmethod
    def get_all(cls):
        query= "SELECT * FROM authors"
        results = connectToMySQL("book_db").query_db(query)
        authors= []
        for author in results:
            authors.append(cls(author))
        return authors

    @classmethod
    def get_one(cls,data):
        query = """SELECT * FROM authors
                WHERE id = %(id)s;
        """
        results = connectToMySQL("book_db").query_db(query,data)
        return cls(results[0])
    
    @classmethod
    def save(cls,data):
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
    def unfavorited_authors(cls,data):
        query= """ SELECT * FROM authors WHERE authors.id NOT IN
                (SELECT author_id FROM favourites WHERE book_id= %(id)s)
        """
        results= connectToMySQL('book_db').query_db(query,data)
        authors=[]
        for author in results:
            authors.append(cls(author))
        return authors
    
    @classmethod
    def add_favorite(cls,data):
        query= """ INSERT INTO favourites(author_id,book_id)
                VALUES(%(author_id)s, %(book_id)s)
        """
        return connectToMySQL('book_db').query_db(query,data)
    
    @classmethod
    def get_author_with_book(cls,data):
        query= """SELECT * FROM authors LEFT JOIN favourites ON authors.id= favourites.author_id
                LEFT JOIN books ON books.id = favourites.book_id WHERE authors.id = %(id)s;
        """
        results = connectToMySQL("book_db").query_db(query,data)
        author = cls(results[0])
        for row in results:
            if row['books.id'] == None:
                break
            book_data = {
                'id': row['books.id'],
                'title': row['title'],
                'num_of_page': row['num_of_page'],
                'created_at': row['created_at'],
                'updated_at': row['updated_at']
            }
            author.books.append(book.Book(book_data))
        return author
    