
def ft_tqdm(lst: range) -> None:
    """
    Decorate an iterable object, returning an iterator which acts exactly
    like the orignal iterable, but prints a dynamically updating
    progressbar every time a value is requested.
    """
    total = len(lst)
    for item in lst:
        print("{index:3d}%|".format(index = int(item * 100 / total)) + "█" * int(item * 102 / total) + " " * (102 - int(item * 102 / total))+ "|",\
        str(item) + "/" + str(total) +" [{index:d}:{yindex:d}<{index2:d}:{yindex2:d}, {index3:.2f}it/s]".format(index=00, yindex=00, index2=00,yindex2=00, index3=100), end="\r" )
        yield item

    print("100%|" + "█" *  (int(total * 100 / total) + 2) + " " * (100 - int(total * 102 / total))+ "|",\
    str(total) + "/" + str(total)+ " [{index:d}:{yindex:d}<{index2:d}:{yindex2:d}, {index3:.2f}it/s]".format(index=00, yindex=00, index2=00,yindex2=00, index3=100) )

print()