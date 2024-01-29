#!/usr/bin/python3
import re
def no_c(my_string):
    new_string = re.sub('[c,C]','',my_string)
    return new_string
