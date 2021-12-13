class App:
	def crear_app(self):
		from interfaz.Raiz import Raiz
		from interfaz.Marco import Marco
		from interfaz.Etiqueta import Etiqueta
		from interfaz.VariableControl import VariableControl
		from interfaz.Entrada import Entrada
		from interfaz.BotonVerificador import BotonVerificador
		from interfaz.Boton import Boton

		objeto_raiz = Raiz()
		objeto_marco = Marco()
		objeto_etiqueta = Etiqueta()
		objeto_var_control = VariableControl()
		objeto_entrada = Entrada()
		objeto_boton_verificador = BotonVerificador()
		objeto_boton = Boton()

		mi_raiz = objeto_raiz.crear_raiz()
		mi_marco = objeto_marco.crear_marco(mi_raiz)
		mi_etiqueta = objeto_etiqueta.crear_etiquetas(mi_marco)
		mi_var_control = objeto_var_control.crear_var_control()
		mi_entrada = objeto_entrada.crear_entradas(mi_marco, mi_var_control)
		mi_boton_verificador = objeto_boton_verificador.crear_botones_vrf(mi_marco, mi_var_control)
		mi_boton = objeto_boton.crear_botones(mi_marco, mi_var_control)

		mi_raiz.mainloop()