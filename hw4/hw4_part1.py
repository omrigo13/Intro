# *************** EXERCISE 4 ***************

# **************************************************************
# ************************ QUESTION 1 **************************
def base_to_decimal(num_as_str, orig_base):
    """
    converts string represantation of a number in a specific base to decimal
    number.
    :param str num_as_str: string represantation of a number
    :param int orig_base: base
    :return: decimal integer
    :rtype: int
    """
    num_as_str = num_as_str[::-1]
    digits_mapping = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,
                      '9':9,'a':10,'b':11,'c':12,'d':13,'e':14,'f':15}
    total = 0
    for i in range(len(num_as_str)):
        total += digits_mapping[num_as_str[i]]*orig_base**i#sums decimal number
    return total
        
def int_to_base(decimal_number , dest_base):
    """
    converts decimal integer to a string a based on base
    :param int decimal_number:
    :param int dest_base:
    :return: a number in a certain base
    :rtype: str
    """
    str_new_base = ""
    digits_mapping = {0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',
                      9:'9',10:'a',11:'b',12:'c',13:'d',14:'e',15:'f'}
    while(decimal_number!=0):
        str_new_base += digits_mapping[decimal_number%dest_base]#sums number as string in new base
        decimal_number = decimal_number//dest_base
    return str_new_base[::-1]

def base_to_base(num_as_str, orig_base , dest_base):
    """
    converts string represantation of a number in a specific base to a string
    a based on base
    :param: str num_as_str: string represantation of a number
    :param int orig_base: base
    :param int dest_base:
    :return: a number in a certain base
    :rtype: str
    """
    return int_to_base(base_to_decimal(num_as_str, orig_base),dest_base)