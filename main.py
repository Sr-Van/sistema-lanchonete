import tkinter as tk
from tkinter import Listbox, messagebox, simpledialog, ttk, font
from ttkthemes import ThemedTk

class App:
  def __init__(self):
    self.root = ThemedTk(theme="arc")
    self.root.attributes('-fullscreen', True)
    self.root.title('APP - Sabor Rapido')
    self.root.configure(bg="#f0f0f0")

    # -- binds --
    self.root.bind("<F11>", self.toggle_fullscreen)
    self.root.bind("<Escape>", self.end_fullscreen)

    # -- control vars --
    self.isFullscreen = False

    # -- custom styles --
    self.style = ttk.Style(self.root)
    self.style.configure('Custom.TButton', foreground='black', font=('Arial', 16))
    self.style.configure('Custom.TFrame', background="#f0f0f0", foreground='black', font=('Arial', 16))
    self.style.configure('Custom.TLabel' ,background='#f0f0f0', foreground='black', font=('Arial', 16))
    self.custom_font = font.Font(family='Arial', size=16)

    # -- frames --
    
    self.upper_buttons = ttk.Frame(self.root, style='Custom.TFrame', height=150)
    self.upper_buttons.pack(side='top', fill='x', padx=15, pady=10)
    self.upper_buttons.pack_propagate(False)

    self.lower_buttons = ttk.Frame(self.root, style='Custom.TFrame', height=150)
    self.lower_buttons.pack(side='bottom', fill='x', padx=15, pady=10)
    self.lower_buttons.pack_propagate(False)

    self.middle_frame = ttk.Frame(self.root, style='Custom.TFrame')
    self.middle_frame.pack(side='top', fill='both', expand=True, padx=15, pady=10)

    self.left_frame = ttk.Frame(self.middle_frame, style='Custom.TFrame')
    self.left_frame.pack(side='left', fill='both', expand=True, padx=15, pady=10)

    self.right_frame = ttk.Frame(self.middle_frame, style='Custom.TFrame')
    self.right_frame.pack(side='right', fill='both', expand=True, padx=15, pady=10)


    #dicionario temporaria
    self.lista_produtos = {"hamburguer": 10.0, "pizza": 15.0, "suco": 5.0}
    self.pedido = {}
    self.total_pedido = 0

    # -- top --

    self.btn_criar_prod = ttk.Button(self.upper_buttons, text='Novo Produto (F1)',command=self.adicionar_produto, style='Custom.TButton', width=20)
    self.btn_criar_prod.pack(side='left', fill='y', ipadx=10, ipady=10, padx=10, pady=10)

    self.btn_confirm = ttk.Button(self.upper_buttons, text='Confirmar (F10)', command=self.emitir_recibo, style='Custom.TButton', width=20)
    self.btn_confirm.pack(side='right', fill='y', ipadx=10, ipady=10, padx=10, pady=10)

    # -- bottom --

    self.btn_adicionar = ttk.Button(self.lower_buttons, text='Adicionar (ENTER)', command=self.adicionar_ao_pedido, style='Custom.TButton', width=20)
    self.btn_adicionar.pack(side='left', fill='y',ipadx=10, ipady=10, padx=10, pady=10)

    self.btn_remove = ttk.Button(self.lower_buttons, text='Remover (DELETE)',  command=self.remover_do_pedido, style='Custom.TButton', width=20)
    self.btn_remove.pack(side='right', fill='y',ipadx=10, ipady=10, padx=10, pady=10)

    #-- left --

    self.label_titulo = ttk.Label(self.left_frame, text='Lista de produtos', style='Custom.TLabel')
    self.label_titulo.pack(side='top', fill='x', ipadx=25, ipady=25)

    self.listbox_produtos = Listbox(self.left_frame, width=20, height=10, bg='#ffecb7', fg='black', font=self.custom_font, selectbackground='orange', selectforeground='black', relief='ridge')
    self.listbox_produtos.pack( fill='both', expand=True, ipadx=10, ipady=10)

    self.label_total = ttk.Label(self.left_frame, text=f'TOTAL: {self.total_pedido}', style='Custom.TLabel')
    self.label_total.pack(side='bottom', fill='x', ipadx=25, ipady=25)

    #-- right --

    self.label_pedido = ttk.Label(self.right_frame, text='Pedido:', style='Custom.TLabel')
    self.label_pedido.pack(side='top', fill='x', ipadx=25, ipady=25)

    self.listbox_pedido = Listbox(self.right_frame, width=20, height=10, bg='#ffecb7', fg='black', font=self.custom_font, selectbackground='orange', selectforeground='black', relief='ridge')
    self.listbox_pedido.pack( fill='both', expand=True, ipadx=10, ipady=10)

    self.atualizar_lista_menu()
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
    
    self.label_total.config(text=f'TOTAL: {self.total_pedido}')
    self.label_total.update_idletasks() 
    
  def emitir_recibo(self):
    pedido = ''
    for produto, preco in self.pedido.items():
      pedido += f'- {produto} - R$ {preco} \n'

    pedido += f'TOTAL: {self.total_pedido} \n'

    messagebox.showinfo('recibo', pedido)
  
  def toggle_fullscreen(self, event):
    self.isFullscreen = not self.isFullscreen
    self.root.attributes('-fullscreen', self.isFullscreen)
    return "break"
  
  def end_fullscreen(self, event):
    self.isFullscreen = False
    self.root.attributes('-fullscreen', self.isFullscreen)
    return "break"
if __name__ == '__main__':
  app = App()