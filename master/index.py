import threading
import time
import os

mainFolder = "C:/shared"


# Função que lista os arquivos dentro da pasta "shared"
def listFiles():

    openList =  open('list.spd','w')

    for file in os.listdir(mainFolder):
        openList.write(file)
        openList.write('\n')

    openList.close()


# Função que cria a pasta "shared" se a mesma não existir
def createMainFolder():
    if not os.path.exists(mainFolder):
        os.mkdir(mainFolder)



#função que verifica o aquivo "list.spd" e invoca a função de listagem dentro de si mesma
def listWatcher():
    num = 1
    while(num>0):

        if(os.path.exists('list.spd')):
            time.sleep(10)
            listFiles()
            os.remove('list.spd')

        elif FileNotFoundError:
            print('O arquivo list.spd não existe ou foi excluído')
            print('Atualizando/ criando novo arquivo...')
            createFile = open('list.spd', 'w')
            createFile.close()
            listFiles()
            print('Arquivo atualizado/criado')


#Invocandoa  função que cria a pasta "shared"
createMainFolder()

#criando uma Thread e apontando o valor alvo para a função "listWatcher"
threading.Thread(target=listWatcher).start()
