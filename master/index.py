import threading
import time
import os

mainFolder = ""
master = ""
port1=""
port2=""
timesync = ""


#Definindo as constantes do projeto que estão contidas dentro de "computers.spd", como a Pasta Shared por exemplo
computers = open('computers.spd')
for linha in computers:
    
    if '[FOLDER]' in linha:
        mainFolder =  computers.readline().rstrip( '\n' )
    elif '[MASTER]' in linha:
        master =  computers.readline().rstrip( '\n' )
    elif '[PORT1]' in linha:
        port1 =  computers.readline().rstrip( '\n' )
    elif '[PORT2]' in linha:
        port2 =  computers.readline().rstrip( '\n' )
    elif '[TIMESYNC]' in linha:
        timesync =  int(computers.readline().rstrip( '\n' ))/1000

computers.close()




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
            time.sleep(timesync)
            listFiles()
            os.remove('list.spd')

        elif FileNotFoundError:
            print('O arquivo list.spd não existe ou está sendo atualizado')
            print('Atualizando/ criando novo arquivo...')
            createFile = open('list.spd', 'w')
            createFile.close()
            listFiles()
            print('Arquivo atualizado/criado')


#Invocando a função que cria a pasta "shared"
createMainFolder()

#criando uma Thread e apontando o valor alvo para a função "listWatcher"
threading.Thread(target=listWatcher).start()



