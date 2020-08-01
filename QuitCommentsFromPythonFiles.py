#!/usr/bin/env python3
# -*- Encoding: UTF-8 -*- 
# extrae commentarios o codigo y crea otro archvo coon la informacion sin modificar el archivo original
# By: Jorge L. Herrera

from sys import argv
from colorama import Back, Fore
from time import strftime

ext = ( '.py' ,
        '.java',
        '.php',
        '.js',
        '.go',
        '.kt')  

isFileVal = lambda f: f[f.rindex('.'):] in ext
ARR = []
COM = []


banner = lambda : print(f"""{Fore.GREEN}{Back.RED}Usage: python ./thisScript.py ./file_with_comments.* \nquit all comments from source files just comments with\n
option 1:\t\tfor export write Usage: python ./thisScript.py [./file_with_comments.*] [-s] create a new file with not comments just source code 
option 2:\t\tfor export just comments Usage: python ./thisScript.py [./file_with_comments.*] [-c] create a new file with comments just source code

{Back.RESET}    PYTHON  : #
    JAVA, PHP, JS, GO, KOTLIN : //
{Fore.RESET}"""
)

def iactive():
    try:
        file = input('Write file name with extension:')
        if isFileVal(file):
            showContent(file)
        elif not isFileVal(file):
            print('Sorry Error NOTFOUNDEXTENSION')
            exit()
        else:
            print('Sorry Error NOTFOUNCOMAND')
            exit()
    except ValueError:
        print('Error in file name')

def showContent(f, m = 0):
    """ m = 0 : es para imprimir en pantalla 
        m = 1 : es para guardar en un array el cual mas adelante se guarda en un archivo
        m = 2 : almacena los commentarios
    """
    try :
        tmp = 'line'
        extension = f[f.rindex('.'):]
        simb = '//' if ext.index(extension) > 0 else '#'
        # readin file
        fileName = open(f, 'rt+')
        while tmp != '':
            tmp = fileName.readline()
            if simb in tmp:
                if m == 2:
                    COM.append(tmp[tmp.index(simb):])
                else:
                    tmp = tmp.replace(tmp[tmp.index(simb):], '\n', 1)
            if m == 0:
                print(tmp, end='') 
            elif m == 1:
                ARR.append(tmp)


        print(f'\n[*] NOTE: This script just remplacing comments inicialicing with by default \'{simb}\'')
        fileName.close()

    except FileNotFoundError:
        print('FileNotFound')

def writeContent(f): 
    
    timeline = strftime('%Y%b%a_%H%M%S') 
    fl, ex = f.split('.')
    try:
        fil = open(f'{fl}{timeline}.{ex}', 'wt+')
        showContent(f, 1)
        for i in ARR:
            fil.write(i)

        print(f'File {fil.name} writed')
        fil.close()
    except FileNotFoundError:

        print('FileNotFound')

def writeComments(f):
    try:
        fl, ex = f.split('.')
        file = open(f"{fl}{strftime('%Y%b%a_%H%M%S')}.{ex}", 'wt+')
        showContent(f, 2)
        for i in COM:
            file.write(i)
        print("[+] File Writed with comments")
        file.close()
    except FileNotFoundError:
        print('FileNotFound')
        
if __name__ == "__main__":

    if len(argv) < 2:
        banner()
        iactive()
    if len(argv) == 2:
        fl = argv[1]
        if isFileVal(fl):
            showContent(fl)
        else:
            banner()
    if len(argv) == 3:
        if argv[2] == '-s':
            writeContent(argv[1])
        elif argv[2] == '-c':
            writeComments(argv[1])
        else:
            banner()
    if len(argv) > 3:
        banner()