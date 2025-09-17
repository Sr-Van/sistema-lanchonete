import sqlite3


class Database:
  def __init__(self):
    self.conn = sqlite3.connect("./database.db")
    self.cursor = self.conn.cursor()
    self.create_table()
    self.cursor.close()
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

if __name__ == "__main__":
  db = Database()
  db.insert_product("Produto 3", 10.99)