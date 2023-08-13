
def ft_tqdm(lst: range) -> None:
    """
    Decorate an iterable object, returning an iterator which acts exactly
    like the orignal iterable, but prints a dynamically updating
    progressbar every time a value is requested.
    """
    total = len(lst)
    for item in lst:
        print("{index:3d}%|".format(index = int(item * 100 / total)) + "█" * int(item * 102 / total) + " " * (102 - int(item * 102 / total))+ "|", (int(item * 102 / total) + 2), end="\r")
        # print(item, end="\r")
        yield item

    print("100%|" + "█" *  (int(total * 100 / total) + 2) + " " * (100 - int(total * 102 / total))+ "|", (int(total * 100 / total) + 2))

    # print("100%|" + "█" * 103 + "|")
print()
    # print(lst[0])