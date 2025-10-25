n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))
n3 = float(input('Digite a nota 3: '))

media = (n1 + n2 + n3) / 3

print('Nota final:', media)

print(f'''
      
      
aprovado? - {media >= 7}
recuperação? - {media >=5 and media <7}
reprovado? {media <= 4}

      ''')
