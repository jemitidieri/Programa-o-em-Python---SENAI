import tkinter as tk
from tkinter import messagebox

def inserir_nome():


    texto_1 =  nome_1.get()
    
    texto_2 = idade_1.get()
    
    texto_3 = email_1.get()
    
    texto_4 = celular_1.get()
    
    texto_5 = endereco_1.get()
    
    texto_6 = cidade_1.get()
    
    texto_7 = cep_1.get()
    
    texto_8 = curso_1.get()
    

    if texto_1 and texto_2 and texto_3 and texto_4 and texto_5 and texto_6 and texto_7 and texto_8:
        print('Nome:', texto_1)
        print('Idade:',texto_2)
        print('E-mail:', texto_3)
        print('Celular:', texto_4)
        print('Endereço:', texto_5)
        print('Cidade:', texto_6)
        print('CEP:', texto_7)
        print('Curso:', texto_8)


        messagebox.showinfo('Sucesso!', 'Dados inseridos com sucesso')
        
    else:
        messagebox.showerror('Erro!', 'Erro nos dados')

tela = tk.Tk()
tela.geometry('1700x750')

tk.Label(tela, text='Cadastro de Cliente', font=('arial', 16)).grid(padx=10, pady=10)

nome = tk.Label(tela, text = 'Nome', font=('arial',16) )
nome.grid(pady=5, column=1, row =1 )

nome_1 = tk.Entry(tela, font=('arial', 12))
nome_1.grid(row=1, column=2, padx=5)


idade = tk.Label(tela, text = 'Idade', font=('arial',16) )
idade.grid(pady=5, column=1, row =2 )

idade_1 = tk.Entry(tela, font=('arial', 12))
idade_1.grid(row=2, column=2, padx=5)


email = tk.Label(tela, text = 'E-mail', font=('arial',16) )
email.grid(pady=5, column=1, row =3 )

email_1 = tk.Entry(tela, font=('arial', 12))
email_1.grid(row=3, column=2, padx=5)


celular = tk.Label(tela, text = 'Celular', font=('arial',16) )
celular.grid(pady=5, column=1, row =4 )

celular_1 = tk.Entry(tela, font=('arial', 12))
celular_1.grid(row=4, column=2, padx=5)


endereco = tk.Label(tela, text = 'Endereço', font=('arial',16) )
endereco.grid(pady=5, column=1, row =5 )

endereco_1 = tk.Entry(tela, font=('arial', 12))
endereco_1.grid(row=5, column=2, padx=5)


cidade = tk.Label(tela, text = 'Cidade', font=('arial',16) )
cidade.grid(pady=5, column=1, row =6 )

cidade_1 = tk.Entry(tela, font=('arial', 12))
cidade_1.grid(row=6, column=2, padx=5)


cep = tk.Label(tela, text = 'CEP', font=('arial',16) )
cep.grid(pady=5, column=1, row =7 )

cep_1 = tk.Entry(tela, font=('arial', 12))
cep_1.grid(row=7, column=2, padx=5)


curso = tk.Label(tela, text = 'Cursos', font=('arial',16) )
curso.grid(pady=5, column=1, row =8 )

curso_1 = tk.Entry(tela, font=('arial', 12))
curso_1.grid(row=8, column=2, padx=5)

btn_enviar = tk.Button(tela, text='Enviar', font=('arial', 16), command=inserir_nome)
btn_enviar.grid(row=15, column= 1, pady=5,padx=5)




tela.mainloop()

