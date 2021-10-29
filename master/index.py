import threading
import time
import os

mainFolder = "C:/shared"

def createMainFolder():
    if not os.path.exists(mainFolder):
        os.mkdir(mainFolder)

def listWatcher():
    num = 1
    while(num>0):

        if(os.path.exists('list.spd')):
            time.sleep(2)
            print('Aguardando mudanças...')

        elif FileNotFoundError:
            time.sleep(2)
            print('O arquivo list.spd não existe ou foi excluído')
            print('Criando novo arquivo...')
            createFile = open('list.spd', 'w')
            createFile.close()
            print('Arquivo criado')


createMainFolder()
threading.Thread(target=listWatcher).start()
