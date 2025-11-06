def display():
    try:
        # n  =  1/0
        n  = 10
        l = []
        print(l[10])
        # x  = int(input('='))
        # print(n + x)
        # print(a)
    except NameError as erro:
        print(erro)   
    except ZeroDivisionError as erro:
        print(erro)   
    except ValueError as erro:
        print(erro)  
    except IndexError as erro:
        print(erro)            
    else:
        print('Ocorreu um erro não identificado')
    finally:
        print('fim de carregamento...')        


display()        