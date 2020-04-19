# *************** EXERCISE 5 ***************

# **************************************************************
# ************************ QUESTION 1 **************************
def movie_pointer(schedule,time):
    """
    gets a dictonary of movies and times, and a specific time and return the 
    place of the movie in the list of movies. ordered by time
    :param dict schedule: dictionary represents key - movie as string and
    value - movie times as tuple
    :param tuple time: tuple represents movie times
    :return: index of movie name in list of movies
    :rtype: int
    """
    lst = sorted(schedule.values())
    for i in range(len(lst)):
        if lst[i] == time:#index of movie time
            return i
    return 0
        
def sort_movies(schedule):
    """
    gets a dictonary and returns a list of movie names in order of time
    :param dict schedule: dictionary represents key - movie as string and
    value - movie times as tuple
    :return: list of movie names ordered by time
    :rtype: list
    """
    movie_names = [""]*len(schedule.values())
    for name,movie in (schedule.items()):
        movie_names[movie_pointer(schedule,movie)] = name#insert the movie name to the right place in the list
    return movie_names

def search_movie(movies, free_time, start, end):
    """
    gets a movies list and a specific time and range of 2 numbers to search
    between them. returns the movie name if found and None otherwise
    :param list movies: list of tuples that represents movie start and end time
    :param tuple free_time: represents movie start and end time
    :param start: starting position to looking from for a movie in the list
    :param end: ending position to looking from for a movie in the list
    :return: name of a movie
    :rtype: string
    """
    if start > end:#base case
        return None
    middle = (start+end)//2
    if free_time == movies[middle][1]:
        return movies[middle][0]
    elif free_time < movies[middle][1]:
        return search_movie(movies, free_time, start, middle-1)#recursive call
    else:
        return search_movie(movies, free_time, middle+1, end)#recursive call
    
# **************************************************************
# ************************ QUESTION 2 **************************
def find_max(numbers_set,length,index,max_set,count):
    """
    gets a list of integer numbers and return the longest increasing 
    subsequence
    :param list numbers_set: represents a list of integer numbers
    :param int length: represents length of list. should be initilized as len
    of the list to run over all the list combinations
    :param int index: represents index in the list. should be initilized as 0
    outside the function to start from the beginning of the list
    of the list
    :param int max_set: an integer in the list to check if the next one is bigger
    :param int count: counts the length of increasing subsequence
    :return: the longest increasing subsequence
    :rtype: integer
    """
    if index == length:#base case
        return count
    max_set1 = find_max(numbers_set,length,index+1,max_set,count)#recursive call
    if numbers_set[index] > max_set:#increasing subsequence count + 1
        max_set2 = find_max(numbers_set, length, index + 1, numbers_set[index], count + 1)#recursive call
        if max_set2 > max_set1:#max subsequence
            max_set1 = max_set2
    return max_set1

def max_sub_set(numbers_set):
    """
    gets a list of integer numbers and return the longest increasing 
    subsequence as size of that list
    :param list numbers_set: a list of random integers bigger than 0
    :return: longest increasing subsequence
    :rtype: integer
    """
    index,max_set,count,length = 0,0,0,len(numbers_set)
    return find_max(numbers_set,length,index,max_set,count)