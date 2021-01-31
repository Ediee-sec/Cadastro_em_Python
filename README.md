## Sistema de cadastramento
* #### *Contexto da aplicação:*
*Programa que cadastra x Funcionários, no sistema interno da empresa, solicita ao úsuario informações e com essas informações toma ações, baseadas nos dados do funcionário*

* #### *Mapa do código:*
1. *Bloco de código que apartir da informação do úsuario. faz o calculo para identicar a sua idade*
```
data_aniversario_funcionario = datetime.strptime(
   input("Infome a sua data de nascimento: "), '%d/%m/%Y')
idade_funcionario = datetime.today() - data_aniversario_funcionario
resultado_idade_funcionario = int("%.0f" % float(idade_funcionario.days / 365))
``` 

2. *Bloco de código que define com base nas informações do funcionário, o crachá dele, periodo em que irá trabalhar e sua função dentro da empresa*
```
data_registro = strftime("%d %b %Y", localtime())
cracha_aleatorio = random.randint(1, 9999)
turno_aleatorio = ["Diurno | 08:00 ás 15:00", "Noturno | 19:00 ás 02:00 "]
cadastro_finalizado = ("\nOlá " + nome_funcionario + ", Seu Registro foi concluido com SUCESSO no dia " +
                       (data_registro) + " O seu número de crachá virtual foi gerado: " + str(cracha_aleatorio))
```

3. *Bloco de código que faz o cadastramento do login do úsuario ao sistema; OBS:A semântica não está da forma que tem que estar, tem que arrumar*
```
loguin_usuario = ''
senha_usuario = ''
while loguin_usuario is senha_usuario == '':
    loguin_usuario = input("Escolha o Nickname: ")
    senha_usuario = input("Escola uma senha: ")

    if loguin_usuario and senha_usuario != '':
        print("Loguin Realizado com sucesso")
    elif loguin_usuario or senha_usuario == '':
        print("\nErro ao cadastar loguin, Tente novamente\n")
```

* ## *Updates:*
1.0 | 29/01/2021 - Otimização do código, encurtado utilizando a semântica correta da linguagem.

1.1 | 29/01/2021 - Adicionado as condicionais [if-elif-else]

1.2 | 30/01/2021 - Adionado documentação do código em Markedowm

1.3 | 30/01/2021 - Adicionado Sistema de loguin
