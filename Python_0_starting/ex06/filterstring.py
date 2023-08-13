from ft_filter import ft_filter

def main():

    print("-------- test __doc__ --------")
    print(filter.__doc__)
    print("-------- test case 1 --------")
    name = "helloHEYhello"
    new_name = filter(str.isupper, name)
    for x in new_name:  
        print(x)

    print("-------- test case 2 --------")
    name = "mehdi"
    last_name = filter(None, name)
    for y in last_name:
        print(y)
    print("-------- test Non-iterable argument --------")
    # # assertion error # 
    print(filter(str.isupper, "HELLO"))

if __name__ == '__main__':
    main()