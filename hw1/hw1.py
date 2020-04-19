# *************** EXERCISE 1 ***************

# **************************************************************
# ************************ QUESTION 1 **************************
def question1(a1, an, n):
    #sum of numbers (n*(a1+an)/2)
    if(n==0):
        return 0
    elif (n==1):
        return a1
    else:
        return ((n*(a1+an))/2)
# **************************************************************
# ************************ QUESTION 2 **************************
def question2(x):
    #modulo 3 and modulo 5 checking
    for i in range(1,x+1):
        if ((i%5==0) and (i%3==0)):
            print('GUMIGAM')
        elif (i%5==0):
            print('BO')
        elif (i%3==0):
            print('SHOKO')
        else:
            print(i)
    print('**********')
# **************************************************************
# ************************ QUESTION 3 **************************
def question3(s):
    #checks if a string is a palindrome when we remove one of his characters
    NewStr = ""
    RevStr = ""
    for i in range(0,len(s)+1):
        NewStr = s[0:i]+s[i+1:len(s)]
        RevStr = NewStr[::-1]
        if(NewStr==RevStr):
            return True
        NewStr = ""
        RevStr = ""
    return False
# **************************************************************
# ************************ QUESTION 4 **************************
def question4(input_list):
    #avreage of max 2 even numbers and max 2 odd numbers
    maxEven1 = 0
    maxEven2 = 0
    maxOdd1 = 0
    maxOdd2 = 0
    for i in range(0,len(input_list)):
        if(input_list[i]==0):
            break
        elif (input_list[i]%2==0 and input_list[i]>maxEven1):
            maxEven2 = maxEven1
            maxEven1 = input_list[i]
        elif (input_list[i]%2==0 and input_list[i]>maxEven2):
            maxEven2 = input_list[i]
        if(input_list[i]%2!=0 and input_list[i]>maxOdd1):
            maxOdd2 = maxOdd1
            maxOdd1 = input_list[i]
        elif(input_list[i]%2!=0 and input_list[i]>maxOdd2):
            maxOdd2 = input_list[i]
    return((maxEven1+maxEven2+maxOdd1+maxOdd2)/4)
    
    
    
    
    