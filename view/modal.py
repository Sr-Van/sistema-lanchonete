import tkinter
from tkinter import ttk


class Recibo(tkinter.Toplevel):
  def __init__(self, parent, pedido, total,title = None):
    super().__init__(parent)
    self.title(title)
    self.parent = parent
    self.pedido = pedido

    self.largura_modal = 700
    self.altura_modal = 750
    self.largura_tela = self.parent.winfo_screenwidth()
    self.altura_tela = self.parent.winfo_screenheight()
    
    self.pos_x = (self.largura_tela // 2) - (self.largura_modal // 2)
    self.pos_y = (self.altura_tela // 2) - (self.altura_modal // 2)
    
    self.geometry(f'{self.largura_modal}x{self.altura_modal}+{self.pos_x}+{self.pos_y}')

    self.upper_frame = ttk.Frame(self)
    self.upper_frame.pack(expand=True, fill='both', ipadx=10, ipady=10)

    self.lower_frame = ttk.Frame(self)
    self.lower_frame.pack(expand=True, fill='both', ipadx=10, ipady=10)

    self.label_total = ttk.Label(self.lower_frame, text=f'TOTAL: {total}', font=('Arial', 16))
    self.label_total.pack(padx=10, pady=10, expand=True, fill='both')

    self.button_ok = ttk.Button(self.lower_frame, text='Confirmar pagamento', command=self.destroy)
    self.button_ok.pack(padx=10, pady=10, expand=True, fill='both')
    
    
    self.grab_set()
    self.focus_set()
    self.show_info()

  def show_info(self):
    tree = ttk.Treeview(self.upper_frame, columns=('quantidade', 'pedido', 'valor'), show='headings')
    tree.pack(expand=True, fill='both', ipadx=10, ipady=10)

    tree.heading('quantidade', text='Quantidade')
    tree.heading('pedido', text='Pedido')
    tree.heading('valor', text='Valor')

    for item in self.pedido:
      iid, quantidade, produto, preco = item.values()
      tree.insert("", tkinter.END, values=(quantidade, produto, preco))


class Novo(tkinter.Toplevel):
  def __init__(self, parent, controller,title = None):
    super().__init__(parent)
    self.title(title)
    self.parent = parent
    self.controller = controller

    self.frame = ttk.Frame(self)
    self.frame.pack(expand=True, fill='both', ipadx=10, ipady=10)

    self.grab_set()
    self.focus_set()

    self.largura_modal = 500
    self.altura_modal = 300
    self.largura_tela = self.parent.winfo_screenwidth()
    self.altura_tela = self.parent.winfo_screenheight()
    
    self.pos_x = (self.largura_tela // 2) - (self.largura_modal // 2)
    self.pos_y = (self.altura_tela // 2) - (self.altura_modal // 2)
    
    self.geometry(f'{self.largura_modal}x{self.altura_modal}+{self.pos_x}+{self.pos_y}')

    self.label_produto = ttk.Label(self.frame, text='Nome produto', font=('Arial', 16))
    self.label_produto.pack(padx=10, pady=10, expand=True, fill='both')

    self.entry_produto = ttk.Entry(self.frame, font=('Arial', 16))
    self.entry_produto.pack(padx=10, pady=10, expand=True, fill='both')
    self.entry_produto.focus_set()

    self.label_preco = ttk.Label(self.frame, text='Preço', font=('Arial', 16))
    self.label_preco.pack(padx=10, pady=10, expand=True, fill='both')

    self.entry_preco = ttk.Entry(self.frame, font=('Arial', 16))
    self.entry_preco.pack(padx=10, pady=10, expand=True, fill='both')

    self.button_ok = ttk.Button(self.frame, text='Confirmar', command=self.salvar_produto)
    self.button_ok.pack(padx=10, pady=10, expand=True, fill='both')

  def salvar_produto(self):
    print('dados preenchidos, depois logica para adicionar produtos. aqui os dados:', self.entry_produto.get(), self.entry_preco.get())
    if self.controller.adicionar_produto(self.entry_produto.get(), float(self.entry_preco.get())):
      print('adicionado com sucesso')
      self.destroy()


