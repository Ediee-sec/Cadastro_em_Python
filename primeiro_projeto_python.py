from time import strftime, localtime
from datetime import datetime
import random

try:
    nome_funcionario = str(input("Digite o seu Nome e Sobrenome: "))
    array_funcionarios = [nome_funcionario]
except:
    print("Error: Apenas Letras é permitido")


# Esta função armazena a data de nascimento do úsuario e faz o calculo para determinar a sua idade.
def idade_aniversario_func():

    data_aniversario_funcionario = datetime.strptime(
        input("Infome a sua data de nascimento: "), '%d/%m/%Y')
    idade_funcionario = datetime.today() - data_aniversario_funcionario
    global resultado_idade_funcionario
    resultado_idade_funcionario = float(
        "%.1f" % float(idade_funcionario.days / 365))


idade_aniversario_func()


# Esta função faz o cadastro do úsuario no sistema, com login e senha, verificando se os campos possuem strings ou inteiros
def cadastro_no_sistema():
    global login_usuario
    global senha_usuario
    login_usuario = ''
    senha_usuario = ''
    while login_usuario is senha_usuario == '':
        login_usuario = input("Escolha o Nickname: ")

        while True:
            try:
                senha_usuario = int(
                    input("Escolha uma senha [Apenas números]: "))
                break
            except ValueError:
                print("Error: 001 (Sua senha deve possuir apenas números)")
                continue

        if login_usuario and senha_usuario != '':
            print("Cadastro de úsuario realizado com sucesso")
        elif login_usuario or senha_usuario == '':
            print("\nErro ao cadastar login, Tente novamente\n")


cadastro_no_sistema()


# Função para uma futura altualização do sistema, não deixará que tenha mais de 2 nicknames iguais no sistema
def verificacao_nickname_duplo():
    login_duplicado = [login_usuario]
    set_login = set(login_duplicado)

    set_login.add(login_usuario)
    # print(set_login)


verificacao_nickname_duplo()


# Função para armazenar a data de registro do funcionário + sortear um crachá aleatório + sortear um turno baseado na função idade_aniversario_func()
def data_registro_cracha_turno():
    global data_registro
    global cracha_aleatorio

    data_registro = strftime("%d %b %Y", localtime())
    cracha_aleatorio = random.randint(1, 9999)
    turno_aleatorio = ["Diurno | 08:00 ás 15:00", "Noturno | 19:00 ás 02:00 "]
    cadastro_finalizado = (
        f'Olá {nome_funcionario}, o seu registro foi concluido com SUCESSO no dia {data_registro}, O seu número de crachá virtual foi gerado : {cracha_aleatorio}')

    print(cadastro_finalizado)

    if resultado_idade_funcionario <= 21:
        print("Você Irá trabalhar como Estagiario")
    elif resultado_idade_funcionario >= 22:
        print("Você irá trabalhar como Operador I")

    if resultado_idade_funcionario >= 22 and cracha_aleatorio >= 5000:
        print(random.choice(turno_aleatorio))
    else:
        print("Horário = 8:00 ás 15:00")


data_registro_cracha_turno()


# Função para logar o usuario no sistema, verifica se o login e senha são os mesmos do cadastro
def login_sistema():

    while True:

        print("\nLogin no Sistema")
        nome = input("Digite aqui seu login: ")

        while True:
            try:
                senha = int(
                    input("Digite aqui a sua senha: "))
                break
            except ValueError:
                print("Error: 001 (Sua senha deve possuir apenas números)")
                continue

        if nome == login_usuario:
            if senha == senha_usuario:
                print("Login Realizado com sucesso")
                break
            else:
                print("Houve um problema, porfavor tente novamente!")
                continue
        else:
            print("Houve um problema, porfavor tente novamente!")
            continue


login_sistema()


# informações pessoais do funcionario
def painel_sistema():
    print(f'\nBem Vindo ao sistema interno {login_usuario}')
    print(f'\nNome: {nome_funcionario}')
    print(f'idade: {resultado_idade_funcionario}')
    print(f'Crachá Virtual: {cracha_aleatorio}')
    print(f'Data de contratação: {data_registro}')


painel_sistema()


# Dicionario com informações do funcionario
def dicionario_do_funcionario():
    dicionario = dict(nome=nome_funcionario,
                      idade=resultado_idade_funcionario, login=login_usuario)
    # print(dicionario)


dicionario_do_funcionario()
