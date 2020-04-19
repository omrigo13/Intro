# *************** EXERCISE 8 ***************

# **************************************************************
# *********************** Fruit_Veggie_Item Class *************************
from Shop_Item import Shop_Item
from List_Item import List_Item

class Fruit_Veggie_Item(Shop_Item, List_Item):
    """
    represents vegetable or fruit in supermarket
    """
    def __init__(self, farm_name, isFruit, vitamins, item_id, item_name, unit_price, qty, request = None):
        """
        builds a new vegetable or a fruit object with all the arguments
        """
        Shop_Item.__init__(self, item_id, item_name, unit_price)
        List_Item.__init__(self, qty, request)
        self.farm_name = farm_name
        self.isFruit = isFruit
        self.vitamins = vitamins
       
    def number_vitamins(self):
        """
        :return: number of vitamins in vegetable or fruit object
        :rtype: int
        """
        return len(self.vitamins)
    
    def __repr__(self):
        """
        prints the string represents fruit or vegetable object with all the details
        """
        if self.isFruit:
            return Shop_Item.__repr__(self) + "\n" \
                   + List_Item.__repr__(self) + "\n" \
                   + "farm: " + self.farm_name + ", fruit, " + str(self.number_vitamins()) + " vitamins"
        return Shop_Item.__repr__(self) + "\n" \
                   + List_Item.__repr__(self) + "\n" \
                   + "farm: " + self.farm_name + ", vegetable, " + str(self.number_vitamins()) + " vitamins"