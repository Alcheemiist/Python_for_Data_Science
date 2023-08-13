import sys

def Count_String(data):
    """Count the number of characters in a string"""
    upper = len(list(filter(str.isupper, data)))
    lower = len(list(filter(str.islower, data)))
    number = len(list(filter(str.isdigit, data)))
    space = len(list(filter(str.isspace, data)))
    punctuation = len(list(filter(lambda x: x in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~', data)))

    print("The text contains {x} characters:".format(x=len(data)))
    print(upper, " upper letters")
    print(lower, " lower letters")
    print(punctuation, " punctuation marks")
    print(space, " spaces")
    print(number, " digits")
    return

def main():
    """Main function"""
    if len(sys.argv) == 1:
        data = input("What is the text to count?\n")
    elif len(sys.argv) == 2:
        data = sys.argv[1]
    else:
        assert sys.argv.__len__() <= 2, "Too many arguments. Only one argument is allowed"
    Count_String(data)

if __name__ == "__main__":
    main()