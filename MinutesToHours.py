#!/usr/bin/env python3

import sys

def Hours(minute):
    if minute < 0:
        raise ValueError("Number is less then zero")
    else:
        return "{} H,{} m".format(int(minute/60),minute%60)

try:
    print(Hours(int(sys.argv[1])))
except:
    print("Parameter Error");
