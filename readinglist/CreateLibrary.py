def StartBookCase():
    book_case = {
        'title': [],
        'format': [],
        'fiction': [],
        'completed': [],
        'reread': [],
        'female': [],
        'poc': [],
        'foreign': [],
        'goodreads': []
    }
    return (book_case)


def MakeBookCard():
    '''
    Make empty questionnaire for user to enter  book information
    :return:
    '''
    book_card = {
        'title': {'question': 'What is the title of the book?',
                  'answer': ''},
        'format': {'question': 'What format was the book read in?',
                   'answer': '',
                   'values': ['paperback', 'hardcover', 'audiobook', 'kindle''']
                   },
        'fiction': {'question': 'Was the book fiction?',
                    'answer': '',
                    'values': [0, 1]
                    },
        'completed': {'question': 'Has the book been completed?',
                      'answer': '',
                      'values': [0, 1]
                      },
        'reread': {'question': 'Was this the first reading?',
                   'answer': '',
                   'values': [0, 1]
                   },
        'female': {'question': 'Is the author female?',
                   'answer': '',
                   'values': [0, 1]
                   },
        'poc': {'question': 'Is the author a POC?',
                'answer': '',
                'values': [0, 1]
                },
        'foreign': {'question': 'Is the author non-American?',
                    'answer': '',
                    'values': [0, 1]
                    },
        'goodreads': {'question': 'What is the Goodreads book score?',
                      'answer': '',
                      'type': float
                      },
    }
    return (book_card)
