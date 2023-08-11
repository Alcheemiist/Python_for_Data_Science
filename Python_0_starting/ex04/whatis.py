import sys 

def whatis(arg):
    assert arg.isdigit() or (arg[0] == '-' and arg[1:].isdigit()), "argument is not an integer"

    if (int(arg) % 2 == 0):
        print("I'm Even")
    else:
        print("I'm Odd")
    return

# assert sys.argv.lenght() > 2, "more than one argument is provided"
assert sys.argv.__len__() <= 2, "more than one argument is provided"
if (sys.argv.__len__() == 2):
    whatis(sys.argv[1])



