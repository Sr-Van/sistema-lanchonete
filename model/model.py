import sqlite3


class Database:
  def __init__(self, db_name):
    self.conn = sqlite3.connect(db_name)
    self.cursor = self.conn.cursor()
    self.create_table()
    self.insert_product('Coca-Cola', 5.99)
    self.insert_product('Fanta', 5.99)
    self.insert_product('Guarana', 5.99)
    self.insert_product('Sprite', 5.99)
    print(self.get_products())
    self.conn.close()

  def create_table(self):
    try:
      self.cursor.execute(f'''CREATE TABLE IF NOT EXISTS produtos (
                              id INTEGER PRIMARY KEY AUTOINCREMENT,
                              produto TEXT NOT NULL,
                              preco REAL NOT NULL)''')
    
      self.conn.commit()
      print("Tabela criada com sucesso!")
    except Exception as e:
      print(e)

  def insert_product(self, produto, preco):
    try:
      self.cursor.execute("INSERT INTO produtos (produto, preco) VALUES (:produto, :preco)", {"produto": produto, "preco": preco})
      self.conn.commit()
      print("Produto inserido com sucesso!")
    except Exception as e:
      print(e)

  def get_products(self):
    try:
      self.cursor.execute("SELECT produto, preco FROM produtos")
      lista_produtos = self.cursor.fetchall()
      dicionario = {}
      for i in range(len(lista_produtos)):
        dicionario[lista_produtos[i][0]] = lista_produtos[i][1]

      return dicionario

    except sqlite3.Error as e:
      print(f'Erro ao buscar produtos: {e}')
if __name__ == "__main__":
  db = Database('./database.db')
