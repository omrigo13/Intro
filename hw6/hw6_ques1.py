# *************** EXERCISE 6 ***************

# **************************************************************
# ************************ QUESTION 1 **************************
def partition(lst,values_lst,count_liora = 0, count_yossi = 0, mem = {}):
    """
    gets a list of building prices to divide between Liora and Yossi
    :param list lst: list of buildings prices to divide between liora and yossi
    :param tuple values_lst: first cell represents the value liora should get
    and second cell represents the value yossi should get
    :param int count_liora: counts how much buildings goes to liora
    :param int count_yossi: counts how much buildings goes to yossi
    :param dict mem: memorization dictonary to save lists for better recursion
    :return: a list of Liora and Yossi names in order of buildings prices each
    one should get
    :rtype: list
    """
    if len(lst) == 1:
        if values_lst[0] == 0:#base case
            current_owner = "Yossi"
        else:
            current_owner = "Liora"
        if not(0 in values_lst and lst[0] in values_lst):#base case
            return []
        elif count_yossi < 2 and current_owner != "Yossi":#base case
            return []
        elif count_liora <2 and current_owner != "Liora":#base case
            return []
        else:
            if values_lst[0] == 0:#base case
                return ["Yossi"]
            else:
                return ["Liora"]
    key = (values_lst, count_liora, count_yossi)#memorization
    if key not in mem:
        if values_lst[0] >= lst[0]:
            give_Liora = partition(lst[1:], (values_lst[0] - lst[0], values_lst[1]), count_liora+1,count_yossi, mem)#recursive call
            if give_Liora:
                mem[key] = ["Liora"] + give_Liora
                return mem[key]
        if values_lst[1] >= lst[0]:
            give_Yosi = partition(lst[1:], (values_lst[0],values_lst[1] - lst[0]), count_liora,count_yossi+1, mem)#recursive call
            if give_Yosi:
                mem[key] = ["Yossi"] + give_Yosi
                return mem[key]
    return []