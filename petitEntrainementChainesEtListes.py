#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 14 08:12:38 2018

@author: cyril
"""

petiteListe = "Mickael Jackson", "Mariah Carey", "Rihanna", "Elvis"

if "Mickael Jackson" in petiteListe:
    print("Yi hee !")

if "Mariah Carey" in petiteListe:
    print("HeartBreaker, you take the Best of me... Aaaooouuuuuu !!!")

if "Elvis" in petiteListe:
    print("Aouh oum, Yeaah eeeh !")

MaryPoppins = "Supercalifragilisticexpialidocious"

if MaryPoppins in petiteListe:
    print("C'est pas possible")

print(MaryPoppins[5:12])
print(MaryPoppins[15:22])
print(MaryPoppins[25:len(MaryPoppins)])

JustinBieber = "Baby "*3 +"Oooooh Right !"
print(JustinBieber)

Lovecraft = "Ph'nglui Mglw'nafh Cthulhu R'lyeh Wgah'nagl Fhtagn"
AaahCounter = []

#for i in Lovecraft:
#    AaahCounter.append("Aaaaah !!!")
#    
#print(AaahCounter)

print(len(petiteListe))
print(len(MaryPoppins))
print(len(Lovecraft))
