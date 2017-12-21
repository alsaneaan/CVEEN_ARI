''' 
This module contains a function that will create a dictionary

'''

from collections import defaultdict
def make_dictionary(keys, values):
    '''
    This function will take two arguments
    Both arguments will be lists
    The function will return a dictionary containing keys from keys list and values from values list
    
    '''
   

    dictionary = {}
    for k in keys:
        for v in values:
            dictionary[k]=v 
    return dictionary
        