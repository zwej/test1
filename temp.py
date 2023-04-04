# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def prime_number(a):
    s=True
    for i in range(1,a):
        if a%i==0 :
            s=False
    if not s:
        pass
    else:
        print(str(a) + "is a prime number")
        
for i in range(1,500):
    prime_number(i)