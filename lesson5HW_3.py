#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 21:35:39 2021

@author: 蔡侑廷
"""
x=int(input('number of students? '))
score=[]


a=0



for i in range(x):
    w=int(input('score?'))
    score.append(w)
    if a<=w:
        a=w

print(a)



