import threading
import time
import os.path





def listWatcher():
    num = 1
    while(num>0):

        if(os.path.exists('src/list.spd')):
            time.sleep(2)
            print('list.spd')

        elif FileNotFoundError:
            time.sleep(2)
            print('O arquivo list.spd não existe')
            print('Criando novo arquivo...')
            createFile = open('src/list.spd', 'w')
            createFile.close()
            print('Arquivo criado')


threading.Thread(target=listWatcher).start()

    







    