import tkinter as tk
from tkinter import *
import tkinter
import tkinter as tk
import tkinter.ttk as tkk
import os
import BancoLogin
import sqlite3
from tkinter import messagebox
import random

usuariologado = []
usuariosaldo = []
usuariosenha =[]


def center(win):

    win.update_idletasks()

    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width

    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width

    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2

    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    win.deiconify()



def tela_login():



    def autenticar_login():

        vlogin = campo_usuario.get()
        vsenha = campo_senha.get()
        if vlogin == "" or vsenha =="" :
            campo_usuario.delete(0, "end")
            campo_senha.delete(0, "end")
            messagebox.showinfo(title="ERRO", message="Preencha todos os dados!")
            return

        usuariologado.append(vlogin)
        usuariosenha.append(vsenha)

        try:

            banco = sqlite3.connect('bancologin.db')
            cursor = banco.cursor()
            cursor.execute("SELECT senha FROM dadosLogin WHERE usuario ='{}'".format(vlogin))
            senha_bd = cursor.fetchall()
            cursor.execute("SELECT usuario FROM dadosLogin WHERE usuario ='{}'".format(vlogin))
            usuario_bd = cursor.fetchall()
            if vsenha != senha_bd[0][0]:
                messagebox.showinfo(title="ERRO", message="Senha incorreta!")
                return
            cursor.execute("SELECT saldo FROM dadosLogin WHERE usuario ='{}'".format(vlogin))
            saldo_bd = cursor.fetchall()
            saldo = saldo_bd[0][0]
            usuariosaldo.append(saldo)

            banco.close()
        except:
            messagebox.showerror(title="ERRO", message="Ddados Inválidos!")
            return


        if vsenha == senha_bd[0][0]:
            tela_principal(login_screen)
        else:
            return

    login_screen = tk.Tk()
    login_screen.geometry("400x600")
    login_screen.title("PigBank")
    login_screen.configure(bg="#c7d0d8")
    center(login_screen)

    cor_roxo = "#8c52ff"
    cor_cinza = "#c7d0d8"

    icon_pig = PhotoImage(file='imagens\\pig.png')
    login_screen.iconphoto(False, icon_pig)

    logo = tkinter.PhotoImage(file="imagens/pig.png")
    logo = logo.subsample(3, 3)
    figura1 = tk.Label(image=logo,bg="#c7d0d8")
    figura1.place(x=207, y=100, anchor=CENTER)

    # usuario
    texto_usuario = tk.Label(login_screen, text="USUARIO", relief="flat", bg=cor_cinza,font=("Helvetica 10 bold")).place(width=350, height=45, relx=0.5, y=215, anchor=CENTER)

    campo_usuario = tk.Entry(login_screen, borderwidth=0)
    campo_usuario.place(width=350, height=45, relx=.5, y=260, anchor=CENTER)

    # senha
    texto_senha = tk.Label(login_screen, text="SENHA", relief="flat", bg=cor_cinza, font=("Helvetica 10 bold")).place(width=350, height=45, relx=.5, y=305, anchor=CENTER)

    campo_senha = tk.Entry(login_screen, show="*", borderwidth=0)
    campo_senha.place(width=350, height=45, relx=.5, y=350, anchor=CENTER)

    # botão entrar
    botao_entrar = tk.Button(login_screen, text="ENTRAR", font=("Helvetica 12 bold"), bd=0, background=cor_roxo,
                             command=autenticar_login)
    botao_entrar.place(width=150, height=40, relx=.5, y=450, anchor=CENTER)

    # botao cadastro
    botao_cadastro = tk.Button(login_screen, text="CADASTRE-SE", font=("Helvetica 12 bold"), bd=0, background=cor_cinza,
                               command=lambda: tela_cadastro(login_screen))
    botao_cadastro.place(width=150, height=40, relx=.5, y=500, anchor=CENTER)

    login_screen.mainloop()


