from readinglist.Librarian import book_card
from readinglist.Librarian import librarian_script


def create_empty_book():
    book = {
        'title': [],
        'author': [],
        'format': [],
        'fiction': [],
        'completed': [],
        'reread': [],
        'female': [],
        'poc': [],
        'foreign': [],
        'goodreads': []
    }
    return book


def start_new_book():
    book = {}
    for k in book_card.keys():
        card_details = book_card[k]
        new_value = librarian_script(part=k,
                                     question=card_details['question'],
                                     type_=card_details['type'],
                                     min_=card_details['min'],
                                     max_=card_details['max'],
                                     range_=card_details['range']
                                     )
        book[k] = [new_value]
    return book
