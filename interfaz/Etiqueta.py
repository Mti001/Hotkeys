class Etiqueta:
	def __init__(self):
		self.texto = None
		self.columna = None
		self.fila = None


	def crear_etiquetas(self, marco):
		print("creando etiquetas")
		from tkinter import Label
		#Titulo
		titulo_guardar_hot = Label(marco, text="Guardar Hotkey", font=("Arial",24))
		titulo_guardar_hot.grid(row=0, column=0, columnspan=2)

		titulo_cargar = Label(marco, text="Cargar", font=("Arial",24))
		titulo_cargar.grid(row=0, column=3, columnspan=4)

		titulo_guardar_combo = Label(marco, text="Guardar Combo", font=("Arial",24))
		titulo_guardar_combo.grid(row=10, column=0, columnspan=2)

		#Etiquetas Guardar 
		etiqueta1 = Label(marco, text="Codigo de mapa: ")
		etiqueta1.grid(row=1, column=0)

		etiqueta2 = Label(marco, text="Tipo de Cañon: ")
		etiqueta2.grid(row=2, column=0)

		etiqueta3 = Label(marco, text="Sentido del giro: ")
		etiqueta3.grid(row=3, column=0)

		etiqueta4 = Label(marco, text="Cantidad de giros: ")
		etiqueta4.grid(row=4, column=0)

		etiqueta5 = Label(marco, text="Posicion en x: ")
		etiqueta5.grid(row=5, column=0)

		etiqueta6 = Label(marco, text="Posicion en y: ")
		etiqueta6.grid(row=6, column=0)

		#Etiqueta cargar
		etiqueta8 = Label(marco, text="Codigo de mapa: ")
		etiqueta8.grid(row=1, column=3)

		#Etiqueta crear combo
		etiqueta9 = Label(marco, text="Codigo de mapa: ")
		etiqueta9.grid(row=11, column=0)

		etiqueta10 = Label(marco, text="ID Hotkey 1: ")
		etiqueta10.grid(row=12, column=0)

		etiqueta11 = Label(marco, text="ID Hotkey 2: ")
		etiqueta11.grid(row=13, column=0)