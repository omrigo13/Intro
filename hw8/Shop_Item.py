# *************** EXERCISE 8 ***************

# **************************************************************
# *********************** Shop_Item Class *************************
class Shop_Item:
    """
    details of Item in supermarket
    """
    def __init__(self, item_id, item_name, unit_price):
        """
        builds a new object with the details of the item
        """
        self.item_id = item_id
        self.item_name = item_name
        self.unit_price = unit_price
        
    def __repr__(self):
        """
        prints the item details, item id, name and price
        """
        return "id: " + self.item_id + ", name: " + self.item_name + ", price: " + str(self.unit_price) + " nis"