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
        self.totalQuestions = 0
        self.totalRightanswers = 0
        
        
class Question:
    def __init__(self, questionType, questionText, questionAnswer):
        self.questionType = questionType
        self.questionText = questionText
        self.questionAnswer = questionAnswer
        

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

"""Luo funktio createQuestions(), joka palauttaa listarakenteessa kymmenen
väittämää vastauksineen. Tee lista Class Question -objektin avulla. Generoinnin
jälkeen luo looppi, joka printtaa kaikki kysymykset.
"""
questions = []
def createQuestions():
    for i in range(1):
        questionType = input('Anna kysymyksen tyyppi: ')
        questionText = input('Anna kysymys: ')
        questionAnswer = input('Anna vastaus: ')
        questions.append(Question(questionType, questionText, questionAnswer))
          
createQuestions()

def newQuiz():
    print('Peli Alkaa!')
    answerCount = 0
    rightAnswerCount = 0
    for question in questions:
        player.totalQuestions += 1
        answer = input('Anna vastaus: ')
        if answer == question.questionAnswer:
            print('Oikein!')
            player.totalRightanswers += 1
        else:
            print('Väärin!')
        

newQuiz()
print(player.userName + ': Total questions: ' + str(player.totalQuestions))

'''Seuraavaksi kysy kolme kysymystä True/False -menetelmällä (t/f). Hyväksyttäviä arvoja
ovat vain pieni t ja f. Samaa logiikkaa vaaditaan vastatessa kysymyksiin. Tämä tarkoittaa
että tarkistaminen tehdään funktiolla, jota eri paikoista. Lisäksi, pelin loputtua kerro yksittäisen 
pelin kysymysten lukumäärä sekä oikeiden vastausten määrä. Pelaaja voi vastata myös ison T:n ja ison F:n
ja ne on hyväksyttävä
'''

        

    











     
        