def tela_cadastro(tela_anterior):

    def cadastrofeito():
        return tela_login()

    def cadastar_usuario():

        if campo_nome_cadastro.get() or campo_usuario_cadastro.get() or campo_cpf_cadastro.get() or campo_data_cadastro.get() or campo_senha_cadastro.get()!= "":

            vnome = campo_nome_cadastro.get()
            vusuario = campo_usuario_cadastro.get()
            vcpf = campo_cpf_cadastro.get()
            vdataNascimento = campo_data_cadastro.get()
            vsenha = campo_senha_cadastro.get()
            vsaldo = str(random.randint(100,5000))


            vquery = "INSERT INTO dadosLogin(nome,usuario,cpf,dataNascimento,senha,saldo) VALUES('" + vnome + "','" + vusuario + "','" + vcpf + "','" + vdataNascimento + "','" + vsenha +"', '"+vsaldo+"')"
            BancoLogin.dml(vquery)
            campo_nome_cadastro.delete(0, "end")
            campo_usuario_cadastro.delete(0, "end")
            campo_cpf_cadastro.delete(0, "end")
            campo_data_cadastro.delete(0, "end")
            campo_senha_cadastro.delete(0, "end")
            messagebox.showinfo(title="CADASTRADO", message="Cadastrado com Sucesso!")
            tela_cadastro.destroy()
            cadastrofeito()



        else:
            messagebox.showinfo(title="ERRO", message="Todos os campos devem estar preenchidos!")

    cor_roxo = "#8c52ff"
    cor_cinza = "#c7d0d8"

    tela_anterior.destroy()
    tela_cadastro = tk.Tk()

    tela_cadastro.geometry("400x700")
    tela_cadastro.title("PigBank")
    tela_cadastro.configure(bg=cor_cinza)

    icon_pig = PhotoImage(file='imagens\\pig.png')
    tela_cadastro.iconphoto(False, icon_pig)
    center(tela_cadastro)

    # nome
    texto_nome_cadastro = tk.Label(tela_cadastro, text="NOME", relief="flat", bg=cor_cinza, font=("Helvetica 10 bold"))
    texto_nome_cadastro.place(x=25, y=115)

    campo_nome_cadastro = tk.Entry(tela_cadastro, borderwidth=0)
    campo_nome_cadastro.place(width=350, height=45, relx=.5, y=160, anchor=CENTER)

    # usuario
    texto_usuario_cadastro = tk.Label(tela_cadastro, text="USUÁRIO", relief="flat", bg=cor_cinza,font=("Helvetica 10 bold"))
    texto_usuario_cadastro.place(x=25, y=205)

    campo_usuario_cadastro = tk.Entry(tela_cadastro, borderwidth=0)
    campo_usuario_cadastro.place(width=350, height=45, relx=.5, y=250, anchor=CENTER)

    # cpf
    texto_cpf_cadastro = tk.Label(tela_cadastro, text="CPF", relief="flat", bg=cor_cinza, font=("Helvetica 10 bold"))
    texto_cpf_cadastro.place(x=25, y=295)

    campo_cpf_cadastro = tk.Entry(tela_cadastro, borderwidth=0)
    campo_cpf_cadastro.place(width=350, height=45, relx=.5, y=340, anchor=CENTER)

    # data de nascimento
    texto_data_cadastro = tk.Label(tela_cadastro, text="DATA DE NASCIMENTO", relief="flat", bg=cor_cinza,
                                   font=("Helvetica 10 bold"))
    texto_data_cadastro.place(x=25, y=385)

    campo_data_cadastro = tk.Entry(tela_cadastro, borderwidth=0)
    campo_data_cadastro.place(width=350, height=45, relx=.5, y=430, anchor=CENTER)

    # senha
    texto_senha_cadastro = tk.Label(tela_cadastro, text="SENHA", relief="flat", bg=cor_cinza,
                                    font=("Helvetica 10 bold"))
    texto_senha_cadastro.place(x=25, y=475)

    campo_senha_cadastro = tk.Entry(tela_cadastro, show="*", borderwidth=0)
    campo_senha_cadastro.place(width=350, height=45, relx=.5, y=515, anchor=CENTER)

    # botao cadastrar
    botao_cadastrar = tk.Button(tela_cadastro, text="CADASTRAR-SE", font=("Helvetica 12 bold"), bd=0,
                                background=cor_roxo,command=cadastar_usuario)
    botao_cadastrar.place(width=150, height=40, relx=.5, y=615, anchor=CENTER)

    tela_cadastro.mainloop()


def tela_principal(tela_anterior):


    usaldo = f'{usuariosaldo[0]:_.2f}'
    usaldo = usaldo.replace('.', ',').replace('_', '.')

    cor_roxo = "#8c52ff"
    cor_cinza = "#c7d0d8"

    tela_anterior.destroy()
    tela_principal = tk.Tk()

    icon_pig = PhotoImage(file='imagens/pig.png')
    tela_principal.iconphoto(False, icon_pig)

    tela_principal.geometry("400x630")
    tela_principal.title("PigBank")
    tela_principal.configure(background=cor_cinza)
    img_investimento = PhotoImage(file="imagens/botão_tela_principal.png")
    img_boleto = PhotoImage(file="imagens/botao_boleto.png")
    img_transf = PhotoImage(file="imagens/botao_transferencia.png")
    img_emprest = PhotoImage(file="imagens/botao_emprestimo.png")
    img_suporte = PhotoImage(file="imagens/botao_suporte.png")
    center(tela_principal)

    # linha
    linha = tk.Label(tela_principal, font=("Helvetica 12 bold"), text=f"SALDO:\nR$ {usuariosaldo[0]}", background=cor_roxo, height=3,width=180, justify="left").grid(row=1, column=0, padx=0, pady=0)
    # saldo
    texto_saldo = tk.Label(tela_principal, font=("Helvetica 12 bold"), text=f"SALDO\nR$ {usaldo}", background=cor_roxo, height=3,width=60, justify="left").place(x=0, y=5, width=100, height=50)

    # user
    #texto_user = tk.Label(tela_principal, font=("Helvetica 12 bold"), text=f"USUARIO\n {usuariologado[0]}", background=cor_roxo, height=3, justify="right").place(x=290, y=5, width=100, height=50)

    # botao emprestimo
    botao_emprestimo = tk.Button(tela_principal, font=("Helvetica 10 bold"), text="EMPRÉSTIMO", image=img_emprest,borderwidth=0, relief=FLAT,command=lambda: tela_emprestimo(tela_principal)).place(width=130, height=130, x=110, y=200, anchor=CENTER)

    # botao transferencia
    botao_transferencia = tk.Button(tela_principal, font=("Helvetica 10 bold"), text="TRANSFERÊNCIA", image=img_transf, borderwidth=0, relief=FLAT,command=lambda: tela_transferencia(tela_principal)).place(width=130, height=130, x=290, y=200, anchor=CENTER)

    # botao investimento
    botao_investimento = tk.Button(tela_principal, font=("Helvetica 10 bold"), text="INVESTIMENTO", image=img_investimento, borderwidth=0, relief=FLAT,command=lambda: tela_investimento1(tela_principal)).place(width=130, height=130,x=110, y=370, anchor=CENTER)

    # botao boleto
    botao_boleto = tk.Button(tela_principal, font=("Helvetica 10 bold"), text="BOLETO", image=img_boleto, borderwidth=0,relief=FLAT, command=lambda: tela_boleto(tela_principal)).place(width=130, height=130, x=290, y=370, anchor=CENTER)

    # botao suporte
    botao_suporte = tk.Button(tela_principal, font=("Helvetica 10 bold"), text="SUPORTE", image=img_suporte, borderwidth=0, relief=FLAT, command=lambda: tela_suporte(tela_principal)).place(width=130, height=130,x=200, y=540, anchor=CENTER)

    tela_principal.mainloop()

