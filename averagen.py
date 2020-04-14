#!/usr/bin/env python3
N = 4
sum = 0
count = 0
print("please input 4 numbers:")
while count < N:
    count = count + 1
    msg = "第{}个参数：".format(count)
    number = float(input(msg))
    sum = sum + number
    
average = sum / N
print("N = {},Sum = {}".format(N,sum))
print("Average = {:.2f}".format(average))
