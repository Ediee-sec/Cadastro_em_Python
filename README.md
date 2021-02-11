## Sistema de cadastramento

* #### *Contexto da aplicação:*

*Programa que cadastra x Funcionários, no sistema interno da empresa, solicita ao úsuario informações e com essas informações toma ações, baseadas nos dados do funcionário*

* #### *Mapa do código:*

1. **Classe que armazena as informações do funcionário**
```Python
class info_colab:
    def __init__(self):
        self.nome_funcionario = ''
        self.login_usuario = ''
        self.senha_usuario = ''


detalhes_func = info_colab()
```
___

2. **Função que solicita ao usuario a sua data de nascimento e apartir da informação. faz o calculo para identicar a sua idade, que será usada posteriormente no algoritimo**

```Python
def idade_aniversario_func():

    data_aniversario_funcionario = datetime.strptime(
        input("Infome a sua data de nascimento: "), '%d/%m/%Y')
    idade_funcionario = datetime.today() - data_aniversario_funcionario
    global resultado_idade_funcionario
    resultado_idade_funcionario = float(
        "%.1f" % float(idade_funcionario.days / 365))


idade_aniversario_func()
``` 
___
3. **Função que faz o cadastro do usuario no sistema, com login e senha**
```Python
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
```
___
4. **Função para armazenar a data de registro do funcionário + sortear um crachá aleatório + sortear um turno baseado na função idade_aniversario_func()**

```Python
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
```
___

5. **Função para logar o usuario no sistema, verifica se o login e senha são os mesmos do cadastro**

```Python
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
```

* ## *Updates:*

1.0 | 29/01/2021 - Otimização do código, encurtado utilizando a semântica correta da linguagem.

1.1 | 29/01/2021 - Adicionado as condicionais [if-elif-else]

1.2 | 30/01/2021 - Adicionado documentação do código em Markedowm

1.3 | 30/01/2021 - Adicionado cadastro no sistema interno

1.4 | 01/02/2021 - Adicionado sistema de login no sistema interno

1.5 | 04/02/2021 - Adicionado painel com informações do funcionario caso o login for True, criando um dicionário para a aplicação

1.6 | 09/02/2021 - Adcionado exeções para tratar possíveis erros

1.7 | 10/02/2021 - Adicionado arquivo de Logging, para controle de acesso e erros

1.8 | 11/02/2021 - Adicionado uma classe para armazenar as informações do colaborador
