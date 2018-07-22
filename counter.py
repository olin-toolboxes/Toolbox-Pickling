""" A program that stores and updates a counter using a Python pickle file"""

from os.path import exists
import sys
from pickle import dump, load


def update_counter(file_name, reset=False):
    """Update a counter stored in the file 'file_name'.

    A new counter will be created and initialized to 1 if none exists or if the
    reset True.

    If the counter already exists and reset is False, the counter's value will
    be incremented.

    Parameters
    ----------
    file_name: str
        The file that stores the counter to be incremented.  If the file
        doesn't exist, a counter is created and initialized to 1.
    reset: bool
        True if the counter in the file should be reset.

    Returns
    -------
    int
        The new counter value

    Examples
    --------
    >>> update_counter('blah.txt',True)
    1
    >>> update_counter('blah.txt')
    2
    >>> update_counter('blah2.txt',True)
    1
    >>> update_counter('blah.txt')
    3
    >>> update_counter('blah2.txt')
    2
    """
    if exists(file_name) and reset == False:
        file_ = open(file_name, 'rb+')
        counter = load(file_) + 1
        file_.close()

        file_ = open(file_name, 'wb')
        dump(counter, file_)
        file_.close()

    else:
        file_ = open(file_name, 'wb')
        counter = 1
        dump(counter, file_)
        file_.close()

    file_ = open(file_name, 'rb+')
    return load(file_)

#update_counter('how_many_grapes.txt')
#file_ = open('how_many_grapes.txt', 'rb+')
#print(load(file_))



if __name__ == '__main__':
    if len(sys.argv) < 2:
        import doctest
        doctest.testmod()
    else:
        print("new value is {}".format(update_counter(sys.argv[1])))
