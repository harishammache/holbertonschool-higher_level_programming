#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0

    for index in my_list[:x]:
        try:
            if type(index) is not int:
                continue
            else:
                print("{:d}".format(index), end="")
                count += 1
        except (IndexError, TypeError, ValueError):
            continue
    print()
    return count
