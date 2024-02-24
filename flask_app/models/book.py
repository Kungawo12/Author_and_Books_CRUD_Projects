from flask_app.config.mysqlconnection import connectToMySQL

class Book:
    def __init__(self,data):
        self.id = data['id']
        self.title= data['title']
        self.num_of_page= data['num_of_page']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.authors = []
        
    @classmethod
    def get_book(cls):
        
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
    def add_book(cls,data):
        query= """ INSERT INTO books(title, num_of_page)
                VALUE(%(title)s, %(num_of_page)s);
        """
        return connectToMySQL("book_db").query_db(query,data)
    
    @classmethod
    def get_books_with_authors(cls,data):
        from flask_app.models.author import Author
        query= """ SELECT * FROM books LEFT JOIN favourites ON favourites.book_id =
                books.id LEFT JOIN authors ON favourites.author_id = authors.id WHERE 
                books.id = %(id)s;
        """
        results = connectToMySQL('book_db').query_db(query,data)
        book =  cls(results[0])
        for row in results:
            author= {
                'id': row['authors.id'],
                'name': row['name'],
                'created_at': row['created_at'],
                'updated_at': row['updated_at']
            }
            book.authors.append(Author(author))
        return book