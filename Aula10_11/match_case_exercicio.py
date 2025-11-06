# EXERCÍCIOS com match/ case:*** 

# 1: Verificando se o número é par ou ímpar***

# numero = int(input('Digite um numero: '))

# match numero: 
#     case numero if numero % 2 == 0:
#         print('Este número é par!')
#     case _:
#         print('ests número é ímpar!')


# 2: Verificando se um número é positivo, negativo ou zero***

# match numero:
#     case numero if numero > 0:
#         print('Positivo')
#     case numero if numero < 0:
#         print('Negativo')
#     case _:
#         print('Zero!')


# 3: Verificando se uma string é vazia ou não***

# texto = input('Digite algo: ')

# match texto:
#     case '':
#         print('Está vazio!')
#     case _:
#         print('Não está vazio!')



# 4: Verificando se um número é maior, menor ou igual a 10***

# match numero: 
#     case numero if numero > 10:
#         print('Este número é maior que 10!')
#     case numero if numero < 10:
#         print('Este número é menor que 10!')
#     case _:
#         print('Número 10!')
    

# 5: Classificando uma idade em faixas etárias -  criança(12), adolescente(17), jovem(35), adulto 35 ><64, idoso(65)***

# match numero:
#     case numero if numero <= 12:
#         print('Criança!')
#     case numero if numero > 12 and numero <= 17:
#         print('Adolescente!')
#     case numero if numero > 17 and numero <= 35:
#         print('Jovem!')
#     case numero if numero > 35 and numero <= 64:
#         print('Adulto!')
#     case _:
#         print('Idoso!')


        
    