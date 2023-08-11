import math 

def NULL_not_found(object: any) -> int:
    if object == None:
        print("Nothing: " ,object, " " , type(object))
    elif object == 0:
        print("Zero: " ,object, " " , type(object))
    elif object == '':
        print("Empty: " ,object, " " , type(object))
    elif object == False:
        print("Fake: " ,object, " " , type(object))
    elif isinstance(object, float) and math.isnan(object):
        print("Cheese: " ,object, " " , type(object))
    else:
        print("Type not Found")
    return 1