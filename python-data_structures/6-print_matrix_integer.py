#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for line_matrice in matrix:
        for number in line_matrice:
            if number == line_matrice[-1]:
                print("{}".format(number), end="")
            else:
                print("{} ".format(number), end="")
        print()