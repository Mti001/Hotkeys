dani feo
import keyboard
import pyautogui
from io import open

class Usuario:
	def obtener_posicion(self):
		print(pyautogui.position())
		
	def guardar_combo(self, codigo_mapa, tipo_canon, sentido_giro, cantidad_giros, posicion_x, posicion_y):
		print("hola")
		archivo_mapa = codigo_mapa + ".txt"
		archivo = open(archivo_mapa, "a")
		archivo.write(codigo_mapa + "-" + tipo_canon + "-" + sentido_giro + "-" + cantidad_giros + "-" + posicion_x + "-" + posicion_y + "\n")
		archivo.close()

	def capturar_pos(self):
		keyboard.unhook_all()
		keyboard.add_hotkey("f1", lambda:self.obtener_posicion())


	def crear_combo(self, lista_combo, tecla):
		#Quitamos los saltos de linea y guiones
		combo = lista_combo[tecla].split()
		combo = combo[0].split("-")

		#variables
		codigo_mapa = combo[0]
		tipo_canon = combo[1]
		sentido_giro = combo[2]
		cantidad_giros = int(combo[3])
		posicion_x = int(combo[4])
		posicion_y = int(combo[5])

		#Tipo de cañon
		keyboard.send(tipo_canon)

		#Sentido de giro
		if sentido_giro != "0":
			if sentido_giro == "x":
				for i in range(cantidad_giros):
					keyboard.send(sentido_giro)
			elif sentido_giro == "z":
				for i in range(cantidad_giros):
					keyboard.send(sentido_giro)

		#Posicion
		pyautogui.moveTo(posicion_x, posicion_y)


	def elegir_combo(self, lista_combo):
		print("combo elegido")
		keyboard.unhook_all()
		keyboard.add_hotkey("f1", lambda:self.crear_combo(lista_combo, 0))
		keyboard.add_hotkey("f2", lambda:self.crear_combo(lista_combo, 1))
		keyboard.add_hotkey("f3", lambda:self.crear_combo(lista_combo, 2))
		keyboard.add_hotkey("f4", lambda:self.crear_combo(lista_combo, 3))
		keyboard.add_hotkey("f5", lambda:self.crear_combo(lista_combo, 4))

	def cargar_combo(self, codigo_mapa2):
		print(codigo_mapa2)
		archivo_mapa = codigo_mapa2 + ".txt"
		archivo = open(archivo_mapa, "r")
		lista_combo = archivo.readlines()
		archivo.close()

		self.elegir_combo(lista_combo)





