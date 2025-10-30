# nome = estutruta dado ou objeto
# estrutura composta
# pode ser interável - percorrivel

# lista vazia
# lista_vazia = []
# print(lista_vazia)

# lista com valores inteiros

# lista = [5, 1 , 2, 3, 8, 16]
# lista_t = ['a', 'k', 'b' , 'p', 'g']
#        0 , 1, 2 - indices positivos
#       -3, -2, -1 - indices negativos

# print(lista[0]) - acessar o indica

# n1 = lista[0]
# n2 = lista[1]
# print(n1 + n2)

# funcões de listas:


# dir é para mostrar quais funções pode usar com objeto
# print(dir(lista))

#len() - comprimento - qual o tamanho da lista, retorna em números
# print(len(lista))

#sum() - soma a lista numerica
# print(sum(lista))

#max() - maior numero da lista
# print(max(lista))

#min() - menor numero da lista
# print(min(lista))

# sorted() - organiza a lista, só não ppode ser mista (numeros e textos)
# print(sorted(lista))


# métodos de listas

lista = [5, 1 , 2, 3, 8, 16, 8, 5, 8, 10, 8]
lista_t = ['a', 'k', 'b' , 'p', 'g']

#append -  adiciona 1 valor ao final

# lista.append(100)
# print(lista)

# insert - adiciona no indice que vc quiser, (coloca a posição que quer e depois o valor que quer inserir)

# lista.insert(10, 250)
# print(lista)

# count() - conta quando vezes repete dentro da lista

# print(lista.count(8))



# extend - adiciona vários dados de uma vez mas no final

# +=() - adiciona variso dados ao final

# adicionando manualmente

# lista[0] = 500
# print(lista)


# removendo dados da lista - remove valor e não o indice apenas 1 valor

# lista.remove(500)
# print(lista)

# del - deleta de dentro pra fora, tem que colocar quial indice que quer

# del lista[0]
# print(lista)

# pop - deleta numero pelo indice ou sem indice, quando não coloca o indice remove o ultimo numero da lista, quando coloca remove o que representa o indice

# lista.pop()
# print(lista)

# lista.pop(1)
# print(lista)

# sort - ordena do menor para o maior

# lista.sort()
# print(lista)

# sort(reverse = True) - ordena do maior para o menor

# lista.sort(reverse = True)
# print(lista)

# copy - copia a lista

# x = lista.copy()
# print(x)

# index - verifica a posição do valor que quer saber

# indice = lista.index(5)
# print(indice)

# split - transforma os caracteres numa lista

# x = 'texto'
# print(x.split())

# clear - limpar dados de toda lista

# lista.clear()
# print(lista)


# fazer listas
# fazer uma lista de 0 a 10

# lista_0_10 = list(range(11))
# print(lista_0_10)

# fazer uma lista de 1 a 10

lista_1_10 = list(range(1,11))
print(lista_1_10)

# fazer uma lista de 1 ate 10 de 2 em 2 numeros

lista_1_10_2 = list(range(1,11,2))

