# 1️⃣ Charada:
# O que é o que é: quanto mais você tira, maior fica?
# Resposta: Um buraco.

# 2️⃣ Charada:
# O que é o que é: tem dentes, mas não morde?
# Resposta: Um pente.

# 3️⃣ Charada:
# O que é o que é: passa diante do sol e não faz sombra?
# Resposta: O vento.

# 4️⃣ Charada:
# O que é o que é: anda com os pés na cabeça?
# Resposta: O piolho.

# 5️⃣ Charada:
# O que é o que é: vive no mar, é redondo e vive dizendo “Oi”?
# Resposta: 'O polvo!'

import random

perguntas = [
'😊Carregue novamente',
'😊O que é o que é: quanto mais você tira, maior fica?',
'😊O que é o que é: tem dentes, mas não morde?',
'😊O que é o que é: passa diante do sol e não faz sombra?',
'😊O que é o que é: anda com os pés na cabeça?',
'😊O que é o que é: vive no mar, é redondo e vive dizendo “Oi”?'
]


respostas = ['','1- Um buraco', '2- Um pente', '3- O vento', '4- O piolho', '5- O polvo!' ]



per_aleatorio = random.choice(perguntas)
indice = perguntas.index(per_aleatorio) 
print(f'''
PERGUNTA...
{per_aleatorio}???
''')

resp_user = int(input(f'''
{respostas[1]}
{respostas[2]}
{respostas[3]}
{respostas[4]}
{respostas[5]}
>>>'''))

if indice == resp_user:
    print('Acertou em cheio, a resposta é', indice)
else:
    print('Errou feio a resposta é', indice)
