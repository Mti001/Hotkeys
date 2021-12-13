class BotonVerificador:
	def __init__(self):
		self.texto = None
		self.columna = None
		self.fila = None

	def crear_botones_vrf(self, marco, diccionario_var_control):
		print("creando botones de verificacion")
		from tkinter import Checkbutton

		#Botones de verificación
		boton_vrf = Checkbutton(marco, text="Ctrl+Rueda", variable=diccionario_var_control["girar_con_ctrl"])#girar_con_ctrl
		boton_vrf.grid(row=7, column=0)

		boton_vrf2 = Checkbutton(marco, text="Presionado", variable=diccionario_var_control["mantener_presionado"])#mantener_presionado
		boton_vrf2.grid(row=8, column=0)
