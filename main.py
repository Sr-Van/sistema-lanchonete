import tkinter as tk
from tkinter import Listbox, messagebox, simpledialog, ttk
from ttkthemes import ThemedTk

class App:
  def __init__(self):
    self.root = ThemedTk(theme="breeze")
    self.root.geometry('500x500')
    self.root.title('APP - Sabor Rapido')

    self.frame = ttk.Frame(self.root)
    self.frame.grid()

    self.style = ttk.Style(self.root)
    self.style.configure('Custom.TButton', background='blue', foreground='black', font=('Arial', 12))

    #dicionario temporaria
    self.lista_produtos = {"hamburguer": 10.0, "pizza": 15.0, "suco": 5.0}
    self.pedido = {}
    self.total_pedido = 0

    self.listbox_produtos = Listbox(self.frame)
    self.listbox_produtos.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    self.listbox_pedido = Listbox(self.frame)
    self.listbox_pedido.grid(row=3, column=5)

    self.atualizar_lista_menu()

    self.label_titulo = ttk.Label(self.frame, text='Lista de produtos')
    self.label_titulo.grid(row=2, column=0, ipadx=12, ipady=12)

    self.label_hold = ttk.Label(self.frame, text="")
    self.label_hold.grid(row=4, column=0, ipadx=25, ipady=25)

    self.label_pedido = ttk.Label(self.frame, text='Pedido:')
    self.label_pedido.grid(row=2, column=5, ipadx=12, ipady=12)

    self.btn_criar_prod = ttk.Button(self.frame, text='Novo Produto',command=self.adicionar_produto, style='Custom.TButton')
    self.btn_criar_prod.grid(row=0, column=0, columnspan=2, ipadx=20, ipady=20)

    self.btn_adicionar = ttk.Button(self.frame, text='Adicionar', command=self.adicionar_ao_pedido, style='Custom.TButton')
    self.btn_adicionar.grid(row=5, column=0, columnspan=2, ipadx=20, ipady=20)

    self.btn_remove = ttk.Button(self.frame, text='Remover',  command=self.remover_do_pedido, style='Custom.TButton')
    self.btn_remove.grid(row=5, column=5, columnspan=2, ipadx=20, ipady=20)
    
    self.btn_confirm = ttk.Button(self.frame, text='Confirmar', command=self.emitir_recibo, style='Custom.TButton')
    self.btn_confirm.grid(row=0, column=5, columnspan=2, ipadx=20, ipady=20)

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

  def adicionar_ao_pedido(self):
      indice = self.listbox_produtos.curselection()
      print('verificando indice:', indice)
      if indice:
        selecionado = self.listbox_produtos.get(indice[0]).split(' - ')
        print(f'adicionando: {selecionado}')

        chave = selecionado[0]
        valor = float(selecionado[1].split('$')[1]) #gambiarra pra separar o R$ e armazenar apenas o valor

        self.pedido[chave] = valor
        self.atualizar_lista_pedido()

      else:
        messagebox.showerror('Nada selecionado', 'Selecione um item para adicionar!')

      self.calculo_total()

  def remover_do_pedido(self):
      indice = self.listbox_pedido.curselection()
      print('verificando indice:', indice)
      if indice:
        selecionado = self.listbox_pedido.get(indice[0]).split(' - ')
        produto = selecionado[0]
        
        print(f'adicionando: {selecionado}')
        to_remove = messagebox.askyesno('Remover Item', f'Deseja remover: {selecionado}')
        print('item: ', to_remove)
        if to_remove:
          self.pedido.pop(produto)
      else:
        messagebox.showerror('Nada selecionado', 'Selecione um item para adicionar!')

      self.calculo_total()

  def adicionar_produto(self):

    nome_produto = simpledialog.askstring("Nome do Produto", "PRODUTO",
                                parent=self.root)
    
    preco_produto = simpledialog.askinteger("Preco do Produto", "PRECO", parent=self.root)
    print(type(nome_produto))

    if nome_produto and preco_produto:
      self.lista_produtos[f'{nome_produto}'] = float(preco_produto)
      print(self.listbox_produtos)
      print(f'dados preenchidos, depois logica para adicionar produtos. aqui os dados: {nome_produto}, {preco_produto}')
      self.atualizar_lista_menu()

  def calculo_total(self):
    self.atualizar_lista_pedido()
    self.total_pedido = 0
    for produto, valor in self.pedido.items():
      print(f'Calculando {produto} no preco de {valor}')
      self.total_pedido+= valor

    self.label_total = ttk.Label(self.frame, text=f'Total: {self.total_pedido}')
    self.label_total.grid(row=4, column=0, ipadx=25, ipady=25)
    
  def emitir_recibo(self):
    pedido = ''
    for produto, preco in self.pedido.items():
      pedido += f'- {produto} - R$ {preco} \n'

    pedido += f'TOTAL: {self.total_pedido} \n'

    messagebox.showinfo('recibo', pedido)
  
if __name__ == '__main__':
  app = App()