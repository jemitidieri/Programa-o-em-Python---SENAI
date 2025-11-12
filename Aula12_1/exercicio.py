def mercado_(lista_prod,lista_valores):
    carrinho = []
    meus_valores = []
    per = input('Deseja pedir? ')
    while per == 'sim':
       produto = int(input(f'''
                     1 {lista_prod [1]} - R$ {lista_valores[1]}
                     2 {lista_prod [2]} - R$ {lista_valores[2]}
                     3 {lista_prod [3]} - R$ {lista_valores[3]}
                     4 {lista_prod [4]} - R$ {lista_valores[4]}
                     5 {lista_prod [5]} - R$ {lista_valores[5]}
                    '''))
       carrinho.append(lista_prod[produto])
       meus_valores.append (lista_valores[produto])
       print(carrinho)
       print(meus_valores)
       soma = sum(meus_valores)
       per = input('Deseja continuar? ')

    else:
        print('Obrigado e volte sempre!')
        print('Se a compra foi efetuada, vá até pagamentos!')

def pagamentos(forma_pag):
    print(forma_pag)
    escolha = int(input('Escolha a forma de pagamento!'))
    print('Sua forma de pagamento é ', forma_pag[escolha])

def despedir (nome):
    return f'obrigada volte sempre {nome}'



def mercado():
    nome = input('Nome: ')
    lista_produtos = ['','a','b','c','d','e']
    valores = [0,55.0,60.8,12.88,9.52,5.44]
    mercado_(lista_produtos, valores)
    lista_pag = ['', '1 - Pix', '2 - CC', '3 - CD']
    pagamentos(lista_pag)
    print(despedir(nome))

mercado()
