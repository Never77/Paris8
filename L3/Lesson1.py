#!/usr/bin/env python
# coding: utf-8

"""
Lecon N°1

Bases algorithmiques
"""

# float: 0.1
# int: 0
# str: "hello"
# char: "a"
# bool: True ou False
# array: [ "str", 12, 1.0, True ]
# dict: {}

def sub(a: int, b: int):
    return int(a) - int(b)

def add(a:int, b:int):
    return a + b

def sub2(a: int, b: int):
    r = int(a) - int(b)
    if r % 2 == 0:
        return 0
    else:
        return r

def add2(a:int, b:int):
    # TODO : faire la meme chose avec un ternaire
    return 3 if int(a) + int(b) % 1 == 0 else int(a) + int(b)

"""
4 | 2
    _
4   Q = 2
_
R = 0 

4 / 2 = 2 <= Q
4 % 2 = 0 <= R
"""

if __name__ == "__main__":
    print('Hello World!')
    a = 12
    b = 13
    # print(f" a = {type(a)}")
    # print(f" b = {type(b)}")

    print(sub(a, b))

    c = 2

    r = c if c % 2 == 0 else c + 1
    
    compteur = [1, 2, 3, 4, 5]
     
    print(compteur[1])

    i = 0

    # while condition est vrai:
    #     code

    while i < 5:
        print(compteur[i])
        i += 1

    for j in compteur:
        print(j)
    
    liste_de_lettre = "abcdef"
    
    for letter in liste_de_lettre:
        print(letter)