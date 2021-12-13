class Marco:
	def __init__(self):
		self.ancho = 700
		self.altura = 700

	def crear_marco(self, raiz):
		print("creando marco")
		from tkinter import Frame
		marco = Frame(raiz)
		marco.pack()
		marco.config(width = self.ancho, height = self.altura)#, bg="Lightblue")
		return marco
