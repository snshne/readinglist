import json


def store_book(book, book_case=None):
    '''
    This function will put a book onto the book case
    :param book: dictionary of book information
    :param book_case:  dictionary of stored book library
    :return: book_case: updated dictionary of stored book library
    '''

    if book_case is None:
        book_case = book

    else:
        for k in book_case.keys():
            book_case[k] += book[k]

    return (book_case)

def open_library(library_path):
    '''
    this function will open the library path (json) and load in the entered books
    :param library_path: path to where the current library dictionary is stored
    :return: dictionary of library
    '''
    with open(library_path, 'r') as fp:
        library = json.load(fp)
    return library

def close_library(library, library_path):
    '''
    this function will save the library dictionary to the library path
    :param library_path: path to where the current library dictionary is stored
    '''
    with open(library_path, 'w') as fp:
        json.dump(library, fp)
