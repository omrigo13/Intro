# *************** EXERCISE 2 ***************

# **************************************************************
# ************************ QUESTION 1 **************************
def print_digits_frame(digit):
    """gets a digit and prints digit+2 rows with specific conditions"""
    print(("#")*(digit+2))
    strLine = ""
    NumOfRows = digit
    for i in range(1,digit+1):#runs over all the numbers between 1 and the digit
        strLine = strLine + str(i) #string of the numbers between 1 to i
        print("|"+ strLine + " "*(NumOfRows-1) + "|")#prints a row with the conditions
        NumOfRows = NumOfRows -1 #Number of empty chars(spaces)
    print(("#")*(digit+2))
           
# **************************************************************
# ************************ QUESTION 2 **************************
def compress_text(to_compress):
    """get a string and return a list with counter of chars in a string"""
    countChars = 1
    countCharsList =[]
    ListIndex = 0
    for i in range(0,len(to_compress)-1):#runs over the string to compare chars in a string
        if(to_compress[i]) == (to_compress[i+1]):#equals chars adds 1 to the counter
            countChars = countChars + 1
        else:#insert the counter and the char as a list to a new list
            countCharsList.insert(ListIndex,[to_compress[i],countChars])
            ListIndex = ListIndex + 1
            countChars = 1
    if (len(to_compress)-2 == i and to_compress[i]==to_compress[i+1]):#add to the list the last char and the count of him
        countCharsList.append([to_compress[i],countChars])
    else:#if the last char is different, adds at the end of the list a list with the new char and the counter = 1
        countCharsList.append([to_compress[i+1],countChars])
    return countCharsList

def evaluate_compression(original_text,compressed_text):#returns a calculation of string length/2*number of counter chars list 
    return len(original_text)/(len(compressed_text)*2)

# **************************************************************
# ************************ QUESTION 3 **************************
def calculate_average_grade(students,feedback):
    """get a list of tuples with students and grades. return avg of grades and prints feedback for grades if feedback is true"""
    average_grade = 0
    sumGrades = 0
    for i in range(0,len(students)):#runs on the students grades
        sumGrades = sumGrades + students[i][1]#summary of the grades
    average_grade = sumGrades/len(students)#average of the grades
    print('Average grade: ' + str(average_grade))
    if feedback == True:#print feedback for students
        print_feedbacks(students,average_grade)
    
def print_feedbacks(students,average_grade):
    """get a list of tuples (students, grades) and avg grade. print feedback depends on grade compare to avg"""
    for i in range(0,len(students)):
        if students[i][1] >= average_grade:
            print('Good Job, '+students[i][0]+"!")
        else:
            print('You can do better, '+students[i][0]+"!")