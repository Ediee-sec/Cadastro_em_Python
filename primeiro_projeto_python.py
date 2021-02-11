# %%
from time import strftime, localtime
from datetime import datetime
import logging
import random

logging.basicConfig(level=logging.DEBUG, filename='registro.log',
                    filemode='a', format='%(levelname)s - %(message)s - %(asctime)s')


class info_colab:
    def __init__(self):
        self.nome_funcionario = ''
        self.login_usuario = ''
        self.senha_usuario = ''


detalhes_func = info_colab()

detalhes_func.nome_funcionario = input("Digite o seu Nome e Sobrenome: ")
array_funcionarios = [detalhes_func.nome_funcionario]


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
    while detalhes_func.login_usuario is detalhes_func.senha_usuario == '':
        detalhes_func.login_usuario = input("Escolha o Nickname: ")

        while True:
            try:
                senha_usuario = int(
                    input("Escolha uma senha [Apenas números]: "))
                break
            except ValueError as error:
                print("Error: 001 (Sua senha deve possuir apenas números)")
                logging.warning(error)
                continue

        if detalhes_func.login_usuario and senha_usuario != '':
            print("Cadastro de úsuario realizado com sucesso")
            logging.info(
                f'O Funcionário {detalhes_func.nome_funcionario}, cadastou seu login e senha com sucesso')
        elif detalhes_func.login_usuario or senha_usuario == '':
            print("\nErro ao cadastar login, Tente novamente\n")
            logging.info(
                f'O Funcionário {detalhes_func.nome_funcionario}, Errou ao tentar se cadastrar no sistema')


cadastro_no_sistema()


# Função para uma futura altualização do sistema, não deixará que tenha mais de 2 nicknames iguais no sistema
def verificacao_nickname_duplo():
    login_duplicado = [detalhes_func.login_usuario]
    set_login = set(login_duplicado)

    set_login.add(detalhes_func.login_usuario)
    # print(set_login)


verificacao_nickname_duplo()


# Função para armazenar a data de registro do funcionário + sortear um crachá aleatório + sortear um turno baseado na função idade_aniversario_func()
def data_registro_cracha_turno():
    global data_registro
    global cracha_aleatorio

    data_registro = strftime("%d %b %Y", localtime())
    cracha_aleatorio = random.randint(1, 9999)
    logging.info(
        f'O crachá do funcionário {detalhes_func.nome_funcionario} foi gerado com sucesso - {cracha_aleatorio}')
    turno_aleatorio = ["Diurno | 08:00 ás 15:00", "Noturno | 19:00 ás 02:00 "]
    cadastro_finalizado = (
        f'\nOlá {detalhes_func.nome_funcionario}, o seu registro foi concluido com SUCESSO no dia {data_registro}, O seu número de crachá virtual foi gerado : {cracha_aleatorio}')

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
            except ValueError as error:
                print("Error: 001 (Sua senha deve possuir apenas números)")
                logging.warning(error)
                continue

        if nome == detalhes_func.login_usuario:
            if senha == detalhes_func.senha_usuario:
                print("Login Realizado com sucesso")
                logging.info(
                    f'O funcionario {detalhes_func.nome_funcionario} de username {detalhes_func.login_usuario}, entrou com sucesso no sistema')
                break
            else:
                print("Houve um problema, porfavor tente novamente!")
                logging.info(
                    f'O funcionario {detalhes_func.nome_funcionario} de username {detalhes_func.login_usuario}, Errou a combnação correta para entrar no sistema')
                continue
        else:
            print("Houve um problema, porfavor tente novamente!")
            continue


login_sistema()


# informações pessoais do funcionario
def painel_sistema():
    print(f'\nBem Vindo ao sistema interno {detalhes_func.login_usuario}')
    print(f'\nNome: {detalhes_func.nome_funcionario}')
    print(f'idade: {resultado_idade_funcionario}')
    print(f'Crachá Virtual: {cracha_aleatorio}')
    print(f'Data de contratação: {data_registro}')


painel_sistema()


# Dicionario com informações do funcionario
def dicionario_do_funcionario():
    dicionario = dict(nome=detalhes_func.nome_funcionario,
                      idade=resultado_idade_funcionario, login=detalhes_func.login_usuario)
    # print(dicionario)


dicionario_do_funcionario()

# %%
