# *************** EXERCISE 4 ***************

# **************************************************************
# ************************ QUESTION 2 **************************

import urllib.request

def add_prefixes(prefix_dict , input_string):
    """
    adds all prefixes of a word to a dictionary
    :param dict prefix_dict: dictionary represents prefixes of words
    :param str input_string: a word
    :return: None, updates all prefixes of a word in the dictionary
    :rtype: None
    """
    for i in range(1, len(input_string) + 1):
        if input_string[:i] not in prefix_dict:#adds a prefix with the word to the dictionary
            prefix_dict[input_string[:i]] = [input_string]
        elif input_string not in prefix_dict[input_string[:i]]:#adds a word to the list of an exist prefix in the dictionary 
            prefix_dict[input_string[:i]].append(input_string)

def add_all_prefixes(prefix_dict , word_list):
    """
    adds all prefixes of a word list to a dictionary
    :param dict prefix_dict: dictionary represents prefixes of words
    :param list word_list: a list of words
    :return: None, updates all prefixes of all the words in the dictionary
    :rtype: None
    """
    for word in word_list:
        add_prefixes(prefix_dict, word)

def init_from_url(webpage):
    """
    show a dictionary with all the prefixes of a webpage
    :param str webpage: a text with words
    :return: dictonary of all prefixes with all the words in the text webpage
    :rtype: dict
    """
    with urllib.request.urlopen (webpage) as url:
	    text = str(url.read(), 'utf-8')
    words = text.split()
    prefixes = {}
    add_all_prefixes(prefixes, words)
    return prefixes

def autocomplete(prefix_dict , prefix):
    """
    show the recommendations of all the words to complete a certain prefix
    :param dict prefix_dict: dictionary represents prefixes of words
    :param str prefix: a prefix of words
    :return: all the words that starting with the prefix from the dictionary
    :rtype: int
    """
    return prefix_dict.get(prefix, [])