class Hotkey:
	def obtener_posicion(self, diccionario_var_control):
		print("evento ejecutado")
		import pyautogui

		x, y = pyautogui.position()
		print(x,y)
		diccionario_var_control["posicion_x"].set(str(x))
		diccionario_var_control["posicion_y"].set(str(y))
	

	def guardar_hot_archivo(self,cod_mapa_guardar_hot, tipo_canon, sentido_giro, cantidad_giros, posicion_x, posicion_y, girar_con_ctrl, mantener_presionado):
		archivo_mapa = cod_mapa_guardar_hot + ".txt" #@123.txt
		archivo = open(archivo_mapa, "a+") #Abrir el archivo en modo añadir y lectura
		archivo.seek(0) #Movemos el puntero al principio 
		cant_hotkeys = len(archivo.readlines()) #Leemos los combos por linea y lo guardamos en una lista. Luego obtenemos la longitud de la lista
		id_hotkey = str(cant_hotkeys + 1) #Asignamos una id al hotkey. De acuerdo a su posicion o número de linea
		girar_con_ctrl = str(girar_con_ctrl) #Convertimos el estado del boton de verificacion a str
		mantener_presionado = str(mantener_presionado)
		archivo.write(cod_mapa_guardar_hot + "," + tipo_canon + "," + sentido_giro + "," + cantidad_giros + "," + posicion_x + "," + posicion_y + "," + girar_con_ctrl + "," + mantener_presionado + "," + id_hotkey + "\n") 
		archivo.close() #Cerramos el archivo en memoria

	def guardar_combo_archivo(self,cod_mapa_guardar_combo, id_hotkey1, id_hotkey2):
		archivo_mapa = cod_mapa_guardar_combo + ".txt" #@123.txt
		archivo = open(archivo_mapa, "a+")
		archivo.seek(0)
		cant_hotkeys = len(archivo.readlines())
		id_combo = str(cant_hotkeys + 1)
		archivo.write(cod_mapa_guardar_combo + "," + id_hotkey1 + "," + id_hotkey2 + "," + id_combo + "\n") 
		archivo.close() #Cerramos el archivo en memoria

	def capturar_pos(self, diccionario_var_control):
		print("esperando evento")
		import keyboard

		keyboard.unhook_all()
		keyboard.add_hotkey("f1", lambda:self.obtener_posicion(diccionario_var_control))


	def ejecutar_combo(self, lista_combo, tecla):
		import keyboard

		#Quitamos los saltos de linea y comas
		combo = lista_combo[tecla].split()
		combo = combo[0].split(",")
		
		#variables
		codigo_mapa = combo[0]
		tipo_canon = combo[1]
		sentido_giro = combo[2]
		cantidad_giros = int(combo[3])
		posicion_x = int(combo[4])
		posicion_y = int(combo[5])
		girar_con_ctrl = int(combo[6])
		mantener_presionado = int(combo[7])

		#Tipo de cañon
		keyboard.send(tipo_canon)

		#Sentido de giro
		if sentido_giro != "0":
			if girar_con_ctrl == 1: 
				sentido_giro = int(sentido_giro)
				for i in range(cantidad_giros): #180 giros con ctrl. 45 de un sentido a otro
					keyboard.press("ctrl")
					mouse.wheel(sentido_giro)
					keyboard.release("ctrl")
			else:
				for i in range(cantidad_giros): #24 giros sin ctrl. 6 de un sentido a otro
					keyboard.send(sentido_giro)

		#Posicion
		if posicion_x != 0 and posicion_y != 0:
			pyautogui.moveTo(posicion_x, posicion_y)

		#Mantener presionado
		if mantener_presionado == 1:
			pyautogui.mouseDown(posicion_x, posicion_y, button="left") #Mantener presionado el boton izquierdo del mouse
			time.sleep(1.02) #Tiempo de presion del boton izquierdo del mouse
			pyautogui.mouseUp(posicion_x, posicion_y) #Dejar de presionar

	def elegir_combo(self,lista_combo):
		import keyboard
		keyboard.unhook_all()
		keyboard.add_hotkey("f1", lambda:self.ejecutar_combo(lista_combo, 0))
		keyboard.add_hotkey("f2", lambda:self.ejecutar_combo(lista_combo, 1))
		keyboard.add_hotkey("f3", lambda:self.ejecutar_combo(lista_combo, 2))
		keyboard.add_hotkey("f4", lambda:self.ejecutar_combo(lista_combo, 3))

	def cargar_combo(self,codigo_mapa_cargar):
		archivo_mapa = codigo_mapa_cargar + ".txt"
		archivo = open(archivo_mapa, "r")
		lista_combo = archivo.readlines()
		archivo.close()
		self.elegir_combo(lista_combo)