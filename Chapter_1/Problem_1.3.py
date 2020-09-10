# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 22:10:21 2020

@author: Nikola
"""


#Problem 1.3
s = input('prompt: ')

s_len = len(s)
count = 0
max_count = 1
start_pos = 0

i = 1
pos = 0

for i in range(s_len):
    if s[i] > s[i-1] or s[i] == s[i-1]:
        count += 1
        if count > max_count:
            max_count = count
            start_pos = pos
    else:
        count = 1
        pos = i
    i += 1

substr = s[start_pos:(start_pos + max_count)]
print("Longest substring in alphabetical order is: ", substr)
