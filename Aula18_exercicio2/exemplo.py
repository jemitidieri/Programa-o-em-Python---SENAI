import tkinter as tk
from tkinter import messagebox


def display():

    nome  = dado1.get()
    idade = dado2.get()
    email = dado3.get()
    celular = dado4.get()
    cep = dado5.get()
    cidade = dado6.get()
    curso = dado7.get()
    endereco = dado8.get()

    if nome and idade and email and cidade and cep and curso and endereco :

        print(f'''
            Nome: {nome}
            Idade: {idade}
            email: {email}  
            celular:{celular}
            cep: {cep}
            cidade: {cidade}
            curso:{curso}
            endereço:{endereco} 
        ''')
        
        messagebox.showinfo('Sucesso!', 'Dados inseridos com sucesso')
    else:
        messagebox.showwarning('erro', 'Insira todos os dados!')



root = tk.Tk()
root.geometry('1700x750')

# fr = tk.Frame(root)
# fr.grid(pady=10)

tk.Label(root,text='Formulário de cadastro', font=('arial', 16)).grid(padx=10, pady=10)

tk.Label(root,text = 'Nome:', font=('arial', 16)).grid(row = 1, column=1, padx=10, pady=10)
dado1 = tk.Entry(root,font=('arial', 16))
dado1.grid(row= 1, column=2, padx=10, pady=10)


tk.Label(root,text = 'Idade:', font=('arial', 16)).grid(row = 2, column=1,padx=10, pady=10)
dado2 = tk.Entry(root,font=('arial', 16))
dado2.grid(row= 2, column=2, padx=10, pady=10)

tk.Label(root,text = 'E-mail:', font=('arial', 16)).grid(row = 3, column=1,padx=10, pady=10)
dado3 = tk.Entry(root,font=('arial', 16))
dado3.grid(row= 3, column=2, padx=10, pady=10)


tk.Label(root,text = 'Celular:', font=('arial', 16)).grid(row = 4, column=1,padx=10, pady=10)
dado4 = tk.Entry(root,font=('arial', 16))
dado4.grid(row=4, column=2, padx=10, pady=10)

tk.Label(root,text = 'CEP:', font=('arial', 16)).grid(row = 5, column=1,padx=10, pady=10)
dado5 = tk.Entry(root,font=('arial', 16))
dado5.grid(row= 5, column=2, padx=10, pady=10)

tk.Label(root,text = 'Cidade:', font=('arial', 16)).grid(row = 6, column=1,padx=10, pady=10)
dado6 = tk.Entry(root,font=('arial', 16))
dado6.grid(row= 6, column=2, padx=10, pady=10)

tk.Label(root,text = 'Curso', font=('arial', 16)).grid(row = 7, column=1,padx=10, pady=10)
dado7 = tk.Entry(root,font=('arial', 16))
dado7.grid(row= 7, column=2, padx=10, pady=10)


tk.Label(root,text = 'Endereço', font=('arial', 16)).grid(row = 8, column=1,padx=10, pady=10)
dado8 = tk.Entry(root,font=('arial', 16))
dado8.grid(row= 8, column=2, padx=10, pady=10)


T = tk.Button(root, text = 'Enviar', font=('arial', 16), command=display)
T.grid(row = 10, column=1,padx=10, pady=10)

root.mainloop()




