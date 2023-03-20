from tkinter import *
from tkinter import messagebox

login = Tk()
largura_monitor = login.winfo_screenwidth()/2
comprimento_monitor = login.winfo_screenheight()/2
comprimento = 300
largura = 200
usuario_var = StringVar()
senha_var = StringVar()
repetir_senha_var = StringVar()
email_var = StringVar()

def carregar():
    lista = []
    with open("cadastro.txt", "r") as arquivo:
        lista = arquivo.readlines()
    return lista

#Funcao que testa se o login e senha digitado coincidem com o banco de dados
def entrar_conta(usuario, senha):
    usuarios = carregar()
    for conta in usuarios:
        conta = conta.split("|")
        if conta[0] == usuario and conta[1] == senha:
            # LOGIN EXECUTADO COM SUCESSO =)
            messagebox.showinfo(title="PARABENS", message="LOGADO COM SUCESSO!!!!! =)")
            return 0
    messagebox.showinfo(title="ERRO", message="Senha e/ou usuario incorreto!\nOBS.: Letras maiusculas e minusculas sao diferentes!")

# Funcao que testa se a senha e repetir senha sao iguais
def checar_senhas_iguais():
    senha = senha_var.get()
    repetir_senha = repetir_senha_var.get()
    if senha == repetir_senha and senha != "":
        return True
    return False

# Funcao que gera as mensagens de erros baseado no tipo de erro cometido pelo usuario
def erros(erro):
    if erro == 'senhas iguais':
        messagebox.showinfo(title="ERRO", message="Senhas nao coincidem ou estao em branco!\nLembre-se que letras miusculas e minusculas sao diferentes\nDigite novamente!")

# Funcao que escreve no Banco de Dados o usuario cadastrado
def func_cadastro():
    with open("cadastro.txt", "a+") as arquivo:
        arquivo.write(f"{usuario_var.get()}|{senha_var.get()}|{email_var.get()} \n")

def tela_cadastro():
    # Config Cadastro
    cadastro = Toplevel(login)
    cadastro.title("Cadastro")
    cadastro.geometry(f"{comprimento+50}x{largura+50}+{int(largura_monitor-comprimento/2)+50}+{int(comprimento_monitor-largura/2)+50}")

    # Label
    Label(cadastro, text="Usuario           ", background="#fff", anchor=W).place(x=comprimento/5, y=largura/5)
    Label(cadastro, text="Senha              ", background="#fff", anchor=W).place(x=comprimento/5, y=largura/5+25)
    Label(cadastro, text="Repetir Senha  ", background="#fff", anchor=W).place(x=comprimento/5, y=largura/5+50)
    Label(cadastro, text="Email               ", background="#fff", anchor=W).place(x=comprimento/5, y=largura/5+75)

    # Input
    cadastro_usuario = Entry(cadastro, textvariable=usuario_var)
    cadastro_usuario.place(x=comprimento/5+80, y=largura/5)

    cadastro_senha = Entry(cadastro, show="*", textvariable=senha_var)
    cadastro_senha.place(x=comprimento/5+80, y=largura/5+25)

    repetir_cadastro_senha = Entry(cadastro, show="*", textvariable=repetir_senha_var)
    repetir_cadastro_senha.place(x=comprimento/5+80, y=largura/5+50)

    cadastro_email = Entry(cadastro, textvariable=email_var)
    cadastro_email.place(x=comprimento/5+80, y=largura/5+75)

    # Limpa os dados que estavam escritos
    def limpar_tela():
        cadastro_usuario.delete(0, END)
        cadastro_senha.delete(0, END)
        repetir_cadastro_senha.delete(0, END)
        cadastro_email.delete(0, END)

    # Botoes
    terminar_cadastro = Button(cadastro, text="Cadastrar", bd='3', command=lambda: [func_cadastro(), limpar_tela(), cadastro.destroy()] if checar_senhas_iguais() else [erros("senhas iguais"), repetir_cadastro_senha.delete(0, END)])
    terminar_cadastro.place(x=comprimento/5+80+60, y=largura/5+100)

    voltar_login = Button(cadastro, text="Voltar", bd='3', command=cadastro.destroy)
    voltar_login.place(x=comprimento/5, y=largura/5+100)

def tela_login():
    # Config Tela
    login.title("Login")
    login.geometry(f"{comprimento}x{largura}+{int(largura_monitor-comprimento/2)}+{int(comprimento_monitor-largura/2)}")

    # Eventos

    # Label
    Label(login, text="Usuario", background="#fff", anchor=W).place(x=comprimento/5, y=largura/5)
    Label(login, text="Senha  ", background="#fff", anchor=W).place(x=comprimento/5, y=largura/5+25)

    # Input
    usuario = Entry(login)
    usuario.place(x=comprimento/5+45, y=largura/5)

    senha = Entry(login, show="*")
    senha.place(x=comprimento/5+45, y=largura/5+25)

    # Botoes
    entrar = Button(login, text="Entrar", bd='3', command=lambda: [entrar_conta(usuario.get(), senha.get())] if True else False)
    entrar.place(x=comprimento/5+45+80, y=largura/5+50)

    cadastrar = Button(login, text="Cadastrar", bd='3', command=tela_cadastro)
    cadastrar.place(x=comprimento/5, y=largura/5+50)

    sair = Button(login, text="Sair", bd='3', command=login.destroy)
    sair.place(x=comprimento-35, y=largura-30)

    login.mainloop()

tela_login()