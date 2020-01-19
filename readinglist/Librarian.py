book_card = {
    'title': {'question': 'What is the title of the book?',
              'type': str,
              'min': None,
              'max': None,
              'range': None,
              },
    'author': {'question': 'What is the name of the author?',
              'type': str,
              'min': None,
              'max': None,
              'range': None,
              },
    'format': {'question': 'What format was the book read in?',
               'type': str,
               'min': None,
               'max': None,
               'range': ['paperback', 'hardcover', 'audiobook', 'kindle'],
               },
    'fiction': {'question': 'Was the book fiction?',
                'type': int,
                'min': 0,
                'max': 1,
                'range': None
                },
    'completed': {'question': 'Has the book been completed?',
                  'type': int,
                  'min': 0,
                  'max': 1,
                  'range': None
                  },
    'reread': {'question': 'Was this the first reading?',
               'type': int,
               'min': 0,
               'max': 1,
               'range': None
               },
    'female': {'question': 'Is the author female?',
               'type': int,
               'min': 0,
               'max': 1,
               'range': None
               },
    'poc': {'question': 'Is the author a POC?',
            'type': int,
            'min': 0,
            'max': 1,
            'range': None
            },
    'foreign': {'question': 'Is the author non-American?',
                'type': int,
                'min': 0,
                'max': 1,
                'range': None,
                },
    'goodreads': {'question': 'What is the Goodreads book score?',
                  'type': float,
                  'min': 0,
                  'max': 5,
                  'range': None
                  },
}


def librarian_script(part, question, type_=None, min_=None, max_=None, range_=None):
    if min_ is not None and max_ is not None and min_ > max_:
        raise ValueError('min_ must be less than or equal to max_')
    while True:
        answer = input(question)
        if type_ is not None:
            try:
                answer = type_(answer)
            except ValueError:
                print(part + f' type must be {type_.__name__}.')
                continue
        if max_ is not None:
            if answer > max_:
                print(part + f' must be less than or equal to {max_}.')
        elif min_ is not None:
            if answer < min_:
                print(part + f' must be greater than or equal to {min_}.')
        elif range_ is not None:
            if answer not in range_:
                print(part + f' must be in {range_}.')
        else:
            return answer
