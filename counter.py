""" A program that stores and updates a counter using a Python pickle file"""

from os.path import exists
import sys
from pickle import dump, load
import pickle
import os.path

def update_counter(file_name, reset=False):
    """ Updates a counter stored in the file 'file_name'

    A new counter will be created and initialized to 1 if none exists or if
    the reset flag is True.

    If the counter already exists and reset is False, the counter's value will
    be incremented.

    file_name: the file that stores the counter to be incremented.  If the file
    doesn't exist, a counter is created and initialized to 1.
    reset: True if the counter in the file should be rest.
    returns: the new counter value

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
    if os.path.exists(file_name)== False:
    	f = open(file_name, '')
    	pickle.dump(1, f)
    	f.close()
    if reset == True:
    	f = open(file_name, 'wb')
    	pickle.dump(1, f)
    	f.close()
    else:
    	f = open(file_name, 'br')
    	#print(f)
    	filecounter = pickle.load(f)
    	f.close()
    	f = open(file_name, 'wb')
    	
    	filecounter+=1
    	
    	pickle.dump(filecounter, f)
    	f.close()


    input_file = open(file_name, 'rb')
    counter = pickle.load(input_file)
    #print(counter)
    f.close()
    return counter

"""
These files were used in my textmining project
"""
def loadbooks():
	"""
	Loads books from gutenberg.org. Book id has to be manualy changed each book.
	"""
	downloaded_book = requests.get('http://www.gutenberg.org/ebooks/1522.txt.utf-8').text
	return downloaded_book

def savebook(book_text, filename):
	"""
	Saves a the text of a book into a file. 
	"""
	f = open(filename, 'wb')
	pickle.dump(book_text, f)
	f.close()

def opensavedbook(file):
	"""
	Opens a file that is saved on the computer
	"""
	input_file = open(file, 'rb')
	opened_text = pickle.load(input_file)
	return opened_text
	
if __name__ == '__main__':
    if len(sys.argv) <= 2:
        import doctest
        doctest.testmod()
    else:
        print("new value is " + str(update_counter(sys.argv[1])))
