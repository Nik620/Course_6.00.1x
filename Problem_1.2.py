# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 21:59:54 2020

@author: Nikola
"""


#Problem 1.2
s = input("please put something: ")

counter = 0
s_len = len(s)
i = 0

for i in range(s_len - 2):
    if s[i] == 'b' and s[i+1] == 'o' and s[i+2] == 'b':
        counter += 1
    i += 1

print("Number of times bob occurs is: ", counter)