def tela_emprestimo(tela_anterior):

    def emprestimo1():

        vsaldoatual = int(usuariosaldo[0])
        vtransf = int(2500)
        vlogin = usuariologado[0]

        if vsaldoatual >= 500:

            banco = sqlite3.connect('bancologin.db')
            cursor = banco.cursor()
            cursor.execute("SELECT saldo FROM dadosLogin WHERE usuario ='{}'".format(vlogin))
            saldo_atual = cursor.fetchall()
            saldoatual = int(saldo_atual[0][0])
            newsaldo = saldoatual + vtransf
            banco.close()
            banco = sqlite3.connect('bancologin.db')
            cursor = banco.cursor()
            cursor.execute("UPDATE dadosLogin SET saldo ={} WHERE usuario ='{}'".format(newsaldo, vlogin))
            banco.commit()
            banco.close()
            usuariosaldo.pop(0)
            usuariosaldo.append(newsaldo)
            messagebox.showinfo(title="EMPRESTIMO", message="Emprestimo Aprovado!\nO valor já está na sua conta")
            banco.close()
        else:
            messagebox.showinfo(title="EMPRESTIMO", message="Infelizmente sua carta de credito não foi aprovada")
            return


    def emprestimo2():

        vsaldoatual = int(usuariosaldo[0])
        vtransf = int(5000)
        vlogin = usuariologado[0]

        if vsaldoatual >= 2000:
            banco = sqlite3.connect('bancologin.db')
            cursor = banco.cursor()
            cursor.execute("SELECT saldo FROM dadosLogin WHERE usuario ='{}'".format(vlogin))
            saldo_atual = cursor.fetchall()
            saldoatual = int(saldo_atual[0][0])
            newsaldo = saldoatual + vtransf
            banco.close()
            banco = sqlite3.connect('bancologin.db')
            cursor = banco.cursor()
            cursor.execute("UPDATE dadosLogin SET saldo ={} WHERE usuario ='{}'".format(newsaldo, vlogin))
            banco.commit()
            banco.close()
            usuariosaldo.pop(0)
            usuariosaldo.append(newsaldo)
            messagebox.showinfo(title="EMPRESTIMO", message="Emprestimo Aprovado!\nO valor já está na sua conta")
            banco.close()
        else:
            messagebox.showinfo(title="EMPRESTIMO", message="Infelizmente sua carta de credito não foi aprovada")
            return


    def emprestimo3():

        vsaldoatual = int(usuariosaldo[0])
        vtransf = int(10000)
        vlogin = usuariologado[0]

        if vsaldoatual >= 2000:
            banco = sqlite3.connect('bancologin.db')
            cursor = banco.cursor()
            cursor.execute("SELECT saldo FROM dadosLogin WHERE usuario ='{}'".format(vlogin))
            saldo_atual = cursor.fetchall()
            saldoatual = int(saldo_atual[0][0])
            newsaldo = saldoatual + vtransf
            banco.close()
            banco = sqlite3.connect('bancologin.db')
            cursor = banco.cursor()
            cursor.execute("UPDATE dadosLogin SET saldo ={} WHERE usuario ='{}'".format(newsaldo, vlogin))
            banco.commit()
            banco.close()
            usuariosaldo.pop(0)
            usuariosaldo.append(newsaldo)
            messagebox.showinfo(title="EMPRESTIMO", message="Emprestimo Aprovado!\nO valor já está na sua conta")
            banco.close()
        else:
            messagebox.showinfo(title="EMPRESTIMO", message="Infelizmente sua carta de credito não foi aprovada")
            return

    tela_anterior.destroy()
    tela_emprestimo = tk.Tk()

    cor_roxo = "#8c52ff"
    cor_cinza = "#c7d0d8"

    icon_pig = PhotoImage(file='imagens\\pig.png')
    tela_emprestimo.iconphoto(False, icon_pig)

    tela_emprestimo.geometry("400x600")
    tela_emprestimo.title("PigBank")
    tela_emprestimo.configure(background=cor_cinza)
    center(tela_emprestimo)

    #texto emprestimo
    texto_emprestimo = tk.Label(tela_emprestimo, font=("Helvetica 12 bold"), text="EMPRÉSTIMO", background=cor_roxo, height=3, justify="left").pack(fill='x')

    #texto selecione
    texto_selecione = tk.Label(tela_emprestimo, text="SELECIONE A QUANTIA DESEJADA:", relief="flat", bg=cor_cinza, font=("Helvetica 10 bold")).place(width=350, height=45, relx=0.5, y=125, anchor=CENTER)

    # 2500
    botao_2500 = tk.Button(tela_emprestimo, text="SOLICITAR R$ 2.500,00", font=("Helvetica 12 bold"), background=cor_roxo, relief=SOLID,command=emprestimo1)
    botao_2500.place(width=350, height=45, relx=.5, y=210, anchor=CENTER)

    # 5000
    botao_5000 = tk.Button(tela_emprestimo, text="SOLICITAR R$ 5.000,00", font=("Helvetica 12 bold"), background=cor_roxo, relief=SOLID,command=emprestimo2)
    botao_5000.place(width=350, height=45, relx=.5, y=300, anchor=CENTER)

    # 10000
    botao_10000 = tk.Button(tela_emprestimo, text="SOLICITAR R$ 10.000,00", font=("Helvetica 12 bold"), background=cor_roxo, relief=SOLID,command=emprestimo3)
    botao_10000.place(width=350, height=45, relx=.5, y=390, anchor=CENTER)

    # botao voltar ao menu principal
    botao_voltar = tk.Button(tela_emprestimo, text="VOLTAR AO MENU PRINCIPAL", font=("Helvetica 12 bold"), bd=0, background=cor_cinza, command=lambda: tela_principal(tela_emprestimo))
    botao_voltar.place(width=315, height=25, x=200, y=500, anchor=CENTER)

