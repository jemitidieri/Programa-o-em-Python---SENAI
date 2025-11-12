import statistics as st

def estatistica(lista_notas):
    
    moda1 = st.mode(lista_notas)
    print('A moda é', moda1)

    media = st.mean(lista_notas)
    print('A média é',media)

    mediana = st.median(lista_notas)
    print('A mediana é',mediana)

    desvio_padrao = st.stdev(lista_notas)
    print('O desvio padrão é', desvio_padrao)

    maior_nota = max(lista_notas)
    print('A maior nota é',maior_nota)

    menor_nota = min(lista_notas)
    print('A menor nota é', menor_nota)
