def store_book(book, book_case=None):
    '''
    This function will put a book onto the book case
    :param book: dictionary of book information
    :param book_case:  dictionary of stored book library
    :return: book_case: updated dictionary of stored book library
    '''

    if book_case is None:
        book_case = book

    for k in book_case.keys():
        book_case[k] += book[k]

    return (book_case)
