# *************** EXERCISE 9 ***************

# **************************************************************
# *********************** BigNumber Class *************************
from QueueModule import Queue

class BigNumber:
    """
    represents a BigNumber using Queue and gets a number as a str
    """
    def __init__(self, num):
        """
        builds a new BigNumber from number as a str
        :param str num: a number represents BigNumber
        """
        if not isinstance(num,str):
                raise TypeError ("BigNumber init expected str")
        self.digits = Queue()
        for digit in num:
            self.digits.enqueue(digit)
        q1 = Queue()
        while not self.digits.is_empty():
            q1.enqueue(self.digits.dequeue())
        while not q1.is_empty():
            if not q1.front().isdigit():
                raise TypeError ("The number contains non digit characters")
            self.digits.enqueue(q1.dequeue()) 

    def converted(self):
        """
        convert BigNumber to str number using Queue
        """
        number = ""
        q1 = Queue()
        while not self.digits.is_empty():
            q1.enqueue(self.digits.dequeue())#add all the digits to a temp Queue
        while not q1.is_empty():
            number += q1.front()#adds all the digits to a new str number
            self.digits.enqueue(q1.dequeue())#adds all digits back to the default Queue
        return number
    
    def __str__(self):
        """
        :return: returns the number as a str
        :rtype: str
        """
        return self.converted()
    
    def __eq__(self, other):
        """
        :param BigNumber other: a BigNumber object represets a number
        :return: True if the two BigNumbers are equall and False otherwise
        :rtype:bool
        """
        if not isinstance(other, BigNumber):
            raise TypeError ("Can only compare two BigNumbers")
        return int(str(self)) == int(str(other))
    
    def __gt__(self, other):
        """
        :param BigNumber other: a BigNumber object represets a number
        :return: True if the first BigNumber is bigger than the second one
        False otherwise
        :rtype:bool
        """
        if not isinstance(other, BigNumber):
            raise TypeError ("Can only compare two BigNumbers")
        return int(str(self)) > int(str(other))

    def read_and_return_biggest(self, path):
        """
        :param str path: gets a path of txt file with numbers
        :return: returns the biggest BigNumber from the txt file and the object
        itself
        :rtype: BigNumber
        """
        try:
            numbers = open(path, "r")
            max_big_number = self
            number = numbers.readline()
            while number != "":#runs over the numbers in the file
                if BigNumber(number.replace("\n","")) > max_big_number:
                    max_big_number = BigNumber(number.replace("\n",""))#saves the max big number
                number = numbers.readline()
            numbers.close()
            return max_big_number
        except:
            print("Could not open file")
      
    def add_number_to_file(self, path):
        """
        adds the BigNumber to an exisiting txt file
        :param str path: gets a path of existing txt file
        """
        try:
            numbers = open(path, "r")
            numbers = open(path, "a")
            numbers.write(str(self))#adds the BigNumber to the file
            numbers.write("\n")#adds enter line to the file \n
            numbers.close()
        except:
            print("Could not open file")