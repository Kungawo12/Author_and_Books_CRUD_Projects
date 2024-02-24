from flask_app.config.mysqlconnection import connectToMySQL

class Book:
    def __init__(self,data):
        self.id = data['id']
        self.title= data['title']
        self.num_of_page= data['num_of_page']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def get_book(cls):
        query = "SELECT * FROM books"
        results= connectToMySQL("book_db").query_db(query)
        
        books = []
        for book in results:
            books.append(cls(book))
        return books
    
    @classmethod
    def add_book(cls,data):
        query= """ INSERT INTO books(title, num_of_page)
                VALUE(%(title)s, %(num_of_page)s);
        """
        return connectToMySQL("book_db").query_db(query,data)