# *************** EXERCISE 8 ***************

# **************************************************************
# *********************** Dry_Item Class *************************
from Shop_Item import Shop_Item
from List_Item import List_Item

class Dry_Item(Shop_Item, List_Item):
    """
    represents a Dry Item in supermarket
    """
    def __init__(self, provider_name, weight, num_calories, exp_date, item_id, item_name, unit_price, qty, request = None):
        """
        builds a  new Dry Item object with all the arguments
        """
        Shop_Item.__init__(self, item_id, item_name, unit_price)
        List_Item.__init__(self, qty, request)
        self.provider_name = provider_name
        self.weight = weight
        self.num_calories = num_calories
        self.exp_date = exp_date
        
    def calories_in_100g(self):
        """
        :return: calculate the calories in 100 grams of the dry item
        :rtype: float
        """
        return (self.num_calories*100)/self.weight