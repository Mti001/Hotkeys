class Boton:
	def __init__(self):
		self.texto = None
		self.columna = None
		self.fila = None
		self.separacion_x = None
		self.separacion_y = None

	#Funciones

	def presionar_guardar_hot(self, diccionario_var_control):
		print("presionaste guardar hotkey")

		from tkinter import messagebox
		from clases.Hotkey import Hotkey

		objeto_hotkey = Hotkey()
		objeto_hotkey.guardar_hot_archivo(diccionario_var_control["cod_mapa_guardar_hot"].get(), 
			diccionario_var_control["tipo_canon"].get(), 
			diccionario_var_control["sentido_giro"].get(), 
			diccionario_var_control["cant_giros"].get(), 
			diccionario_var_control["posicion_x"].get(), 
			diccionario_var_control["posicion_y"].get(), 
			diccionario_var_control["girar_con_ctrl"].get(),
			diccionario_var_control["mantener_presionado"].get())
		messagebox.showinfo("Guardado",f"Se ha guardado el hotkey correctamente")

	def presionar_guardar_combo():
		print("presionaste guardar combo")

		from tkinter import showinfo
		from clases.Hotkey import Hotkey

		objeto_hotkey = Hotkey()
		objeto_hotkey.guardar_combo_archivo(diccionario_var_control["cod_mapa_guardar_combo"].get(), 
			diccionario_var_control["id_hotkey1"].get(), 
			diccionario_var_control["id_hotkey2"].get())
		messagebox.showinfo("Guardado",f"Se ha guardado el combo correctamente")

	def presionar_capturar(self, diccionario_var_control):
		print("presionaste capturar")

		from clases.Hotkey import Hotkey

		objeto_hotkey = Hotkey()
		objeto_hotkey.capturar_pos(diccionario_var_control)

	def presionar_cargar(self, diccionario_var_control):
		print("presionaste cargar")

		from clases.Hotkey import Hotkey
		objeto_hotkey = Hotkey()
		objeto_hotkey.cargar_combo(diccionario_var_control["cod_mapa_cargar"].get())


	def crear_botones(self, marco, diccionario_var_control):
		print("creando botones")

		from tkinter import Button
		#Botones
		boton_capturar = Button(marco, text="Capturar", command=lambda:self.presionar_capturar(diccionario_var_control))
		boton_capturar.grid(row=9, column=0, pady=5)

		#Guardar hotkey
		boton_guardar_hotkey = Button(marco, text="Guardar", command=lambda:self.presionar_guardar_hot(diccionario_var_control))
		boton_guardar_hotkey.grid(row=9, column=1, pady=5)

		#Guardar combo
		boton_guardar_combo = Button(marco, text="Guardar", command=self.presionar_guardar_combo)
		boton_guardar_combo.grid(row=14, column=1, pady=5)

		boton_cargar = Button(marco, text="Cargar", command=lambda:self.presionar_cargar(diccionario_var_control))
		boton_cargar.grid(row=2, column=4)
