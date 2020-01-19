def GetBookInformation():
    '''
    ask user for the following information:
        - book title
        - book author
        - book format
        - if the book is:
            - fiction
            - completed
            - re-read
        - if the author is:
            - female
            - a poc
            - non-American
        - the goodreads book score
    '''

    book_information = {
        'title' : {'question': 'What is the title of the book?',
                   'answer' : ''},
        'format': {'question': 'What format was the book read in?',
                  'answer': ''},
        'fiction': {'question': 'Was the book fiction?',
                  'answer': ''},
        'completed': {'question': 'Has the book been completed?',
                  'answer': ''},
        'reread': {'question': 'Was this the first reading?',
                  'answer': ''},
        'female': {'question': 'Is the author female?',
                  'answer': ''},
        'poc': {'question': 'Is the author a POC?',
                  'answer': ''},
        'foreign': {'question': 'Is the author non-American?',
                   'answer': ''},
        'goodreads': {'question': 'What is the Goodreads book score?',
                'answer': ''},
    }

    for k in book_information.keys():
        this_question = book_information[k]['question']
        print(this_question)
        this_answer = input()
        book_information[k]['answer'] = this_answer

    return(book_information)
