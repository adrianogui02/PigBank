import sqlite3
from sqlite3 import Error
import os


pastaApp=os.path.dirname(__file__)
nomeBanco=pastaApp+"\\bancologin.db"



conexao = sqlite3.connect('bancologin.db')
# Criando o cursor:
c = conexao.cursor()

# Criando a tabela:

#c.execute("""CREATE TABLE  dadosLogin (
#      nome text,
#      usuario text,
#      cpf text,
#      dataNascimento text,
#      senha text
#      )""")

#Commit as mudanças:
conexao.commit()

#Fechar o banco de dados:
conexao.close()



def ConexaoBanco():
    con=None
    try:
        con=sqlite3.connect(nomeBanco)
    except Error as ex:
        print(ex)
    return con

def dql(query):
    vcon=ConexaoBanco()
    c=vcon.cursor()
    c.execute(query)
    res=c.fetchall()
    vcon.close()
    return res

def dml(query):
    try:
        vcon = ConexaoBanco()
        c = vcon.cursor()
        c.execute(query)
        vcon.commit()
        vcon.close()
    except Error as ex:
        print(ex)


