#!/usr/bin/env python3

import os
import sys
import subprocess

def print_dir(dir_name,n):
    if n == 0:
        print(dir_name.upper().center(40,'-'))
    elif n >= 2:
        print('{}{}'.format(' '*(n-2),dir_name.upper()))
    elif n>3:
        print('{}{}'.format(' '*(n-2),dir_name.capitalize()))
    elif n>6:
        sys.exit(1)
    dir_ls = [i for i in os.listdir() if i[0]!='.']
    for file in dir_ls:
        if os.path.isfile(file):
            pass
            #print_file(file,n+2)
        if os.path.isdir(file):
            os.chdir(file)
            print_dir(file,n+2)
            os.chdir('..')

dir_name = sys.argv[1]
print_dir(dir_name,0)
