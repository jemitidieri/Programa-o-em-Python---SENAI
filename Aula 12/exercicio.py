## Exercícios com funções:

# variáveis locais, globais e parâmetros

# 1 - CRIE UMA FUNÇÃO PARA COMPARAR 2 NÚMEROS (par ou impar). UTILIZE VARIÁVEIS LOCAIS.***


# def comparar():
#     n1 = int(input('Digite um número: '))
#     n2 = int(input('Digite um número: '))

#     if n1 % 2 == 0 and n2 % 2 == 0:
#         print('Ambos são pares!')
#     elif n1 % 2 == 0 or n2 % 2 == 0:
#         print('Apenas 1 é par!')
#     else:
#         print('Ambos são ímpares!')
        
# comparar()

# 2 - CRIE UMA FUNÇÃO PARA MULTIPLICAR 3 NUMEROS.***

# def multiplicar():
    
#     n1 = int(input('Digite um número: '))
#     n2 = int(input('Digite um número: '))
#     n3 = int(input('Digite um número: '))
#     resultado = n1 * n2 * n3
#     print(resultado)

# multiplicar()

# 3 - CRIE UMA FUNÇÃO PARA DESCOBRIR O VALOR ELEVADO DE UM NÚMERO.***

# def elevado():

#     n1 = int(input('Digite um número: '))
#     n2 = int(input('Digite um valor elevado: '))
#     resultado = n1**n2
#     print(resultado)

# elevado()

# 4 - CRIE UMA FUNÇÃO PARA MOSTRAR UMA MENSAGEM PERSONALIZADA NA TELA, SE O USUÁRIO  DIGITAR, 18 ANOS.***

# def mensagem():

#     idade = int(input('Digite sua idade: '))
#     if idade == 18:
#         print('18 anos!')
#     else:
#         print('Você não tem 18 anos!')

# mensagem()

# 5 - DESENVOLVA UMA FUNÇÃO PARA DESCOBRIR A IDADE DE UMA PESSOA.***

# def mostrar_idade():

#     ano_atual = 2025
#     ano_nascimento = int(input('Digite o ano do seu nascimento: '))
#     mes = int(input('Digite o mês atual: '))
#     if mes < 11:
#         idade = ano_atual - ano_nascimento
#         print(idade, 'anos')
#     else:
#         idade = ano_atual - (ano_nascimento + 1)
#         print(idade, 'anos')

# mostrar_idade()

# 6 - DESENVOLVA UMA FUNÇÃO PARA VER SE O BRASIL GANHOU A COPA DE 1999.***

# def copa():

    # copa_do_mundo = [1958,1962,1970,1994,2002]
    # ano = int(input('Digite o ano que vc acha que o Brasil ganhou a copa: '))

    # if ano in copa_do_mundo:
    #     print('Ganhou a copa!')
    # else:
    #     print('Não ganhou a copa!')

# copa()


# 7 -DESENVOLVA UM SISTEMA DE RESTAURANTE, ONDE O CLIENTE TEM OPÇÃO DE ESCOLHER ENTRE SALADA, MACARRONADA, SANDUICHE, SORVETE.***  

# def cumprimento():

#     print('Seja bem-vindo!')

# def restaurante():
#     pergunta = input('Deseja pedir?')
#     carrinho = []
#     while pergunta == "sim":
#         cumprimento()
#         lista = ['','salada', 'macarronada', 'sanduiche', 'sorvete']
#         print(lista)
        
#         carrinho.append(lista[int(input('Escolha o id do produto: 1 - Salada, 2 - Macarronada, 3 - Sanduiche, 4 - Sorvete '))])
#         print('Escolheu', carrinho)
#         pergunta = input('Deseja continuar?')
#     else:
#         print('Obrigada volte sempre!')
    

# restaurante()

#     1 - Função -  cumprimentar o cliente***

#     2 - Função - restaurante***

#     3 - Sugestão utilize listas  e loops***
