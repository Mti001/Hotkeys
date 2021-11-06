from tkinter import *
from Usuario import Usuario

def crear_interfaz():

	#Ventana
	raiz = Tk()
	raiz.title("Generador de combos")

	#Variables de control
	codigo_mapa = StringVar("")
	tipo_canon = StringVar("")
	sentido_giro = StringVar("")
	cantidad_giros = StringVar("")
	posicion_x = StringVar("")
	posicion_y = StringVar("")

	#Frame
	marco = Frame(raiz)
	marco.pack()
	marco.config(width = 700, height = 700)#, bg="Lightblue")


	#Titulo
	titulo = Label(marco, text="Generar combo", font=("Arial",24))
	titulo.grid(row=0, column=0, columnspan=2)

	#Etiquetas
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

	#Entradas
	entrada1 = Entry(marco, textvariable=codigo_mapa)
	entrada1.grid(row=1, column=1)		

	entrada2 = Entry(marco, textvariable=tipo_canon)
	entrada2.grid(row=2, column=1)		

	entrada3 = Entry(marco, textvariable=sentido_giro)
	entrada3.grid(row=3, column=1)		

	entrada4 = Entry(marco, textvariable=cantidad_giros)
	entrada4.grid(row=4, column=1)	

	entrada5 = Entry(marco, textvariable=posicion_x)
	entrada5.grid(row=5, column=1)	

	entrada6 = Entry(marco, textvariable=posicion_y)
	entrada6.grid(row=6, column=1)	

	#Funciones
	def crear_hot():
		usuario1.guardar_combo(codigo_mapa.get(), tipo_canon.get(), sentido_giro.get(), cantidad_giros.get(), posicion_x.get(), posicion_y.get())

	def capturar_pos():
		usuario1.capturar_pos()

	def abrir_ventana2():

		#Ventana2
		ventana2 = Toplevel()
		ventana2.title("Combos")

		#Variables de control2
		codigo_mapa2 = StringVar("")

		#Frame2
		marco_ventana2 = Frame(ventana2)
		marco_ventana2.pack()
		marco_ventana2.config(width=700, height=700)

		#Titulo2
		titulo2 = Label(marco_ventana2, text="Combos", font=("Arial",24))
		titulo2.grid(row=0, column=0, columnspan=4)

		#Etiquetas2
		etiqueta_mapa = Label(marco_ventana2, text="Codigo de mapa: ")
		etiqueta_mapa.grid(row=1, column=0, columnspan=2)

		#Entradas
		entrada_mapa = Entry(marco_ventana2, textvariable=codigo_mapa2)
		entrada_mapa.grid(row=1, column=2, columnspan=2)	

		#Funciones2
		def cargar_combo():
			usuario1.cargar_combo(codigo_mapa2.get())
		
		#Botones2
		boton_combos1 = Button(marco_ventana2, text="Combos1")
		boton_combos1.grid(row=3, column=0, ipadx=5, ipady=5, padx=5, pady=5)

		boton_combos2 = Button(marco_ventana2, text="Combos2")
		boton_combos2.grid(row=3, column=1, ipadx=5, ipady=5, padx=5, pady=5)

		boton_combos3 = Button(marco_ventana2, text="Combos3")
		boton_combos3.grid(row=3, column=2, ipadx=5, ipady=5, padx=5, pady=5)

		boton_combos4 = Button(marco_ventana2, text="Combos4")
		boton_combos4.grid(row=3, column=3, ipadx=5, ipady=5, padx=5, pady=5)

		boton_cargar = Button(marco_ventana2, text="Cargar", command=cargar_combo)
		boton_cargar.grid(row=2, column=0, ipadx=5, ipady=5, padx=5, pady=5, columnspan=4)


	#Botones
	boton_capturar = Button(marco, text="Capturar", command=capturar_pos)
	boton_capturar.grid(row=7, column=0, ipadx=5, ipady=5, padx=5, pady=5)

	boton_crear = Button(marco, text="Guardar", command=crear_hot)
	boton_crear.grid(row=7, column=1, ipadx=5, ipady=5, padx=5, pady=5)

	boton_ventana2 = Button(marco, text=">>", command=abrir_ventana2)
	boton_ventana2.grid(row=8, column=0, ipadx=10, ipady=10, padx=10, pady=10, columnspan=2)

	raiz.mainloop()

if __name__ == "__main__":
	usuario1 = Usuario()
	crear_interfaz()
