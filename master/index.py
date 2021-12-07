import threading
import time
import os
import socket


#Constantes do projeto
mainFolder = ""
master = ""
port1=""
port2=""
timesync = ""


#Definindo os valores das constantes do projeto que estão contidas dentro de "computers.spd", comoo caminho da Pasta Shared, por exemplo.
computers = open('computers.spd')
for linha in computers:

    if '[FOLDER]' in linha:
        mainFolder =  computers.readline().rstrip('\n')
    elif '[MASTER]' in linha:
        master =  computers.readline().rstrip('\n')
    elif '[PORT1]' in linha:
        port1 =  computers.readline().rstrip('\n')
    elif '[PORT2]' in linha:
        port2 =  computers.readline().rstrip('\n')
    elif '[TIMESYNC]' in linha:
        timesync =  int(computers.readline().rstrip('\n'))/1000

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


#Função que verifica o aquivo "list.spd" e invoca a função de listagem dentro de si mesma
def listWatcher():
    num = 1
    while(num>0):

        if(os.path.exists('list.spd')):
            time.sleep(timesync)
            listFiles()
            os.remove('list.spd')

        elif FileNotFoundError:

            createFile = open('list.spd', 'w')
            createFile.close()
            listFiles()
            print('Arquivo "list.spd" atualizado ...')



#Invocando a função que cria a pasta "shared"
createMainFolder()





server  =  socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('localhost',3333))

#Iniciando a instância do socket server : 
    


def createServer():
    server.listen()
    connection, address =  server.accept()
    print("socket server em execução")
    fileName = connection.recv(1024).decode()
    
    with open (fileName, 'rb') as file : 
        for data in file.readlines():
            connection.send(data)
        print('arquivo enviado')


#criando uma Thread e apontando o valor alvo para as suas respectivas funções
threading.Thread(target=createServer).start()
threading.Thread(target=listWatcher).start()



