# *************** EXERCISE 8 ***************

# **************************************************************
# *********************** Meat_Item Class *************************
from Shop_Item import Shop_Item
from List_Item import List_Item

class Meat_Item(Shop_Item, List_Item):
    """
    represents a Meat Item in supermarket
    """
    def __init__(self, butcher_name, exp_date, weight, item_id, item_name, unit_price, qty, request = None):
        """
        build a  new Meat Item object with all the arguments
        """
        Shop_Item.__init__(self, item_id, item_name, unit_price)
        List_Item.__init__(self, qty, request)
        self.butcher_name = butcher_name
        self.exp_date = exp_date
        self.weight = weight
        
    def __repr__(self):
        """
        prints Meat Item details with butcher name, exp date of item and weight of item
        """
        res = Shop_Item.__repr__(self)
        res += "\n" + List_Item.__repr__(self)
        return res + "\n" + "butcher: " + self.butcher_name + ", exp: " + self.exp_date + ", " + str(self.weight) + "g"