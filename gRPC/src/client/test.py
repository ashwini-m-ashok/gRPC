import unittest
from unittest.mock import Mock, MagicMock

import get_book_titles
from src.client.inventory_client import InventoryClient
from src.service import library_pb2

client = InventoryClient('localhost', 50051)

"""
    This test is to verify that the get_book_titles function returns a list of book titles
    when given a list of ISBNs.
"""


class InventoryClientTest(unittest.TestCase):

    def test_get_list_of_book_titles(self):
        """
            This test is to verify that the get_book_titles function returns a list of book titles
            when given a list of ISBNs with a mock client
        """
        self.mock = Mock(spec=InventoryClient)

        def side_effect(isbn):
            if isbn == '9780439708180':
                return library_pb2.GetBookReply(
                    book=library_pb2.Book(title='Harry Potter and the Sorcerer\'s Stone',
                                          isbn='9780439708180',
                                          author='J.K. Rowling',
                                          genre=library_pb2.Genre.FICTION,
                                          publishedYear=1997), message='Book found. Status Code: 0')
            elif isbn == '9780439064873':
                return library_pb2.GetBookReply(
                    book=library_pb2.Book(title='Harry Potter and the Chamber of Secrets',
                                          isbn='9780439064873',
                                          author='J.K. Rowling',
                                          genre=library_pb2.Genre.FICTION,
                                          publishedYear=1998), message='Book found. Status Code: 0')
            elif isbn == '9780439136365':
                return library_pb2.GetBookReply(
                    book=library_pb2.Book(title='Harry Potter and the Prisoner of Azkaban',
                                          isbn='9780439136365',
                                          author='J.K. Rowling',
                                          genre=library_pb2.Genre.FICTION,
                                          publishedYear=1999), message='Book found. Status Code: 0')

        self.mock.get_book = MagicMock(side_effect=side_effect)
        # wrong isbns check
        correct_isbns = ['9780439708180', '9780439064873', '9780439136365']
        self.assertEqual(
            get_book_titles.get_list_of_book_titles(self.mock, correct_isbns),
            ["Harry Potter and the Sorcerer's Stone",
             'Harry Potter and the Chamber of Secrets',
             'Harry Potter and the Prisoner of Azkaban'])

        # wrong isbns check
        wrong_isbns = ['978043A708180', '9780439B64873', '97804391C6365']
        self.assertEqual(['', '', ''], get_book_titles.get_list_of_book_titles(self.mock, isbns=wrong_isbns))

    def test_get_book_with_real_client(self):
        """
            This test is to verify that the get_book_titles function returns a list of book titles
            when given a list of ISBNs with a real client
        :return:
        """

        # correct isbns check
        self.assertEqual(
            get_book_titles.get_list_of_book_titles(client, ['9780439708180',
                                                             '9780439064873',
                                                             '9780439136365']),
            ["Harry Potter and the Sorcerer's Stone",
             'Harry Potter and the Chamber of Secrets',
             'Harry Potter and the Prisoner of Azkaban'])

        # wrong isbns check
        self.assertEqual(
            get_book_titles.get_list_of_book_titles(client, ['978043A708180',
                                                             '9780439B64873',
                                                             '97804391C6365']),
            ['', '', ''])


if __name__ == '__main__':
    unittest.main()
