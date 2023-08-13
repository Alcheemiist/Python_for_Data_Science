import sys
from ft_filter import ft_filter

def main():
    assert len(sys.argv) == 3 and sys.argv[2].isnumeric(), "the arguments are bad"
    main_list = sys.argv[1].split(" ")
    is_longer = lambda x: len(x) > int(sys.argv[2])
    result = ft_filter(is_longer, main_list)    
    print([ x for x in result])
    
if __name__ == '__main__':
    main()