def tela_boleto(tela_anterior):

    def pagar_boleto():
        saldo = usuariosaldo[0]
        vlogin = usuariologado[0]
        vcodigo = campo_codigo.get()
        vdata =campo_data.get()



        banco = sqlite3.connect('bancologin.db')
        cursor = banco.cursor()
        cursor.execute("SELECT valorboleto FROM boletos WHERE codigo ='{}'".format(vcodigo))
        valor_boleto = cursor.fetchall()
        boleto = int(valor_boleto[0][0])
        if boleto > saldo:
            messagebox.showinfo(title="ERRO", message="Saldo insufuciente!")
            campo_codigo.delete(0, "end")
            campo_data.delete(0, "end")

            return
        newsaldo = saldo - boleto
        banco.close()
        banco = sqlite3.connect('bancologin.db')
        cursor = banco.cursor()
        cursor.execute("UPDATE dadosLogin SET saldo ={} WHERE usuario ='{}'".format(newsaldo, vlogin))
        banco.commit()
        banco.close()
        usuariosaldo.pop(0)
        usuariosaldo.append(newsaldo)
        messagebox.showinfo(title="BOLETO", message="Boleto pago com sucesso!")
        banco.close()

    tela_anterior.destroy()
    tela_boleto = tk.Tk()

    cor_roxo = "#8c52ff"
    cor_cinza = "#c7d0d8"

    icon_pig = PhotoImage(file='imagens\\pig.png')
    tela_boleto.iconphoto(False, icon_pig)

    tela_boleto.geometry("400x600")
    tela_boleto.title("PigBank")
    tela_boleto.configure(background=cor_cinza)
    center(tela_boleto)

    #texto boleto
    texto_boleto = tk.Label(tela_boleto, font=("Helvetica 12 bold"), text="PAGAR BOLETO", background=cor_roxo, height=3, justify="left").pack(fill='x')

    # codigo boleto
    texto_codigo = tk.Label(tela_boleto, text="CÓDIGO", relief="flat", bg=cor_cinza, font=("Helvetica 10 bold")).place(width=350, height=45, relx=0.5, y=165, anchor=CENTER)
    campo_codigo = tk.Entry(tela_boleto, borderwidth=0)
    campo_codigo.place(width=350, height=45, relx=.5, y=210, anchor=CENTER)

    # data pagamento
    texto_data = tk.Label(tela_boleto, text="DATA DO PAGAMENTO", relief="flat", bg=cor_cinza, font=("Helvetica 10 bold")).place(width=350, height=45, relx=.5, y=255, anchor=CENTER)
    campo_data = tk.Entry(tela_boleto, borderwidth=0)
    campo_data.place(width=350, height=45, relx=.5, y=300, anchor=CENTER)

    # botão pagar
    botao_pagar = tk.Button(tela_boleto, text="PAGAR", font=("Helvetica 12 bold"), background=cor_roxo, relief=SOLID,command=pagar_boleto)
    botao_pagar.place(width=200, height=50, relx=.5, y=450, anchor=CENTER)

    # botao voltar ao menu principal
    botao_voltar = tk.Button(tela_boleto, text="VOLTAR AO MENU PRINCIPAL", font=("Helvetica 12 bold"), bd=0, background=cor_cinza, command=lambda: tela_principal(tela_boleto))
    botao_voltar.place(width=315, height=25, x=200, y=500, anchor=CENTER)

