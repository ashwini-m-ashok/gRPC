from __future__ import print_function

import logging

import grpc

from src.client.get_book_titles import get_list_of_book_titles
from src.service import library_pb2_grpc, library_pb2

"""
    This is the client for the inventory service. It is used to get book information from the inventory service.
"""


class InventoryClient(object):
    localhost_port = 50051

    # Reference: https://stackoverflow.com/questions/65052746/python-grpc-how-to-reuse-channel-correctly
    def __init__(self, host: str, port: int):
        """
            This is the constructor for the InventoryClient class.
            param host:  The host of the inventory service.
            param port: The port of the inventory service.
        """
        self._server_address = host + ':' + str(port)
        channel = grpc.insecure_channel(self._server_address)
        self.stub = library_pb2_grpc.InventoryServiceStub(channel)

    def get_book(self, isbn):
        """
        This function is used to get a book from the inventory service.
        param isbn: ISBN of the book to get.
        :return: The book with the given ISBN.
        """
        return self.stub.GetBook(library_pb2.GetBookRequest(isbn=isbn))

    def create_book(self, title, isbn, author, genre, publishedYear):
        """
        This function is used to create a book in the inventory service.
        param title: Title of the book to create.
        param isbn: ISBN of the book to create.
        param author: Author of the book to create.
        param genre: Genre of the book to create.
        param publishedYear: Published year of the book to create.
        :return: Status code of the create book request.
        """
        return self.stub.CreateBook(library_pb2.CreateBookRequest(
            title=title,
            isbn=isbn,
            author=author,
            genre=genre,
            publishedYear=publishedYear))


if __name__ == '__main__':
    """
        This is the main function for the inventory client.
    """
    logging.basicConfig()
    client = InventoryClient('localhost', 50051)
    print(get_list_of_book_titles(client, ['9780439708180', '9780439064873', '9780439136365']))
