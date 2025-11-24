# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 23:41:59 2018

@author: Jonas Lindemann
"""

def my_func2(p1):
    print("my_func2() p1=", p1)

    if p1 < 0:
        print("p1 mindre än 0")

def my_func1(p1):
    print("my_func() p1 =", p1)
    my_func2(p1)

    for i in range(5):
        print("i =", i)

my_func1(-2)
my_func1(1)



