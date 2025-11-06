# Exercício 1:
# Peça ao usuário para inserir um número e manipule a exceção caso ele insira algo que não seja um número inteiro.

# try:
#     numero = int(input('Digite um número: '))
#     print(numero)

# except:
#     print('Não é um numero inteiro!')

# Exercício 2:
# Peça ao usuário para inserir dois números e realize uma operação de divisão. Manipule a exceção caso ocorra um erro na operação  -  ZeroDivisionError.

# try: 
#     n1 = int(input('Digite um número: '))
#     n2 = int(input('Digite um número: '))
#     resultado = n1 / n2
#     print(resultado)

# except ZeroDivisionError as error:
#     print(error)

# else:
#     print('Sem erros!')

# finally:
#     print('Finalizado')

# Exercício 3:
# Crie uma lista e um índice como entrada e retorne o índice. Manipule a exceção caso o índice seja inválido(caso imprima um indice que não exista na lista).



try:
    minha_lista = ['Maçã', 'Banana', 'Laranja', 'Kiwi', 'Mamão']
    indice = int(input('Digite um número: '))
    print(minha_lista[indice])

except IndexError as error:
    print('Não existe!')

finally:
    print('Finalizado!')


