#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 19:36:44 2021

@author:蔡侑廷
"""

score = []
x = int(input('number of students? '))
for i in range(x):
    
    y = int(input('students score?' ))
    score.append(y)
    



total = 0

    


for t in range(x):
    total = score[t] + total
    
print('average score is ' + str (total/x))


