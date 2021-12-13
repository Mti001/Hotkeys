class Entrada:
	def __init__(self):
		self.variable_texto = None
		self.fila = None
		self.columna = None

	def crear_entradas(self, marco, diccionario_var_control):
		print("creando entradas")
		from tkinter import Entry

		#Entradas guardar hotkey
		entrada1 = Entry(marco, textvariable=diccionario_var_control["cod_mapa_guardar_hot"])
		entrada1.grid(row=1, column=1)		

		entrada2 = Entry(marco, textvariable=diccionario_var_control["tipo_canon"])
		entrada2.grid(row=2, column=1)		

		entrada3 = Entry(marco, textvariable=diccionario_var_control["sentido_giro"])
		entrada3.grid(row=3, column=1)		

		entrada4 = Entry(marco, textvariable=diccionario_var_control["cant_giros"])
		entrada4.grid(row=4, column=1)	

		entrada5 = Entry(marco, textvariable=diccionario_var_control["posicion_x"])
		entrada5.grid(row=5, column=1)	

		entrada6 = Entry(marco, textvariable=diccionario_var_control["posicion_y"])
		entrada6.grid(row=6, column=1)	

		#Entrada cargar
		entrada7 = Entry(marco, textvariable=diccionario_var_control["cod_mapa_cargar"])
		entrada7.grid(row=1, column=4, padx=5)	

		#Entradas guardar combo
		entrada8 = Entry(marco, textvariable=diccionario_var_control["cod_mapa_guardar_combo"])
		entrada8.grid(row=11, column=1)	

		entrada9 = Entry(marco, textvariable=diccionario_var_control["id_hotkey1"])
		entrada9.grid(row=12, column=1)	

		entrada10 = Entry(marco, textvariable=diccionario_var_control["id_hotkey2"])
		entrada10.grid(row=13, column=1)	