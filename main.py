import tkinter as tk

class App:
  def __init__(self):
    self.root = tk.Tk()
    self.root.geometry('500x500')
    self.root.title('APP - Sabor Rapido')

    self.frame = tk.Frame(self.root)
    self.frame.grid()
    
    self.root.mainloop()    

if __name__ == '__main__':
  app = App()