import sqlite3

class Database:
  def __init__(self, conn):
    self.conn = conn
    self.cursor = self.conn.cursor()
    print("Conexão com o banco de dados estabelecida com sucesso!")
    self.create_table()

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
      return True
    except Exception as e:
      print(e)
      return False

  def get_products(self):
    try:
      self.cursor.execute("SELECT produto, preco FROM produtos")
      return self.cursor.fetchall()

    except sqlite3.Error as e:
      print(f'Erro ao buscar produtos: {e}')