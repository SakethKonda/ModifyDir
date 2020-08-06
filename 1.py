#!/usr/bin/env python3

import re

def error_msg(line):
    result = re.search("Error: ([\w ]+) ",line)
    return result[1]

def error_user(line):
    result = re.search("\((\w+)\)")
    return result[1]

def info_user(line):
    result = re.search("\((w+)\)")
    return result[1]
