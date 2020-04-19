# *************** EXERCISE 8 ***************

# **************************************************************
# *********************** Shopping_List Class *************************
from Shop_Item import Shop_Item
from Meat_Item import Meat_Item

class Shopping_List:
    """
    supermarket class represents shopping list
    """
    def __init__(self, sl_id, customer_name, items = []):
        """
        builds a new shopping list object
        """
        self.sl_id = sl_id
        self.customer_name = customer_name
        self.items = items
    
    def get_id(self):
        """
        :return: returns shopping list id
        :rtype: str
        """
        return self.sl_id
    
    def get_customer_name(self):
        """
        :return: returns customer name
        :rtype: str
        """
        return self.customer_name
    
    def total_price(self):
        """
        :return: returns total price of shopping list
        :rtype: float
        """
        return sum(item.unit_price * item.qty for item in self.items)
    
    def __add__(self, items):
        """
        updates shopping list with list of items or 1 item
        """
        if isinstance(items, list):
            self.items = self.items + items
        else:
            self.items = self.items + [items]
    def item_summary(self):
        """
        :return: returns list of all items in shopping list and quantity of each one
        :rtype: list
        """
        return [(item.item_name,item.qty) for item in self.items]
    
    def is_empty(self):
        """
        :return: returns True if the shopping list is empty and false otherwise
        :rtype: bool
        """
        return self.items == []
    
    def __gt__(self,other):
        """
        :return: returns True if the shopping list is bigger than other 
        shopping list and False otherwise
        :rtype: bool
        """
        if self.total_price() > other.total_price():#compare total price shoping lists
            return True
        elif self.total_price() == other.total_price():
            if sum(item.qty for item in self.items) > sum(item2.qty for item2 in other.items):
                #compare quantity difference between 2 shopping lists
                return True
        count_self = 1
        count_other = 1
        for item in self.items:
            if item.item_id != self.items[0].item_id:
                count_self += 1
        for item2 in other.items:
            if item2.item_id != other.items[0].item_id:
                count_other += 1
        if self.total_price() == other.total_price() and sum(item.qty for item in self.items) == \
        sum(item2.qty for item2 in other.items) and count_self > count_other:
            #compare number of items id difference between 2 shopping lists
            return True
        return False
    def __repr__(self):
        """
        prints the shopping list deatils with shopping list id, number of products
        in the shopping list, number of items in the shopping list and total price
        """
        return '*'*30 + '\n' \
                + "List id: " + self.sl_id + '\n' \
                + "Number of Products: " + str(len(self.items)) + '\n' \
                + "Number of Items: " + str(sum(self.items[i].qty for i in range(len(self.items)))) + '\n' \
                + "Total Price: " + str(self.total_price()) + '\n'\
                + '*'*30
                
    

butcher = "The Art of Meat"
exp = "22/1/2019"
weight = 350
item_id2 = "6015"
item_name2 = "Sirloin"
unit_price2 = 53
qty2 = 3
test4_stud = Meat_Item(butcher , exp ,
weight,
item_id2, item_name2 , unit_price2, qty2)
print(str(test4_stud))