def tela_transferencia(tela_anterior):

    def tranfermoney():


        vuser = campo_usuario_transf.get()
        vtransf = (campo_valor.get())

        vdata =campo_data.get()
        if vtransf == "" or vuser =="" :

            messagebox.showinfo(title="ERRO", message="Preencha todos os dados!")
            return
        intvtranf =int(vtransf)
        vlogin = usuariologado[0]

        banco = sqlite3.connect('bancologin.db')
        cursor = banco.cursor()
        cursor.execute("SELECT saldo FROM dadosLogin WHERE usuario ='{}'".format(vuser))
        saldo_receber = cursor.fetchall()
        cursor.execute("SELECT saldo FROM dadosLogin WHERE usuario ='{}'".format(vlogin))
        saldo_dar = cursor.fetchall()
        saldoatualreceber = int(saldo_receber[0][0])
        saldoatualdar = int(saldo_dar[0][0])
        if intvtranf > saldoatualdar:
            messagebox.showinfo(title="ERRO", message="Saldo insufuciente!")
            return
        newsaldoreceber = saldoatualreceber + intvtranf
        newsaldodar = saldoatualdar - intvtranf
        cursor.execute("SELECT usuario FROM dadosLogin WHERE usuario ='{}'".format(vuser))
        usuario_bd = cursor.fetchall()
        banco.close()

        print("Usuario que vai fazer a transferencia: {}\nSaldo Atual:{}".format(vlogin,saldoatualdar))
        print("Usuario que vai receber a transferencia: {}\nSaldo Atual:{}".format(vuser, saldoatualreceber))
        print("=======Após Transação=======")
        print("Usuário: {}\nSaldo Atual:{}".format(vlogin,newsaldodar))
        print("Usuário: {}\nSaldo Atual:{}".format(vuser, newsaldoreceber))


        if vuser == usuario_bd[0][0]:
            banco = sqlite3.connect('bancologin.db')
            cursor = banco.cursor()
            cursor.execute("UPDATE dadosLogin SET saldo ={} WHERE usuario ='{}'".format(newsaldoreceber, vuser))
            cursor.execute("UPDATE dadosLogin SET saldo ={} WHERE usuario ='{}'".format(newsaldodar, vlogin))
            banco.commit()
            banco.close()
            usuariosaldo.pop(0)
            usuariosaldo.append(newsaldodar)
            messagebox.showinfo(title="ERRO", message="Transferencia realizada com sucesso!")
            return tela_principal(tela_transferir)


        else:
            return False

    tela_anterior.destroy()
    tela_transferir = tk.Tk()

    cor_roxo = "#8c52ff"
    cor_cinza = "#c7d0d8"

    icon_pig = PhotoImage(file='imagens\\pig.png')
    tela_transferir.iconphoto(False, icon_pig)

    tela_transferir.geometry("400x600")
    tela_transferir.title("PigBank")
    tela_transferir.configure(background=cor_cinza)
    img_botao_transferir = PhotoImage(file="imagens/botao_transferir.png")
    img_voltar = PhotoImage(file="imagens/botao_voltar_menu.png")
    center(tela_transferir)

    #texto transferencia
    texto_transferencia = tk.Label(tela_transferir, font=("Helvetica 12 bold"), text="TRANSFERÊNCIA", background=cor_roxo, height=3, justify="left").pack(fill='x')

    # valor
    texto_valor = tk.Label(tela_transferir, text="VALOR", relief="flat", bg=cor_cinza, font=("Helvetica 10 bold")).place(width=350, height=45, relx=0.5, y=135, anchor=CENTER)
    campo_valor = tk.Entry(tela_transferir, borderwidth=0)
    campo_valor.place(width=350, height=45, relx=.5, y=180, anchor=CENTER)

    # data pagamento
    texto_data = tk.Label(tela_transferir, text="DATA DO PAGAMENTO", relief="flat", bg=cor_cinza, font=("Helvetica 10 bold")).place(width=350, height=45, relx=.5, y=225, anchor=CENTER)
    campo_data = tk.Entry(tela_transferir, borderwidth=0)
    campo_data.place(width=350, height=45, relx=.5, y=270, anchor=CENTER)

    #usuario
    texto_data = tk.Label(tela_transferir, text="USUARIO", relief="flat", bg=cor_cinza,font=("Helvetica 10 bold")).place(width=350, height=45, relx=.5, y=315, anchor=CENTER)
    campo_usuario_transf = tk.Entry(tela_transferir, borderwidth=0)
    campo_usuario_transf.place(width=350, height=45, relx=.5, y=360, anchor=CENTER)

    # botão transferir
    botao_transferir = tk.Button(tela_transferir, text="TRANSFERIR", font=("Helvetica 12 bold"), background=cor_roxo, relief=SOLID,command=tranfermoney)
    botao_transferir.place(width=200, height=50, relx=.5, y=450, anchor=CENTER)

    # botao voltar ao menu principal
    botao_voltar = tk.Button(tela_transferir, text="VOLTAR AO MENU PRINCIPAL", font=("Helvetica 12 bold"), bd=0, background=cor_cinza, command=lambda: tela_principal(tela_transferir))
    botao_voltar.place(width=315, height=25, x=200, y=500, anchor=CENTER)

