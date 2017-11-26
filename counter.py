""" A program that stores and updates a counter using a Python pickle file"""

from os.path import exists
import sys
from pickle import dump, load


def update_counter(file_name, reset=False):
    
    if exists(file_name) or reset == False:
        f = open(file_name, 'rb+')
        count = pickle.load(f) + 1
        f.close()

        f = open(file_name,'wb')
        pickle.dump(count,f)
        f.close()
        return count

    else:
        f = open(file_name, 'wb')
        count = 1
        pickle.dump(count,f)
        f.close()
        return count



if __name__ == '__main__':
    if len(sys.argv) < 2: