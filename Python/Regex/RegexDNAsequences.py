#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 21 17:10:27 2018

@author: cyril
"""
import re
from re import search

brin1 = "1 TTTACGCCATTCATAGCGAGTAATGCCATAGCGTCCGGAGGTGCATATGCTTAATCGACTT"
brin2 = "2 CCGCTTGCGCGAATAATAGCCAGTCTTGGACATAGGGCATCTCGATAGTGCTATCTGAGGT"
brin3 = "3 TCGTCTTATATGGTAATACGGAGTCAGTAGAATTGTGAGTTATGTAGGGAGAGCTCACTGG"
brin4 = "4 ATAGCGCTGAGATGGTTTTGTATGGACACGTTGATCAGTTACACATGAAACTCTGGGAACG"
brin5 = "5 CGCGGCCGTATCAGGAAAAACGTATTCGCAACCGACGTTAACGCACTTCATGACGTCGACG"
brin6 = "6 ATGAACTTCGGTCATGTATCACAAGCTACAGAGTCGGATGTACACAAAACGTTTTGACGTC"
brin7 = "7 TCCGCGCTCCCACTTCTTGTGATTCAAACTATTAGCCCGCACGTTATTGGAGTATCCAAAG"
brin8 = "8 TCGTTCCTGGCTATAGAACCGGCTAACTAGGTACAATACCTATGAGCCCTCGGTGGCTTTA"
brin9 = "9 GCATTGGCCGGGGGTGTGCCCTAATACCCTCATCTGTTTGCCTCCTAAGATCGAGAGGCCC"

banqueGenes =[brin1,brin2,brin3,brin4,brin5,brin6,brin7,brin8,brin9]

print("Everyone wants to be a CAT... ")
for i in banqueGenes:
    minou = re.search(r"CAT", i) != None
    if minou:
        print(i)

print()
print("Thug Life... ")
for j in banqueGenes:
    gangsta = re.search(r"GTA", j) != None
    if gangsta:
        print(j)

print()
print("Trop à gauche... ")
for k in banqueGenes:
    drapeauRouge = re.search(r"CGT", k) != None
    if drapeauRouge:
        print(k)

#Ok, GTA et CGT sont des regex trop proches (l'ironie); après la CGT, il y a
#probablement un A après

print()
print("Horreur absolu... ")
for a in banqueGenes:
    lovecraft = re.search(r"AAA", a) != None
    if lovecraft:
        print(a)

print()
print("C'est de la m... ")
for m in banqueGenes:
    ohshjt = re.search(r"CACA", m) != None
    if ohshjt:
        print(m)

print()
print("Lady... ")
for g in banqueGenes:
    starlette = re.search(r"GAGA", g) != None
    if starlette:
        print(g)

print()
print("Tatie... ")
for t in banqueGenes:
    mariepierre = re.search(r"TATA",t) != None
    if mariepierre:
        print(t)





