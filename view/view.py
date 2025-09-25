import tkinter as tk
from tkinter import Listbox, messagebox, simpledialog, ttk, font
from ttkthemes import ThemedTk
from view.modal import Recibo

class App:
  def __init__(self, controller):
    self.controller = controller

    self.root = ThemedTk(theme="arc")
    self.root.attributes('-fullscreen', True)
    self.root.title('APP - Sabor Rapido')
    self.root.configure(bg="#f0f0f0")

    # -- binds --
    self.root.bind("<F11>", self.toggle_fullscreen)
    self.root.bind("<Return>", self.adicionar_ao_pedido)
    self.root.bind("<Delete>", self.remover_do_pedido)
    self.root.bind("<F1>", self.adicionar_produto)
    self.root.bind("<F10>", self.emitir_recibo)
    self.root.bind("<Escape>", self.end_fullscreen)

    # -- control vars --
    self.isFullscreen = False

    # -- custom styles --
    self.style = ttk.Style(self.root)
    self.style.configure('Custom.TButton', foreground='black', font=('Arial', 16))
    self.style.configure('Custom.TFrame', background="#f0f0f0", foreground='black', font=('Arial', 16))
    self.style.configure('Custom.TLabel' ,background='#f0f0f0', foreground='black', font=('Arial', 16))
    self.style.configure("Treeview", rowheight=35, font=('Arial', 11))
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
    self.lista_produtos = self.controller.pegar_produtos()
    self.pedido = []
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

    self.tree_produtos = ttk.Treeview(self.left_frame, columns=('col1', 'col2'), show='headings', height=10)
    self.tree_produtos.pack(fill='both', expand=True, ipadx=10, ipady=10)
    self.tree_produtos.heading('col1', text='Produto')
    self.tree_produtos.heading('col2', text='Preco')

    self.listbox_produtos = Listbox(self.left_frame, width=20, height=10, bg='#ffecb7', fg='black', font=self.custom_font, selectbackground='orange', selectforeground='black', relief='ridge')

    self.label_total = ttk.Label(self.left_frame, text=f'TOTAL: {self.total_pedido}', style='Custom.TLabel')
    self.label_total.pack(side='bottom', fill='x', ipadx=25, ipady=25)

    #-- right --

    self.label_pedido = ttk.Label(self.right_frame, text='Pedido:', style='Custom.TLabel')
    self.label_pedido.pack(side='top', fill='x', ipadx=25, ipady=25)

    self.tree_pedido = ttk.Treeview(self.right_frame, columns=('col0','col1', 'col2', 'col3'), show='headings', height=10)
    self.tree_pedido.pack(fill='both', expand=True, ipadx=10, ipady=10)
    self.tree_pedido.heading('col0', text='ID')
    self.tree_pedido.heading('col1', text='Quantidade')
    self.tree_pedido.heading('col2', text='Produto')
    self.tree_pedido.heading('col3', text='Preço')

    self.listbox_pedido = Listbox(self.right_frame, width=20, height=10, bg='#ffecb7', fg='black', font=self.custom_font, selectbackground='orange', selectforeground='black', relief='ridge')

    self.atualizar_lista_menu()
    self.root.mainloop()     

  def atualizar_lista_menu(self):
    primeiro_item = None
    self.lista_produtos = []
    self.lista_produtos = self.controller.pegar_produtos()
    print(self.lista_produtos)
    for i in self.tree_produtos.get_children():
            self.tree_produtos.delete(i)

    for produto, preco in self.lista_produtos.items():
      item = self.tree_produtos.insert("", tk.END, values=(produto, preco))

      if primeiro_item is None:
         primeiro_item = item
    
    if primeiro_item:
      self.tree_produtos.selection_set(primeiro_item)
      self.tree_produtos.focus(primeiro_item)

    self.tree_produtos.focus_set()

  def atualizar_lista_pedido(self):

    for i in self.tree_pedido.get_children():
            self.tree_pedido.delete(i)

    for item in self.pedido:
      iid, quantidade, produto, preco = item.values()
      self.tree_pedido.insert("", tk.END, values=(iid, quantidade, produto, preco))

  def adicionar_ao_pedido(self, event=None):
      
      indice = self.tree_produtos.selection()
      print('verificando indice:', indice)

      if self.item_existe(indice[0]):
        return
      if not indice:
        messagebox.showerror('Nada selecionado', 'Selecione um item para adicionar!')
        return
      
      item = self.tree_produtos.item(indice[0])
      print(item['values'])

      produto = item['values'][0]
      preco = item['values'][1]

      self.pedido.append({'IID': indice[0] ,'quantidade': 1, 'produto': produto, 'preco': preco})
      self.atualizar_lista_pedido()
      print(self.pedido)

      self.calculo_total()

  def remover_do_pedido(self, event=None):
      indice_lista = self.tree_pedido.selection()[0]
      indice = self.tree_pedido.item(indice_lista)['values'][0]
      print('verificando indice:', indice)
      if indice:
        for item in self.pedido:
          if item['IID'] == indice:
            selecionado = f'{item["quantidade"]} - {item["produto"]} - R$ {item["preco"]}'
            break
        
        print(f'adicionando: {selecionado}')
        to_remove = messagebox.askyesno('Remover Item', f'Deseja remover: {selecionado}')
        print('item: ', to_remove)
        if to_remove:
          for index, item in enumerate(self.pedido):
            
            if item['IID'] == indice:
              self.pedido.pop(index)
              break
      else:
        messagebox.showerror('Nada selecionado', 'Selecione um item para adicionar!')

      self.calculo_total()

  def adicionar_produto(self, event=None):

    nome_produto = simpledialog.askstring("Nome do Produto", "PRODUTO",
                                parent=self.root)
    
    preco_produto = simpledialog.askfloat("Preco do Produto", "PRECO", parent=self.root)
    print(type(nome_produto))

    if nome_produto and preco_produto:
      if self.controller.adicionar_produto(nome_produto, preco_produto):
         self.atualizar_lista_menu()
         print(f'dados preenchidos, depois logica para adicionar produtos. aqui os dados: {nome_produto}, {preco_produto}')

  def item_existe(self, index):
     for item in self.pedido:
      if item['IID'] == index:
        item['quantidade'] += 1
        self.calculo_total()
        return True

     return False
      
  def calculo_total(self):
    self.atualizar_lista_pedido()
    self.total_pedido = 0
    for item in self.pedido:
      iid, quantidade, produto, preco = item.values()
      valor = quantidade * float(preco)
      self.total_pedido+= valor
    
    self.label_total.config(text=f'TOTAL: {self.total_pedido}')
    self.label_total.update_idletasks() 
    
  def emitir_recibo(self, event=None):
    modal = Recibo(self.root, self.pedido, title='RECIBO', total=self.total_pedido)
    self.root.wait_window(modal)
    self.encerrar_pedido()
  
  def encerrar_pedido(self):
    self.pedido = []
    self.total_pedido = 0
    self.calculo_total()
  def toggle_fullscreen(self, event):
    self.isFullscreen = not self.isFullscreen
    self.root.attributes('-fullscreen', self.isFullscreen)
    return "break"
  
  def end_fullscreen(self, event):
    self.isFullscreen = False
    self.root.attributes('-fullscreen', self.isFullscreen)
    return "break"