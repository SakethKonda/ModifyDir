#!/usr/bin/env python3

import os
import sys

def del_files(file_name):
    files = os.listdir(file_name)
    os.chdir(file_name)
    for file in files:
        if file.endswith("-2.jpg"):
            os.remove(file)
        if file.endswith(" (1).jpg"):
            os.remove(file)

del_files(sys.argv[1])
