## ***ATIVIDADE 2***

# Crie um sistema de notas alunos, com as seguintes operações:
# ***Utilize While ou for***

#  **Sistema de notas de alunos**

# - ***Visão do professor***

# - Acesso a conta com condicionais

# - 3 chances de acessar o sistema

# - Após errar 3 x mensagem que diga que a conta bloqueada (senha incorreta)
# - Inserir notas (se Senha correta)
# - Fazer a média

# - Utilize ***loops for, while, condicionais, variáveis, listas, tuplas ou dicionários…***

# ***IMPORTANTE:***

# - Ao finalizar o código, insira na borda do script, no última linha:

# input(’Digite enter para sair’)

senha = 1234



for chances in range(3):
    senha_prof = int(input('Digete sua senha:'))
    if senha_prof == senha:
        n1 = int(input('Digite a n1: '))
        n2 = int(input('Digite a n2: '))
        n3 = int(input('Digite a n3: '))
        media = (n1 + n2 + n3)/3
        print(round(media,2))
        if media >= 7:
                print('Você passou de ano')
        else:
                print('Você repetiu de ano!')
        break
    else: 
        print('Senha incorreta, tente novamente')
else:
    print('Senha bloqueada!')          

input('Digite enter para sair')