import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Book


class BookTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "bookshelf_test"
        self.database_path = "postgresql://{}:{}@{}/{}".format(
            "postgres", "123paradise", "localhost:5432", self.database_name
        )
        setup_db(self.app, self.database_path)

        self.new_book = {"title": "Anansi Boys", "author": "Neil Gaiman", "rating": 5}

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    # def test_create_book(self):
    #     res = self.client().post('/books', json=self.new_book)
    #     data = json.loads(res.data)
    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertTrue(data['created'])
    #     self.assertTrue(len(data['books']))

    # def test_405_method_not_allowed_cannot_create_book(self):
    #     res = self.client().post('/books/43', json=self.new_book)
    #     data = json.loads(res.data)
    #     self.assertEqual(res.status_code, 405)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 'This method is not allowed for the requested URL')


    # def test_delete_book(self):
    #     res = self.client().delete('/books/12')
    #     data = json.loads(res.data)
    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertTrue(data['deleted'],10)
    #     self.assertTrue(data['total_books'])
    #     self.assertTrue(len(data['books']))

    # def test_405_delete_entire_book(self):
    #     res = self.client().delete('/books')
    #     data = json.loads(res.data)
    #     self.assertEqual(res.status_code, 405)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 'This method is not allowed for the requested URL')

    # def test_422_delete_nonexistent_book(self):
    #     res = self.client().delete('/books/1000')
    #     data = json.loads(res.data)
    #     self.assertEqual(res.status_code, 422)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'],'Unprocessable')
    
    # def test_update_rating(self):
    #     res = self.client().patch('/books/8', json={'rating':3})
    #     book = Book.query.filter(Book.id==8).one_or_none()
    #     data = json.loads(res.data)
    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertEqual(book.format()['rating'], 3)

    # def test_404_sent_requesting_beyond_valid_page(self):
    #     res = self.client().get('/books?page=1000', json={'rating': 5})
    #     data = json.loads(res.data)
    #     self.assertEqual(res.status_code, 404)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], "Resource not found")

    # def test_400_failed_update_rating(self):
    #     res = self.client().patch('/books/7')
    #     data = json.loads(res.data)
    #     self.assertEqual(res.status_code, 400)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 'Bad request sent')

     # @TODO: Write tests for search - at minimum two
    #        that check a response when there are results and when there are none
    def test_search(self):
        res = self.client().post('/books', json={'search':'Novel'})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['books'])
        self.assertTrue(data['total_books'])

    def test_search_without_result(self):
        res = self.client().post('/books', json={'search':'abracadabra'})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['books'], 0)
        self.assertTrue(data['total_books'], 0)
    
    def tearDown(self):
        """Executed after reach test"""
        pass
# @TODO: Write at least two tests for each endpoint - one each for success and error behavior.
#        You can feel free to write additional tests for nuanced functionality,
#        Such as adding a book without a rating, etc.
#        Since there are four routes currently, you should have at least eight tests.
# Optional: Update the book information in setUp to make the test database your own!


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()