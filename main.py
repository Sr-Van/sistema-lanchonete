import tkinter as tk
from tkinter import Listbox

class App:
  def __init__(self):
    self.root = tk.Tk()
    self.root.geometry('500x500')
    self.root.title('APP - Sabor Rapido')

    self.frame = tk.Frame(self.root)
    self.frame.grid()

    #dicionario temporaria
    self.lista_produtos = {"hamburguer": 10.0, "pizza": 15.0, "suco": 5.0}
    self.pedido = {}
    self.total_pedido = 0

    self.listbox_produtos = Listbox(self.frame)
    self.listbox_produtos.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    self.listbox_pedido = Listbox(self.frame)
    self.listbox_pedido.grid(row=2, column=5)

    self.atualizar_lista_menu()

    self.label_titulo = tk.Label(self.frame, text='Lista de produtos')
    self.label_titulo.grid(row=1, column=0)

    self.btn_criar_prod = tk.Button(self.frame, text='Novo Produto', padx=10, pady=10)
    self.btn_criar_prod.grid(row=0, column=0, columnspan=2)

    self.btn_adicionar = tk.Button(self.frame, text='Adicionar', padx=10, pady=10)
    self.btn_adicionar.grid(row=4, column=0, columnspan=2)

    self.btn_remove = tk.Button(self.frame, text='Remover',  padx=10, pady=10)
    self.btn_remove.grid(row=4, column=2, columnspan=2)
    
    self.btn_confirm = tk.Button(self.frame, text='Confirmar', padx=10, pady=10)
    self.btn_confirm.grid(row=4, column=4, columnspan=2)

    self.root.mainloop()     

  def atualizar_lista_menu(self):
    self.listbox_produtos.delete(0, tk.END)

    for produto, preco in self.lista_produtos.items():
      self.listbox_produtos.insert(tk.END, f'{produto} - R${preco}')

  def atualizar_lista_pedido(self):
    self.listbox_pedido.delete(0, tk.END)
    print(self.pedido)
    for produto, preco in self.pedido.items():
      self.listbox_pedido.insert(tk.END, f'{produto} - R${preco}') 

if __name__ == '__main__':
  app = App()