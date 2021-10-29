from os import path
import threading
from threading import Timer
import time
import os.path
from pathlib import Path



listSpd = "list.spd"
pathToFolder = "/spd/"

# folder = Path(pathToFolder+listSpd)
folder =  'list.spd'



def listWatcher():
    num = 1
    while(num>0):

        if(os.path.exists('list.spd')):
            time.sleep(2)
            print(listSpd)

        elif FileNotFoundError:
            time.sleep(2)
            print('O arquivo list.spd não existe')
            print('Criando novo arquivo...')
            createFile = open('list.spd', 'w')
            createFile.close()


# threading.Thread(target=listWatcher).start()

listWatcher()






    







    