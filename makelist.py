#!/usr/bin/env python3

import os
import sys

def print_file(file,n):
    print('{}{}'.format(' '*(n),file))

def print_dir(dir_name,n):
    if n == 0:
        print(dir_name.upper().center(40,'-'))
    elif n >= 2:
        print('{}{}'.format(' '*(n-2),dir_name.upper()))
    elif n>3:
        print('{}{}'.format(' '*(n-2),dir_name.capitalize()))
    dir_ls = [i for i in os.listdir() if i[0]!='.']
    for file in dir_ls:
        if os.path.isdir(file):
            os.chdir(file)
            print_dir(file,n+2)
            os.chdir('..')
        if os.path.isfile(file):
            print_file(file,n+2)

dir_name = sys.argv[1]
os.chdir(dir_name)
print_dir(dir_name,0)
