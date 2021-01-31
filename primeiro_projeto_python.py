from time import strftime, localtime
from datetime import datetime
import random

nome_funcionario = input("Digite o seu Nome e Sobrenome: ")
array_funcionarios = [nome_funcionario]

# Neste bloco é guardado a data de nascimento do funcionario,
data_aniversario_funcionario = datetime.strptime(
    input("Infome a sua data de nascimento: "), '%d/%m/%Y')
idade_funcionario = datetime.today() - data_aniversario_funcionario
resultado_idade_funcionario = int("%.0f" % float(idade_funcionario.days / 365))

# Neste bloco sera feito o loguin de usuario para acessar o sistema interno
login_usuario = ''
senha_usuario = ''
while login_usuario is senha_usuario == '':
    login_usuario = input("Escolha o Nickname: ")
    senha_usuario = input("Escola uma senha: ")

    if login_usuario and senha_usuario != '':
        print("Login Realizado com sucesso")
    elif login_usuario or senha_usuario == '':
        print("\nErro ao cadastar login, Tente novamente\n")

# Neste bloco é definido a data de registro do funcionario e é gerado o seu crachá
data_registro = strftime("%d %b %Y", localtime())
cracha_aleatorio = random.randint(1, 9999)
turno_aleatorio = ["Diurno | 08:00 ás 15:00", "Noturno | 19:00 ás 02:00 "]
cadastro_finalizado = ("\nOlá " + nome_funcionario + ", Seu Registro foi concluido com SUCESSO no dia " +
                       (data_registro) + " O seu número de crachá virtual foi gerado: " + str(cracha_aleatorio))
print(cadastro_finalizado)

if resultado_idade_funcionario <= 21:
    print("Você Irá trabalhar como Estagiario")
elif resultado_idade_funcionario >= 22:
    print("Você irá trabalhar como Operador I")

if resultado_idade_funcionario >= 22 and cracha_aleatorio >= 5000:
    print(random.choice(turno_aleatorio))
else:
    print("Horário = 8:00 ás 15:00")

print("\nLoguin no Sistema")
nome = input("Digite aqui seu loguin")
senha = input("Digite aqui sua senha")

# Adcionar aqui um método de acesso ao sistema, com verificação de loguin e senha
''' while nome != loguin_usuario:
    while senha != senha_usuario:
        print("Informações incorretas") '''

# print(array_funcionarios)
# print(resultado_idade_funcionario)
# print(data_registro)
# print(nome_funcionario)
