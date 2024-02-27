from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author
class Book:
    def __init__(self,data):
        self.id = data['id']
        self.title= data['title']
        self.num_of_page= data['num_of_page']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.authors = []
        
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books"
        results= connectToMySQL("book_db").query_db(query)
        
        books = []
        for book in results:
            books.append(cls(book))
        return books
    
    @classmethod
    def get_one_book(cls,data):
        query = """SELECT * FROM books
                WHERE id = %(id)s;
        """
        results = connectToMySQL("book_db").query_db(query,data)
        return cls(results[0])
    
    @classmethod
    def save(cls,data):
        query= """ INSERT INTO books(title, num_of_page)
                VALUE(%(title)s, %(num_of_page)s);
        """
        return connectToMySQL("book_db").query_db(query,data)
    
    @classmethod
    def unfavorited_books(cls,data):
        query= """ SELECT * FROM books WHERE books.id NOT IN
                (SELECT book_id FROM favourites WHERE author_id= %(id)s)
        """
        results= connectToMySQL('book_db').query_db(query,data)
        books=[]
        for book in results:
            books.append(cls(book))
        return books

    @classmethod
    def get_books_with_authors(cls,data):
        
        query= """ SELECT * FROM books LEFT JOIN favourites ON books.id =
                favourites.book_id LEFT JOIN authors ON authors.id = favourites.author_id WHERE 
                books.id = %(id)s;
        """
        results = connectToMySQL('book_db').query_db(query,data)
        book =  cls(results[0])
        for row in results:
            if row['authors.id'] == None:
                break
            author_data= {
                'id': row['authors.id'],
                'name': row['name'],
                'created_at': row['created_at'],
                'updated_at': row['updated_at']
            }
            book.authors.append(author.Author(author_data))
        return book