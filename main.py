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

    
    self.root.mainloop()    

if __name__ == '__main__':
  app = App()