def tela_investimento1(tela_anterior):

    usaldo = f'{usuariosaldo[0]:_.2f}'
    usaldo = usaldo.replace('.', ',').replace('_', '.')

    def investimento1():

        def inv1():

            vinvest = str(campo_valor_invest.get())
            vlogin = usuariologado[0]
            vsenha = usuariosenha[0]
            vsaldo = usuariosaldo[0]
            senha = campo_senha.get()
            if vinvest == '' or senha == '':
                messagebox.showerror(title="INVESTIMENTO",message="reencha todos os campos!")
                tela_inv1.destroy()
                return

            taxa = 0.1
            anos = 3
            vinvest = float(campo_valor_invest.get())
            if senha == vsenha and vsaldo >= 100:
                invest = vinvest * pow((1 + taxa), anos)
                print("Quantia a receber do investimento:{}".format(invest))
                newsaldo = vsaldo + invest

                banco = sqlite3.connect('bancologin.db')
                cursor = banco.cursor()
                cursor.execute("UPDATE dadosLogin SET saldo ={} WHERE usuario ='{}'".format(newsaldo, vlogin))
                banco.commit()
                banco.close()
                usuariosaldo.pop(0)
                usuariosaldo.append(newsaldo)
                messagebox.showinfo(title="INVESTIMENTO", message="O dinheiro foi aplidado!\n O valor já está na sua conta")
                banco.close()
                tela_inv1.destroy()
                return tela_investimento1
            else:
                messagebox.showinfo(title="INVESTIMENTO",
                                    message="Saldo insufuciente ou senha incorreta")
                tela_inv1.destroy()
                return tela_investimento1


        tela_inv1 = tk.Tk()
        cor_roxo = "#8c52ff"
        cor_cinza = "#c7d0d8"
        tela_inv1.geometry("400x600")
        tela_inv1.title("PigBank")
        tela_inv1.configure(background=cor_cinza)
        center(tela_inv1)

        # usuario
        texto_usuario = tk.Label(tela_inv1, text="VALOR DO INVESTIMENTO:", relief="flat", bg=cor_cinza,
                                 font=("Helvetica 10 bold")).place(width=350, height=45, relx=0.5, y=215, anchor=CENTER)

        campo_valor_invest = tk.Entry(tela_inv1, borderwidth=0)
        campo_valor_invest.place(width=350, height=45, relx=.5, y=260, anchor=CENTER)

        # senha
        texto_senha = tk.Label(tela_inv1, text="SENHA:", relief="flat", bg=cor_cinza,font=("Helvetica 10 bold")).place(width=350, height=45, relx=.5, y=305, anchor=CENTER)

        campo_senha = tk.Entry(tela_inv1, show="*", borderwidth=0)
        campo_senha.place(width=350, height=45, relx=.5, y=350, anchor=CENTER)

        # botão entrar
        botao_entrar = tk.Button(tela_inv1, text="INVESTIR", font=("Helvetica 12 bold"), bd=0, background=cor_roxo,command=inv1)
        botao_entrar.place(width=150, height=40, relx=.5, y=450, anchor=CENTER,)

        tela_inv1.mainloop()





    def investimento2():

        def inv2():

            vinvest = float(campo_valor_invest.get())
            vlogin = usuariologado[0]
            vsenha = usuariosenha[0]
            vsaldo = usuariosaldo[0]
            senha = campo_senha.get()
            taxa = 0.15
            anos = 8

            if vinvest == '' or senha == '':
                messagebox.showerror(title="INVESTIMENTO",message="reencha todos os campos!")
                tela_inv2.destroy()
                return

            if senha == vsenha and vsaldo >= 100:
                invest = vinvest * pow((1 + taxa), anos)
                print("Quantia a receber do investimento:{}".format(invest))
                newsaldo = vsaldo + invest
                banco = sqlite3.connect('bancologin.db')
                cursor = banco.cursor()
                cursor.execute("UPDATE dadosLogin SET saldo ={} WHERE usuario ='{}'".format(newsaldo, vlogin))
                banco.commit()
                banco.close()
                usuariosaldo.pop(0)
                usuariosaldo.append(newsaldo)
                messagebox.showinfo(title="INVESTIMENTO",
                                    message="O dinheiro foi aplidado!\n O valor já está na sua conta")
                banco.close()
                tela_inv2.destroy()
                return tela_investimento1
            else:
                messagebox.showinfo(title="INVESTIMENTO",
                                    message="Saldo insufuciente ou senha incorreta")
                tela_inv2.destroy()
                return tela_investimento1

        tela_inv2 = tk.Tk()
        cor_roxo = "#8c52ff"
        cor_cinza = "#c7d0d8"
        tela_inv2.geometry("400x600")
        tela_inv2.title("PigBank")
        tela_inv2.configure(background=cor_cinza)
        center(tela_inv2)

        # usuario
        texto_usuario = tk.Label(tela_inv2, text="VALOR DO INVESTIMENTO:", relief="flat", bg=cor_cinza,
                                 font=("Helvetica 10 bold")).place(width=350, height=45, relx=0.5, y=215, anchor=CENTER)

        campo_valor_invest = tk.Entry(tela_inv2, borderwidth=0)
        campo_valor_invest.place(width=350, height=45, relx=.5, y=260, anchor=CENTER)

        # senha
        texto_senha = tk.Label(tela_inv2, text="SENHA:", relief="flat", bg=cor_cinza, font=("Helvetica 10 bold")).place(
            width=350, height=45, relx=.5, y=305, anchor=CENTER)

        campo_senha = tk.Entry(tela_inv2, show="*", borderwidth=0)
        campo_senha.place(width=350, height=45, relx=.5, y=350, anchor=CENTER)

        # botão entrar
        botao_entrar = tk.Button(tela_inv2, text="INVESTIR", font=("Helvetica 12 bold"), bd=0, background=cor_roxo,
                                 command=inv2)
        botao_entrar.place(width=150, height=40, relx=.5, y=450, anchor=CENTER, )

        tela_inv2.mainloop()

    def investimento3():
        def inv3():

            vinvest = float(campo_valor_invest.get())
            vlogin = usuariologado[0]
            vsenha = usuariosenha[0]
            vsaldo = usuariosaldo[0]
            senha = campo_senha.get()
            taxa = 0.2
            anos = 13

            if vinvest == '' or senha == '':
                messagebox.showerror(title="INVESTIMENTO",message="reencha todos os campos!")
                tela_inv1.destroy()
                return

            if senha == vsenha and vsaldo >= 100:
                invest = vinvest * pow((1 + taxa), anos)
                print("Quantia a receber do investimento:{}".format(invest))
                newsaldo = vsaldo + invest
                banco = sqlite3.connect('bancologin.db')
                cursor = banco.cursor()
                cursor.execute("UPDATE dadosLogin SET saldo ={} WHERE usuario ='{}'".format(newsaldo, vlogin))
                banco.commit()
                banco.close()
                usuariosaldo.pop(0)
                usuariosaldo.append(newsaldo)
                messagebox.showinfo(title="INVESTIMENTO",
                                    message="O dinheiro foi aplidado!\n O valor já está na sua conta")
                banco.close()
                tela_inv1.destroy()
                return tela_investimento1
            else:
                messagebox.showinfo(title="INVESTIMENTO",
                                    message="Saldo insufuciente ou senha incorreta")
                tela_inv1.destroy()
                return tela_investimento1

        tela_inv1 = tk.Tk()
        cor_roxo = "#8c52ff"
        cor_cinza = "#c7d0d8"
        tela_inv1.geometry("400x600")
        tela_inv1.title("PigBank")
        tela_inv1.configure(background=cor_cinza)
        center(tela_inv1)

        # usuario
        texto_usuario = tk.Label(tela_inv1, text="VALOR DO INVESTIMENTO:", relief="flat", bg=cor_cinza,
                                 font=("Helvetica 10 bold")).place(width=350, height=45, relx=0.5, y=215, anchor=CENTER)

        campo_valor_invest = tk.Entry(tela_inv1, borderwidth=0)
        campo_valor_invest.place(width=350, height=45, relx=.5, y=260, anchor=CENTER)

        # senha
        texto_senha = tk.Label(tela_inv1, text="SENHA:", relief="flat", bg=cor_cinza, font=("Helvetica 10 bold")).place(
            width=350, height=45, relx=.5, y=305, anchor=CENTER)

        campo_senha = tk.Entry(tela_inv1, show="*", borderwidth=0)
        campo_senha.place(width=350, height=45, relx=.5, y=350, anchor=CENTER)

        # botão entrar
        botao_entrar = tk.Button(tela_inv1, text="INVESTIR", font=("Helvetica 12 bold"), bd=0, background=cor_roxo,
                                 command=inv3)
        botao_entrar.place(width=150, height=40, relx=.5, y=450, anchor=CENTER, )

    tela_anterior.destroy()
    tela_investimento1 = tk.Tk()

    cor_roxo = "#8c52ff"
    cor_cinza = "#c7d0d8"

    icon_pig = PhotoImage(file='imagens\\pig.png')
    tela_investimento1.iconphoto(False, icon_pig)

    tela_investimento1.geometry("400x600")
    tela_investimento1.title("PigBank")
    tela_investimento1.configure(background=cor_cinza)
    center(tela_investimento1)

    #texto investimento
    texto_investimento = tk.Label(tela_investimento1, font=("Helvetica 12 bold"), text="INVESTIMENTO", background=cor_roxo, height=3, justify="left").pack(fill='x')

    #texto saldo
    texto_saldo = tk.Label(tela_investimento1, font=("Helvetica 12 bold"), text=f"SALDO:\nR$ {usaldo}", background=cor_cinza, height=3, justify="left").place(x=25, y=75)

    #carteira porquinho
    texto_porquinho = tk.Label(tela_investimento1, font=("Helvetica 12 bold"), text="CARTEIRA PORQUINHO", background=cor_cinza, height=3, justify="left").place(x=25, y=125)
    texto_desc_porquinho = tk.Label(tela_investimento1, font=("Helvetica 8 bold"), text="Aplicação mínima: R$ 100,00\nVencimento: 18/09/2025\nRendimento: 10%a.a.", background=cor_cinza, height=3, justify="left").place(x=25, y=165)
    botao_porquinho = tk.Button(tela_investimento1, text="INVESTIR", font=("Helvetica 12 bold"), background=cor_roxo, relief=SOLID,command=investimento1)
    botao_porquinho.place(x=320, y=175, anchor=CENTER)

    #carteira porco
    texto_porco = tk.Label(tela_investimento1, font=("Helvetica 12 bold"), text="CARTEIRA PORCO", background=cor_cinza, height=3, justify="left").place(x=25, y=215)
    texto_desc_porco = tk.Label(tela_investimento1, font=("Helvetica 8 bold"), text="Aplicação mínima: R$ 500,00\nVencimento: 23/05/2030\nRendimento: 15%a.a.", background=cor_cinza, height=3, justify="left").place(x=25, y=255)
    botao_porco = tk.Button(tela_investimento1, text="INVESTIR", font=("Helvetica 12 bold"), background=cor_roxo, relief=SOLID,command=investimento2)
    botao_porco.place(x=320, y=265, anchor=CENTER)

    # carteira porcao
    texto_porcao = tk.Label(tela_investimento1, font=("Helvetica 12 bold"), text="CARTEIRA PORCÃO", background=cor_cinza, height=3, justify="left").place(x=25, y=305)
    texto_desc_porcao = tk.Label(tela_investimento1, font=("Helvetica 8 bold"), text="Aplicação mínima: R$ 1.000,00\nVencimento: 24/01/2035\nRendimento: 20%a.a.", background=cor_cinza, height=3, justify="left").place(x=25, y=345)
    botao_porcao = tk.Button(tela_investimento1, text="INVESTIR", font=("Helvetica 12 bold"), background=cor_roxo, relief=SOLID,command=investimento3)
    botao_porcao.place(x=320, y=355, anchor=CENTER)

    # botao voltar ao menu principal
    botao_voltar = tk.Button(tela_investimento1, text="VOLTAR AO MENU PRINCIPAL", font=("Helvetica 12 bold"), bd=0, background=cor_cinza, command=lambda: tela_principal(tela_investimento1))
    botao_voltar.place(width=315, height=25, x=200, y=500, anchor=CENTER)

