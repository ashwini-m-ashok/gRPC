import logging
from concurrent import futures

import grpc
import library_pb2 as library_pb2
import library_pb2_grpc as library_pb2_grpc

"""
The Python implementation of the GRPC InventoryService.InventoryService server.
"""


class InventoryService(library_pb2_grpc.InventoryServiceServicer):
    # Books database
    books = {'9780439708180': library_pb2.Book(title='Harry Potter and the Sorcerer\'s Stone',
                                               isbn='9780439708180',
                                               author='J.K. Rowling', genre=library_pb2.Genre.FICTION,
                                               publishedYear=1997),
             '9780439064873': library_pb2.Book(title='Harry Potter and the Chamber of Secrets',
                                               isbn='9780439064873',
                                               author='J.K. Rowling', genre=library_pb2.Genre.FICTION,
                                               publishedYear=1998),
             '9780439136365': library_pb2.Book(title='Harry Potter and the Prisoner of Azkaban',
                                               isbn='9780439136365',
                                               author='J.K. Rowling', genre=library_pb2.Genre.FICTION,
                                               publishedYear=1999)}

    def GetBook(self, request, context):
        """
        Get a book from the database
        :param request: ISBN of the book to be retrieved
        :param context: gRPC context
        :return: GetBookReply with the book and a message
        """
        print(request.isbn)
        if str(request.isbn) in self.books.keys():
            return library_pb2.GetBookReply(book=self.books[request.isbn],
                                            message='Book found. Status Code: ' + str(grpc.StatusCode.OK.value[0]))
        return library_pb2.GetBookReply(
            message='Book not found. Status Code: ' + str(grpc.StatusCode.NOT_FOUND.value[0]))

    def CreateBook(self, request, context):
        """
        Create a book in the database
        :param request: Book details of the book to be created
        :param context: gRPC context
        :return: message
        """
        if str(request.isbn) == '':
            return library_pb2.CreateBookReply(
                message='ISBN found to be empty ' + str(grpc.StatusCode.INVALID_ARGUMENT.value[0]))
        # Check if the book already exists
        if str(request.isbn) in self.books.keys() and self.books[request.isbn].title == request.title:
            # If the book already exists, return an error
            return library_pb2.CreateBookReply(message='Book already exists. Status Code: '
                                                       + str(grpc.StatusCode.ALREADY_EXISTS.value[0]))
        # If the book does not exist, add it to the database with key as the ISBN and value as the book
        self.books[request.isbn] = library_pb2.Book(title=request.title, isbn=request.isbn,
                                                    author=request.author, genre=request.genre,
                                                    publishedYear=request.publishedYear)
        return library_pb2.CreateBookReply(message='Book created. Status Code:  ' + str(grpc.StatusCode.OK.value[0]))


def serve():
    """
    Start the server
    :return:
    """
    port = '50051'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    library_pb2_grpc.add_InventoryServiceServicer_to_server(InventoryService(), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == '__main__':
    """
    Main function
    """
    logging.basicConfig()
    serve()
