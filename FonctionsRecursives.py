#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  8 08:23:18 2018

@author: cyril
"""

def factorielle(n):
    if (n==1):
        return 1
    else:
         return n * factorielle (n-1)

print(factorielle(6))

def fibbonacci(n):
    if (n==0) or (n==1):
        return 1
    else:
        return fibbonacci(n-1) + fibbonacci(n-2)

print(fibbonacci(6))
        