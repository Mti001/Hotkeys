class Raiz:
	def __init__(self):
		self.titulo = "Generador de combos"
		
	def crear_raiz(self):
		print("creando raiz")
		from tkinter import Tk
		raiz = Tk()
		raiz.title(self.titulo)

		return raiz