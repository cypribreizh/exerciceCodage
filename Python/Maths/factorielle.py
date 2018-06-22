#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  4 15:56:40 2018

@author: cyril
"""

# 5 ! = 1*2*3*4*5

def factorielle(nombre):
    calcul = 1
    for i in range(1 , nombre+1):
        calcul *= i
    return calcul

print(factorielle(7))

        
        
