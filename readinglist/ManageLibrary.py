from readinglist.CreateLibrary import start_new_book
from readinglist.CreateLibrary import make_book_card


def get_book_information():
    '''
    ask user to input book information:
    '''

    book_information = make_book_card()

    for k in book_information.keys():
        this_question = book_information[k]['question']
        print(this_question)
        this_answer = [input()]
        book_information[k]['answer'] = this_answer

    return (book_information)


def store_book(book_details, book_case=None):
    '''
    This function will put a book onto the book case
    :param book_details: dictionary of output from 'GetBookInformation'
    :param book_case:  dictionary of stored book library
    :return: book_case: updated dictionary of stored book library
    '''

    if book_case is None:
        book_case = start_new_book()

    for k in book_case.keys():
        book_case[k] += book_details[k]['answer']

    return (book_case)
