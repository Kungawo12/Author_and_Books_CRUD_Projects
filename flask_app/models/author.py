from flask_app.config.mysqlconnection import connectToMySQL


class Author:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def get_author(cls):
        query= "SELECT * FROM authors"
        results = connectToMySQL("book_db").query_db(query)
        authors= []
        for author in results:
            authors.append(cls(author))
        return authors

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