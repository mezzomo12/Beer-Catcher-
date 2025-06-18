import os, time, sys, random
from datetime import datetime
import os, time, sys, random, json

def limpar():
    os.system("cls")

def esperar(segundos):
    time.sleep(segundos)

def inicializarBancoDeDados():
    try:
        banco = open("data.jogo","r")
    except:
        print("Banco de Dados Inexistente. Criando...")
        banco = open("data.jogo","w")

def escreverDados(nome, pontos):
    # INI - inserindo no arquivo
    banco = open("data.jogo","r")
    dados = banco.read()
    banco.close()
    if dados != "":
        dadosDict = json.loads(dados)
    else:
        dadosDict = {}
        
    data_br = datetime.now().strftime("%d/%m/%Y")
    dadosDict[nome] = (pontos, data_br)
    
    banco = open("data.jogo","w")
    banco.write(json.dumps(dadosDict))
    def limpar():
        os.system("cls")

    def esperar(segundos):
        time.sleep(segundos)

    def inicializarBancoDeDados():
        try:
            banco = open("data.jogo","r")
        except:
            print("Banco de Dados Inexistente. Criando...")
            banco = open("data.jogo","w")

    def escreverDados(nome, pontos):
        # INI - inserindo no arquivo
        banco = open("data.jogo","r")
        dados = banco.read()
        banco.close()
        if dados != "":
            dadosDict = json.loads(dados)
        else:
            dadosDict = {}
            
        data_br = datetime.now().strftime("%d/%m/%Y")
        dadosDict[nome] = (pontos, data_br)
        
        banco = open("data.jogo","w")
        banco.write(json.dumps(dadosDict))
        banco.close()


