import tkinter as tk
from aluno import Aluno

janela = tk.Tk()
A = Aluno()

def processar():
    print(entry_idade.get())
    print(entry_sobrenome.get())
    
    #A.cadastrar(entry_nome.get(), entry_sobrenome.get(), entry_idade.get(), entry_telefone.get())
    entry_nome.delete(0, "end")
    entry_sobrenome.delete(0, "end")
    entry_idade.delete(0, "end")
    entry_telefone.delete(0, "end")

janela.title("Area de Cadastro")

label_nome = tk.Label(janela, text="Nome", fg="purple", font=('arial', 18))
label_nome.grid(row=0, column=0, padx=10, pady=10)

label_sobrenome = tk.Label(janela, text="sobrenome", fg="purple", font=('arial',18))
label_sobrenome.grid(row=1, column=0, padx=10, pady=10)

label_idade = tk.Label(janela, text="idade", fg="purple", font=('arial', 18))
label_idade.grid(row=2, column=0, padx=10, pady=10)

label_telefone = tk.Label(janela, text="telefone", fg="purple", font=('arial', 18))
label_telefone.grid(row=3, column=0, padx=10, pady=10)


entry_nome = tk.Entry(janela, width=30)
entry_nome.grid(row=0, column=1, padx=1, pady=10)

entry_sobrenome= tk.Entry(janela, width=30)
entry_sobrenome.grid(row=2, column=1, padx=1, pady=10)

entry_idade= tk.Entry(janela, width=30)
entry_idade.grid(row=1, column=1, padx=1, pady=10)



entry_telefone= tk.Entry(janela, width=30)
entry_telefone.grid(row=3, column=1, padx=1, pady=10)

botao_cadastrar = tk.Button(janela, text="CADASTRAR", command=processar)
botao_cadastrar.grid(row=4, column=1, padx=10, pady=10)

janela.mainloop()