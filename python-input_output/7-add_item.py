#!/usr/bin/python3
"""
    Write a script that adds all arguments to a Python list
    , and then save them to a file
"""

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
import sys


filename = "add_item.json"

if load_from_json_file(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []
python_list = sys.argv[1:]
save_to_json_file(my_list, filename)