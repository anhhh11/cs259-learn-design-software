def max_f(list,func):
    """ Return max of list using func to rank
        equal to max(list,key=func) in Python
    """
    maxe=None
    pos=None
    for i in range(len(list)):
        result = func(list[i])
        if result > maxe or maxe is None:
            maxe = result
            pos=i
    return list[pos]