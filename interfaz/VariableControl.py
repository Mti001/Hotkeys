class VariableControl:

	def crear_var_control(self):
		from tkinter import StringVar
		from tkinter import IntVar

		#Variables de control 
		cod_mapa_guardar_hot = StringVar()
		cod_mapa_cargar = StringVar()
		tipo_canon = StringVar()
		sentido_giro = StringVar()
		cant_giros = StringVar()
		posicion_x = StringVar()
		posicion_y = StringVar()
		girar_con_ctrl = IntVar()
		mantener_presionado = IntVar()

		cod_mapa_guardar_combo = StringVar()
		id_hotkey1 = StringVar()
		id_hotkey2 = StringVar()

		diccionario_var_control = {
		"cod_mapa_guardar_hot":cod_mapa_guardar_hot, 
		"cod_mapa_cargar":cod_mapa_cargar, 
		"tipo_canon":tipo_canon, 
		"sentido_giro":sentido_giro, 
		"cant_giros":cant_giros, 
		"posicion_x":posicion_x, 
		"posicion_y":posicion_y, 
		"cod_mapa_guardar_combo":cod_mapa_guardar_combo, 
		"id_hotkey1":id_hotkey1, 
		"id_hotkey2":id_hotkey2, 
		"girar_con_ctrl":girar_con_ctrl, 
		"mantener_presionado":mantener_presionado
		}


		return diccionario_var_control