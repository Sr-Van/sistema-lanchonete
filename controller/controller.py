
class Controller:
  def __init__(self, db):
    self.db = db

  def adicionar_produto(self, produto, preco):
    if self.db.insert_product(produto, preco):
      return True
  def pegar_produtos(self):
    lista_prod = self.db.get_products()
    dicionario = {}
    for i in range(len(lista_prod)):
      dicionario[lista_prod[i][0]] = lista_prod[i][1]
    
    return dicionario
