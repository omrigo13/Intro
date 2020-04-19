# *************** EXERCISE 9 ***************

# **************************************************************
# *********************** Queue Class *************************
class Queue:
    """
    represents Queue data starcture First in First Out using list
    """
    def __init__(self):
        """
        making a new Queue data stracture object
        """
        self.queue_vals = []
        self.len = 0
    
    def enqueue(self,val):
        """
        adds an item at the end and updates the len of the Queue
        :param val: a value to add
        """
        self.queue_vals.append(val)
        self.len += 1
    
    def dequeue(self):
        """
        removes the first item from the Queue and updates the len of the Queue
        """
        if self.is_empty():
            raise IndexError("The queue is empty")
        res = self.queue_vals[0]
        self.queue_vals = self.queue_vals[1:]
        self.len -= 1
        return res
            
    def is_empty(self):
        """
        checks if there is no items in the Queue
        :return: True if empty and False otherwise
        :rtype: bool
        """
        return self.len == 0
    
    def front(self):
        """
        return the first item in the Queue
        """
        if self.is_empty():
            raise IndexError("The queue is empty")
        return self.queue_vals[0]
    
    def rear(self):
        """
        return the last item in the Queue
        """
        if self.is_empty():
            raise IndexError("The queue is empty")
        return self.queue_vals[-1]
    
    def __len__(self):
        """
        :return: return the length of the Queue
        :rtype: int
        """
        return self.len