def tela_suporte(tela_anterior):
    tela_anterior.destroy()
    tela_suporte = tk.Tk()

    cor_roxo = "#8c52ff"
    cor_cinza = "#c7d0d8"

    icon_pig = PhotoImage(file='imagens\\pig.png')
    tela_suporte.iconphoto(False, icon_pig)

    tela_suporte.geometry("400x600")
    tela_suporte.title("PigBank")
    tela_suporte.configure(background=cor_cinza)
    center(tela_suporte)

    # texto suporte
    texto_suporte = tk.Label(tela_suporte, font=("Helvetica 12 bold"), text="SUPORTE", background=cor_roxo, height=3, justify="left").pack(fill='x')

    # botao pergunta 1
    texto_pergunta1 = tk.Button(tela_suporte, font=("Helvetica 10 bold"), text="Como funciona o empréstimo no PigBank?", background=cor_cinza, height=3, justify="left", command=lambda: tela_suporteP1(tela_suporte)).place(width=340, height=75, x=25, y=125)

    # botao pergunta 2
    texto_pergunta2 = tk.Button(tela_suporte, font=("Helvetica 10 bold"), text="Como funciona o investimento no PigBank?", background=cor_cinza, height=3, justify="left", command=lambda: tela_suporteP2(tela_suporte)).place(width=340, height=75, x=25, y=210)

    # botao pergunta 3
    texto_pergunta3 = tk.Button(tela_suporte, font=("Helvetica 10 bold"), text="Quem desenvolveu o PigBank?", background=cor_cinza, height=3, justify="left", command=lambda: tela_suporteP3(tela_suporte)).place(width=340, height=75, x=25, y=295)

    # botao voltar ao menu principal
    botao_voltar = tk.Button(tela_suporte, text="VOLTAR AO MENU PRINCIPAL", font=("Helvetica 12 bold"), bd=0, background=cor_cinza, command=lambda: tela_principal(tela_suporte))
    botao_voltar.place(width=315, height=25, x=200, y=500, anchor=CENTER)

