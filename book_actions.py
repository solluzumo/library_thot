#---Book actions---



def book_delete(username,book_name):
    return f"Book {book_name} from {username}' library was deleted"


def book_cont_reading(username,book_name):
    return f"Book {book_name} from {username}' library was opened"


def book_review_reading(book_name):
    return f"Here's {book_name} reviews"


def book_review_leaving(book_name):
    return f"You can leave yours review about {book_name}!"
