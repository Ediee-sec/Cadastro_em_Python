from time import strftime, localtime
from datetime import datetime
import random

nome_funcionario = input("Digite o seu Nome e Sobrenome: ")
array_funcionarios = [nome_funcionario]

# Neste bloco é guardado a data de nascimento do funcionario,
data_aniversario_funcionario = datetime.strptime(
    input("Infome a sua data de nascimento: "), '%d/%m/%Y')
data_hoje = datetime.today()
idade_funcionario = data_hoje - data_aniversario_funcionario

# Neste bloco é definido a data de registro do funcionario e é gerado o seu crachá
data_registro = strftime("%d %b %Y", localtime())
cracha_aleatorio = random.randint(1, 9999)
cadastro_finalizado = ("\nOlá " + nome_funcionario + ", Seu Registro foi concluido com SUCESSO no dia " +
                       (data_registro) + " O seu número de crachá virtual foi gerado: " + str(cracha_aleatorio))
print(cadastro_finalizado)

# print(array_funcionarios)
# print(idade_funcionario)
# print(data_registro)
# print(nome_funcionario)
