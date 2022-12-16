def get_list_of_book_titles(InventoryClient, isbns):
    """
    This function returns a list of book titles when given a list of ISBNs
    :param InventoryClient: Client object
    :param isbns: list of ISBNs
    :return: list of book titles
    """
    book_titles = []
    for isbn in isbns:
        book = InventoryClient.get_book(isbn)
        if book:
            book_titles.append(book.book.title)
        else:
            book_titles.append('')
    return book_titles
