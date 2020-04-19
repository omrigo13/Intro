# *************** EXERCISE 8 ***************

# **************************************************************
# *********************** List_Item Class *************************
class List_Item:
    """
    order information of a specific item in the supermarket
    """
    def __init__(self, qty, request = None):
        """
        builds a new order object of an item
        """
        self.qty = qty
        self.request = request
    
    def get_request(self):
        """
        :return: return the request of the order if exists otherwise empty string
        :rtype: str
        """
        if self.request is None:
            return ""
        return self.request
    
    def update_quantity(self, new_qty):
        """
        updates the quantity of the item in the order
        """
        self.qty =  new_qty
        
    def __repr__(self):
        """
        prints the order details with the quantity and the request if exists
        """
        if self.request is None:
            return "qty: " + str(self.qty) + ", request: None"
        return "qty: " + str(self.qty) + ", request: " + self.request