
def ft_filter(function_to_apply, list_of_inputs):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    
    if function_to_apply is None:
        newList = [x for x in list_of_inputs if x]
        return (iter(newList))
    assert hasattr(list_of_inputs, '__iter__') , "TypeError: " + str(type(list_of_inputs)) + " object is not iterable"
    newList = [x for x in list_of_inputs if function_to_apply(x)]
    return (iter(newList))