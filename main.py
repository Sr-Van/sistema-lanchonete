import sqlite3

from view.view import App
from controller.controller import Controller
from model.model import Database

if __name__ == '__main__':
  conexao = sqlite3.connect('./model/produtos.db')
  db = Database(conexao)
  controlador = Controller(db)
  app = App(controlador)