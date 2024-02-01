#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for index in my_list[:x]:
            if type(index) is not int:
                continue
            else:
                print("{:d}".format(index), end="")
                count += 1
    except IndexError:
        pass
    except TypeError:
        pass
    except ValueError:
        pass
    finally:
        print()
    return count
