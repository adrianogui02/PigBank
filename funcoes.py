import sqlite3
import time
from sqlite3 import Error
import os
import BancoLogin
import main


def cadastar_usuario():



    vnome = main.campo_nome_cadastro.get()
    vusuario = main.campo_usuario_cadastro.get()
    vcpf = main.campo_cpf_cadastro.get()
    vdataNascimento = main.campo_data_cadastro.get()
    vsenha = main.campo_senha_cadastro.get()

    vquery = "INSERT INTO dadosLogin(nome,usuario,cpf,dataNascimento,senha) VALUES('" + vnome + "','" + vusuario + "','" + vcpf + "','" + vdataNascimento + "','" + vsenha + "')"
    BancoLogin.dml(vquery)
    print("Usuario Cadastrado")


def autenticar_login():

    vlogin = main.campo_usuario.get()
    vsenha = main.campo_senha.get()


    banco = sqlite3.connect('bancologin.db')
    cursor = banco.cursor()
    cursor.execute("SELECT senha FROM dadosLogin WHERE usuario ='{}'".format(vlogin))
    senha_bd = cursor.fetchall()
    cursor.execute("SELECT usuario FROM dadosLogin WHERE usuario ='{}'".format(vlogin))
    usuario_bd =cursor.fetchall()
    banco.close()

    if vlogin != usuario_bd[0][0]:
        print("Usuário Não encontrado!")
        time.sleep(2)

        print("Voltando ao Login...")
        time.sleep(3)

        return autenticar_login()

    elif vsenha != senha_bd[0][0]:
        print("Dados Incorretos!")
        time.sleep(2)

        print("Voltando ao Login...")
        time.sleep(3)

        return autenticar_login()

    elif vsenha == senha_bd[0][0]:
        print("====LOGIN EFETUADO COM SUCESSO====")
    else:
        print("AQUI NAO ACONTECE POHA NENHUMA")

def tranfermoney():

    print("===TRANSFERENCIA===\nPreencha os dados para transferir!")
    vuser = input("Digite o User: ")
    vtransf = int(input("Digite o valor: R$  "))
    vsenha = input("Digite sua senha:")

    banco = sqlite3.connect('bancologin.db')
    cursor = banco.cursor()
    cursor.execute("SELECT senha FROM dadosLogin WHERE usuario ='{}'".format(vuser))
    senha_bd = cursor.fetchall()
    cursor.execute("SELECT saldo FROM dadosLogin WHERE usuario ='{}'".format(vuser))
    saldo_bd = cursor.fetchall()
    saldoatual = saldo_bd[0][0]
    newsaldo = saldoatual + vtransf
    cursor.execute("SELECT usuario FROM dadosLogin WHERE usuario ='{}'".format(vuser))
    usuario_bd = cursor.fetchall()
    banco.close()
    print(saldoatual)
    print(newsaldo)
    if vuser != usuario_bd[0][0]:
        print("Usuário Não encontrado!")
        time.sleep(2)

        print("Voltando ao Login...")
        time.sleep(3)

        return autenticar_login()

    elif vsenha != senha_bd[0][0]:
        print("Dados Incorretos!")
        time.sleep(2)

        print("Voltando ao Login...")
        time.sleep(3)

        return autenticar_login()

    elif vsenha == senha_bd[0][0]:
        banco = sqlite3.connect('bancologin.db')
        cursor = banco.cursor()
        cursor.execute("UPDATE dadosLogin SET saldo ={} WHERE usuario ='{}'".format(newsaldo, vuser))
        banco.commit()
        banco.close()
        print("Transferindo...")
        time.sleep(4)
        print("Trenferencia realizada com sucesso!")

    else:
        print("AQUI NAO ACONTECE POHA NENHUMA")



