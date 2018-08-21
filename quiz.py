#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 12:45:11 2018

@author: olli
"""

"""
login()
Käyttäjät: Olli, Tarja, Teemu, Tommi, Tiina
Tehdään class player kutakin pelaaja kohti objekti tuosta luokasta.
Objektit laitetaan player-taulukkoon.
Playeriin tulee ainakin seuraavat kentät: userName, password, 
"""
class Player:
    def __init__(self, userName, password):
        self.userName = userName
        self.password = password
        

def login():
    userName = input('Anna käyttäjätunnus: ')
    password = input('Anna salasana: ')
    loginSucceeded = False
    if userName == 'Olli' and password == 'olli':
         loginSucceeded = True
    elif userName == 'Tarja' and password == 'tarja':
        loginSucceeded = True
    elif userName == 'Teemu' and password == 'teemu':
        loginSucceeded = True
    elif userName == 'Tommi' and password == 'tommi':
        loginSucceeded = True
    elif userName == 'Tiina' and password == 'tiina':
        loginSucceeded = True
    else:
         print('Väärä tunnus tai salasana')
    p = None
    if loginSucceeded:
        p = Player(userName, password)
        print('Tervetuloa pelaamaan ' + p.userName)
    return p
player = login()
print(player)

        
"""
Jos loginSucceeded = True, niin silloin luodaan player-objekti
pelaajasta ja palautetaan returnilla luotu player-objekti.
"""

        
        