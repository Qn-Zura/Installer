#!/usr/bin/env python

from os import system as cans


print('''
┊┊╱▔▔▔▔╲┊▂▂╱▔▔╲┊┊
┊╱▔┈┈┈┈▕╱╋┳▏┈┈▔╲┊
╱▔┈╱▔▔▔▔╰━╯▔▔╲┈▔╲
╲▂╱┳▅┳╭┛┈┈┈┳▅┳╲▂╱
┊╭▏╰━╯╰━╯┈┳╰━╯▕╮┊
┊╰╲┈┈┈┈╰━━╯┈┈┈╱╯┊
┊┊┊▔▔▔▔▏▕▔▔▔▔▔┊┊┊''')

def main():
    print('[1].Tools Gabut\n[2].Tools Spam Sms\n[3].Tools endec [ python ]\n[4].About\n[5].Exit')
    while(True):
         try:
             zura = int(input('Pilih : '))
             if zura in ['1','01']:
                 gbt()
             elif zura in ['2','02']:
                 spm()
             elif zura in ['3','03']:
                 end()
             elif zura in ['4','04']:
                 abt()
             elif zura in ['5','05']:
                 ext()
         except Exception as lol:
               exit(lol)
               
def gbt():
    print('Prosess Install....')
    cans('pkg install git ruby;gem install lolcat; git clone https://github.com/MhankBarBar/GABUT ;cd GABUT;sh gbtz.sh')
def spm():
    print('Prosess Install....')
    cans('pkg install git python;pip install requests bs4;git clone https://github.com/MhankBarBar/spam ;cd spam;python spam.py')
def abt():
    print('''
    AUTHOR : QN-ZURA
    DATE : 11-03-2020
    TEAM : -
    ''')
    input('Tekan Enter Untuk Kembali')
    main()
def end():
    print('Prosess Install')
    cans('pkg install git python2;pip2 install uncompyle6;git clone https://github.com/MhankBarBar/endec ;cd endec; python2 endec.py')
def ext():
    print('Exit...\nGood Bay :*')
    exit()
  
  
if __name__ == '__main__':
    main()