def tela_suporteP1(tela_anterior):
    tela_anterior.destroy()
    tela_suporteP1 = tk.Tk()

    cor_roxo = "#8c52ff"
    cor_cinza = "#c7d0d8"

    icon_pig = PhotoImage(file='imagens\\pig.png')
    tela_suporteP1.iconphoto(False, icon_pig)

    tela_suporteP1.geometry("400x600")
    tela_suporteP1.title("PigBank")
    tela_suporteP1.configure(background=cor_cinza)
    center(tela_suporteP1)

    # texto suporte p1
    texto_suporteP2 = tk.Label(tela_suporteP1, font=("Helvetica 12 bold"), text="SUPORTE - Pergunta 1",
                                  background=cor_roxo, height=3, justify="left").pack(fill='x')
    text1 = "Como funciona o empréstimo no PigBank?"
    banco = sqlite3.connect('bancologin.db')
    cursor = banco.cursor()
    cursor.execute("SELECT resposta FROM suporte WHERE pergunta ='{}'".format(text1))
    resp = cursor.fetchall()
    resposta = resp[0][0]

    #pergunta 1
    texto_p1 = tk.Label(tela_suporteP1, font=("Helvetica 12 bold"), text=f"{text1}",background=cor_cinza, height=3, justify="left").place(x=25, y=75)
    texto_r1 = tk.Label(tela_suporteP1, font=("Helvetica 8 bold"),text=f"{resposta}",background=cor_cinza, height=3, justify="left").place(x=25, y=125)

   # botao voltar ao suporte
    botao_voltar = tk.Button(tela_suporteP1, text="VOLTAR", font=("Helvetica 12 bold"), bd=0,
                             background=cor_cinza, command=lambda: tela_suporte(tela_suporteP1))
    botao_voltar.place(width=315, height=25, x=200, y=500, anchor=CENTER)

def tela_suporteP2(tela_anterior):
    tela_anterior.destroy()
    tela_suporteP2 = tk.Tk()

    cor_roxo = "#8c52ff"
    cor_cinza = "#c7d0d8"

    icon_pig = PhotoImage(file='imagens\\pig.png')
    tela_suporteP2.iconphoto(False, icon_pig)

    tela_suporteP2.geometry("400x600")
    tela_suporteP2.title("PigBank")
    tela_suporteP2.configure(background=cor_cinza)
    center(tela_suporteP2)

    # texto suporte p2
    texto_suporteP2 = tk.Label(tela_suporteP2, font=("Helvetica 12 bold"), text="SUPORTE - Pergunta 2",
                                  background=cor_roxo, height=3, justify="left").pack(fill='x')

    # pergunta 2
    texto_p2 = tk.Label(tela_suporteP2, font=("Helvetica 12 bold"), text="Como funciona o investimento no PigBank?",
                               background=cor_cinza, height=3, justify="left").place(x=25, y=75)
    texto_r2 = tk.Label(tela_suporteP2, font=("Helvetica 8 bold"),
                                    text="Aplicação mínima: R$ 100,00\nVencimento: 18/09/2025\nRendimento: 10%a.a.",
                                    background=cor_cinza, height=3, justify="left").place(x=25, y=125)

   # botao voltar ao suporte
    botao_voltar = tk.Button(tela_suporteP2, text="VOLTAR", font=("Helvetica 12 bold"), bd=0,
                             background=cor_cinza, command=lambda: tela_suporte(tela_suporteP2))
    botao_voltar.place(width=315, height=25, x=200, y=500, anchor=CENTER)

def tela_suporteP3(tela_anterior):
    tela_anterior.destroy()
    tela_suporteP3 = tk.Tk()

    cor_roxo = "#8c52ff"
    cor_cinza = "#c7d0d8"

    icon_pig = PhotoImage(file='imagens\\pig.png')
    tela_suporteP3.iconphoto(False, icon_pig)

    tela_suporteP3.geometry("400x600")
    tela_suporteP3.title("PigBank")
    tela_suporteP3.configure(background=cor_cinza)
    center(tela_suporteP3)

    # texto suporte p3
    texto_suporteP3 = tk.Label(tela_suporteP3, font=("Helvetica 12 bold"), text="SUPORTE - Pergunta 3",
                                  background=cor_roxo, height=3, justify="left").pack(fill='x')

    # pergunta 3
    texto_p3 = tk.Label(tela_suporteP3, font=("Helvetica 12 bold"), text="Quem desenvolveu o PigBank?",background=cor_cinza, height=3, justify="left").place(x=25, y=75)
    texto_r3 = tk.Label(tela_suporteP3, font=("Helvetica 8 bold"),text="    Com o objetivo de desenvolver um projeto para o Seminário\n da disciplina Modelagem e Projeto de Sistemas, um grupo de\n alunos da Universidade do Estado do Amazonas formado por:\n- Adriano Nobre Vieira Guimarães;\n- Geovani Lopes Sampaio;\n- Gustavo Pacífico S. S. Chaves;\n- José Augusto de Almeida Neto.  ",background=cor_cinza, justify="left").place(x=25, y=125)
    # botao voltar ao suporte
    botao_voltar = tk.Button(tela_suporteP3, text="VOLTAR", font=("Helvetica 12 bold"), bd=0,
                             background=cor_cinza, command=lambda: tela_suporte(tela_suporteP3))
    botao_voltar.place(width=315, height=25, x=200, y=500, anchor=CENTER)



tela_login()