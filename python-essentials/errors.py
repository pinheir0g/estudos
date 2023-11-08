#!/usr/bin/env python3

import sys

# EAFP - Easy to Ask Forgiveness than permission

try:
    names = open("names.txt").readlines()  # FileNotFoundError
except FileNotFoundError as e:  # capturando a exception
    print(f"[Error] {str(e)}.") # tratando a exception
    sys.exit(1)

try:
    print(names[2])
except:
    print("[Error] Missing name in the list")
    sys.exit(1)
