# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 21:52:07 2020

@author: Nikola
"""

s = input("please put input: ")

s_len = len(s)
counter = 0
i = 0
for i in range(s_len):
    char = s[i]
    if char == 'a' or char == 'i' or char == 'e' or char == 'o' or char == 'u':
        counter += 1
    i += 1

print("Number of vowels: ", counter)