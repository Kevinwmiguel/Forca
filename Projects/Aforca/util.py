from random import choice
import os
from pygame import mixer
PS = 'CONTROL', 'SMARTPHONE', 'TELEVISION', 'ROBOT', 'COMPUTER', 'CABLE', 'ARTIFICIAL', 'INTELLIGENCE'


def palavra():
    p = choice(PS)
    return p


def header():
    print('\033[33m-=' * 15)
    print('Hangman game'.center(30))
    print('\033[33m-=\033[m' * 15)
    print('\033[32mTips: Technology \033[m')

def forca(x):
    num = x
    h = 'o'
    la = '/'
    ll = '/'
    rl = '\\'
    ra = '\\'
    b = '|'
    if num == 0:
        print(f'\033[31m-----┬\n'
              f'|\n'
              f'|\n'
              f'|\n'
              f'|\n'
              f'|\n\033[m')
        mixer.init()
        mixer.music.load('interface6.mp3')
        mixer.music.play()
    elif num == 1:
        print(f'\033[31m-----┬\n'
              f'|    {h}\n'
              f'|\n'
              f'|\n'
              f'|\n'
              f'|\n\033[m')
        mixer.init()
        mixer.music.load('interface6.mp3')
        mixer.music.play()
    elif num == 2:
        print(f'\033[31m-----┬\n'
              f'|    {h}\n'
              f'|    {b}\n'
              f'|\n'
              f'|\n'
              f'|\n\033[m')
        mixer.init()
        mixer.music.load('interface6.mp3')
        mixer.music.play()
    elif num == 3:
        print(f'\033[31m-----┬\n'
              f'|    {h}\n'
              f'|   {la}{b}\n'
              f'|\n'
              f'|\n'
              f'|\n\033[m')
        mixer.init()
        mixer.music.load('interface6.mp3')
        mixer.music.play()
    elif num == 4:
        print(f'\033[31m-----┬\n'
              f'|    {h}\n'
              f'|   {la}{b}{ra}\n'
              f'|\n'
              f'|\n'
              f'|\n\033[m')
        mixer.init()
        mixer.music.load('interface6.mp3')
        mixer.music.play()
    elif num == 5:
        print(f'\033[31m-----┬\n'
              f'|    {h}\n'
              f'|   {la}{b}{ra}\n'
              f'|   {ll}\n'
              f'|\n'
              f'|\n\033[m')
        mixer.init()
        mixer.music.load('interface6.mp3')
        mixer.music.play()
    elif num == 6:
        print(f'\033[31m-----┬\n'
              f'|    {h}\n'
              f'|   {la}{b}{ra}\n'
              f'|   {ll} {rl}\n'
              f'|\n'
              f'|\n\033[m')
        mixer.init()
        mixer.music.load('interface6.mp3')
        mixer.music.play()


def gamestart():
    p = palavra()
    listas = list('_' * len(p))
    e = 0
    pontos = 0
    letras_usadas = list()
    while True:
        header()
        forca(e)
        print(f'\033[33m{listas}\033[m')
        user = input('\033[33mType a letter: \033[m').strip().upper()
        if user in letras_usadas:
            print('\033[31mThe letter has already been used. Try another one\033[m')
            continue
        letras_usadas.append(user)
        if not user:
            print('\033[31mPlease, we dont accept void space\033[m')
            continue
        if user.isnumeric():
            print('\033[31mJust Letters!\033[m')
            continue
        if len(user) >= 2:
            print('\033[31mPlease just one letter \033[m')
            continue
        for c, v in enumerate(p):
            if v == user:
                print(f'The secret word has: {v}')
                listas[c] = user
                pontos = pontos + 1
        if user not in p:
            e = e + 1
        if pontos == len(p):
            forca(e)
            print('\033[32mGood one You Win!\033[m')
            mixer.init()
            mixer.music.load('WON.mp3')
            mixer.music.play()
            print(f'\033[32m{listas}\033[m')
            break

        if e == 6:
            forca(e)
            print('\033[31mYou lost!\033[m')
            print(f'The word was {p}')
            break
        os.system('cls')


os.system('cls')
