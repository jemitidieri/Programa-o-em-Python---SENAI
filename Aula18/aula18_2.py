import tkinter as tk


def mostrar_resultado_soma():
    n1_ = float(n1.get())
    n2_ = float(n2.get())
    soma  = n1_ +  n2_
    resultado.config(text=soma) 

def mostrar_resultado_sub():
    n1_ = float(n1.get())
    n2_ = float(n2.get())
    subtrair  = n1_ -  n2_
    resultado.config(text=subtrair) 

def mostrar_resultado_mult():
    n1_ = float(n1.get())
    n2_ = float(n2.get())
    multiplicar  = n1_ *  n2_
    resultado.config(text=multiplicar) 

def mostrar_resultado_div():
    n1_ = float(n1.get())
    n2_ = float(n2.get())
    dividir  = n1_ /  n2_
    resultado.config(text=dividir) 

root = tk.Tk()
root.geometry('250x370')


n1_label =  tk.Label(root, text='N1', font=('arial',12))
n1_label.grid(pady=5, column=1, row =1 )

n1 =  tk.Entry(root, font=('arial',12))
n1.grid(row=1, column=2, padx=5)

n2_label =  tk.Label(root, text='N2', font=('arial',12))
n2_label.grid(pady=5, column=1, row =3 )

n2 =  tk.Entry(root, font=('arial',12))
n2.grid(row=3, column=2, padx=5)

fr = tk.Frame(root)
fr.grid(columnspan=4, padx=5)


btn_soma =  tk.Button(fr, text= '+', font=('arial',10), command=mostrar_resultado_soma)
btn_soma.grid(row=5, column= 1, pady=5,padx=5)

btn_subtrair =  tk.Button(fr, text= '-', font=('arial',10), command=mostrar_resultado_sub)
btn_subtrair.grid(row=5, column=2, pady=3, padx=5)

btn_multiplicar =  tk.Button(fr, text= '*', font=('arial',10), command=mostrar_resultado_mult)
btn_multiplicar.grid(row=5, column= 3, pady=5, padx=5)

btn_dividir =  tk.Button(fr, text= '/', font=('arial',10), command=mostrar_resultado_div)
btn_dividir.grid(row=5, column=4 , pady=20, padx=5)


resultado =  tk.Label(root, text = '=', font=('arial',12))
resultado.grid(row = 6, column=2)



root.mainloop()
