# *************** EXERCISE 8 ***************

# **************************************************************
# *********************** Frozen_Item Class *************************
from Shop_Item import Shop_Item
from List_Item import List_Item

class Frozen_Item(Shop_Item, List_Item):
    """
    represents a Frozen Item in supermarket
    """
    def __init__(self, max_temp, exp_date, item_id, item_name, unit_price, qty, request = None):
        """
        builds a  new Frozen Item object with all the arguments
        """
        Shop_Item.__init__(self, item_id, item_name, unit_price)
        List_Item.__init__(self, qty, request)
        self.max_temp = max_temp
        self.exp_date = exp_date