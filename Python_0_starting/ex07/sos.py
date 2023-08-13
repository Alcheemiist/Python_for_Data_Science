import sys

NESTED_MORSE = { 
                    " ": "/ ", 
                    "A": ".- ", "B": "-... ", "C": "-.-. ", "D": "-.. ", "E": ". ","F": "..-. ",
                    "G": "--. ", "H": ".... ", "I": ".. ", "J": ".--- ", "K": "-.- ", "L": ".-.. ",
                    "M": "-- ", "N": "-. ", "O": "--- ", "P": ".--. ", "Q": "--.- ", "R": ".-. ",
                    "S": "... ", "T": "- ", "U": "..- ", "V": "...- ", "W": ".-- ", "X": "-..- ",
                    "Y": "-.-- ", "Z": "--.. ", "1": ".---- ", "2": "..--- ", "3": "...-- ",
                    "4": "....- ", "5": "..... ", "6": "-.... ", "7": "--... ", "8": "---.. ",
                    "9": "----. ", "0": "----- "
                }

def main():
    assert len(sys.argv) == 2, "the arguments are bad"
    message = sys.argv[1].upper()
    # print(message)
    for letter in message:  
        assert letter in NESTED_MORSE, "the arguments are bad"
        print NESTED_MORSE[letter],

if __name__ == "__main__" : main()