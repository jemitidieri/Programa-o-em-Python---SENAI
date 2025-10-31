# Desafio 1
# Crie um e-commerce com a estrutura de dicionários.
# Produtos:  Livros, tablets e fones de ouvido
# As ações: 
# Comprar()
# Pagar()
# mostra o valor da compra


e_commerce = {

'livros': {

'O diário da princesa': 50.0,
'Crepusculo': 120.0,
'O senhor': 200.00


},

'Papelaria': {

'Caderno': 20.0,
'Caneta': 15.0,
'Estojo': 25.0,

},

'Brinquedos': {

'Bola': 10.0,
'Boneca': 25.0,
'Jogos': 50.0,


},

}

minhas_compras = {

'carrinho': [],
'valores' : []

}

secao1 = input('livros, Papelaria, Brinquedos')
prod1 = input(f'{e_commerce[secao1]}')

secao2 = input('livros, Papelaria, Brinquedos')
prod2 = input(f'{e_commerce[secao2]}')

secao3 = input('livros, Papelaria, Brinquedos')
prod3 = input(f'{e_commerce[secao3]}')

minhas_compras['carrinho'].append(prod1)
minhas_compras['valores'].append(e_commerce[secao1][prod1])
print(minhas_compras)

minhas_compras['carrinho'].append(prod2)
minhas_compras['valores'].append(e_commerce[secao2][prod2])
print(minhas_compras)

minhas_compras['carrinho'].append(prod3)
minhas_compras['valores'].append(e_commerce[secao3][prod3])
print(minhas_compras)

total = sum(minhas_compras['valores'])
print('R$',total)