from tkinter import *
from Usuario import Usuario
from tkinter import messagebox
def crear_interfaz():

	#Ventana
	raiz = Tk()
	raiz.title("Generador de combos")

	#Variables de control
	codigo_mapa_guardar = StringVar()
	codigo_mapa_cargar = StringVar()
	tipo_canon = StringVar()
	sentido_giro = StringVar()
	cantidad_giros = StringVar()
	posicion_x = StringVar()
	posicion_y = StringVar()

	#Frame
	marco = Frame(raiz)
	marco.pack()
	marco.config(width = 700, height = 700)#, bg="Lightblue")


	#Titulo
	titulo_guardar = Label(marco, text="Guardar", font=("Arial",24))
	titulo_guardar.grid(row=0, column=0, columnspan=2)

	titulo_cargar = Label(marco, text="Cargar", font=("Arial",24))
	titulo_cargar.grid(row=0, column=2, columnspan=4)


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

	etiqueta8 = Label(marco, text="Codigo de mapa: ")
	etiqueta8.grid(row=1, column=2)

	#Entradas
	entrada1 = Entry(marco, textvariable=codigo_mapa_guardar)
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

	entrada7 = Entry(marco, textvariable=codigo_mapa_cargar)
	entrada7.grid(row=1, column=3)	

	#Funciones
	def crear_hot():
		estado = True
		if tipo_canon.get().isalpha():
		 	messagebox.showerror("Error", "En el tipo de cañon debes ingresar un número")
		 	estado = False
		elif int(tipo_canon.get()) < 0 and int(tipo_canon.get()) > 9:
				messagebox.showerror("Error", "En el tipo de cañon debes ingresar un número del 0 al 9")
				estado = False

		elif sentido_giro.get() != "x" and sentido_giro.get() != "z" and sentido_giro.get() != "0":
			messagebox.showerror("Error", "En el sentido del giro debes ingresar una 'x' o una 'z'. Si el cañon no va a girar ingresa un 0")
			estado = False

		elif cantidad_giros.get().isnumeric() != True:
			messagebox.showerror("Error", "En la cantidad de giros debes ingresar un número")	
			estado = False

		elif posicion_x.get().isalpha():
			messagebox.showerror("Error", "La posicion en 'x' debe ser un número")
			estado = False

		elif posicion_y.get().isnumeric() != True:
			messagebox.showerror("Error", "La posicion en 'y' debe ser un número")
			estado = False

		else:
			usuario1.guardar_combo(codigo_mapa_guardar.get(), tipo_canon.get(), sentido_giro.get(), cantidad_giros.get(), posicion_x.get(), posicion_y.get())
			messagebox.showinfo("Guardado",f"Se ha creado el cañon correctamente")

	def capturar_pos():
		usuario1.capturar_pos()

	def cargar_combo():
		usuario1.cargar_combo(codigo_mapa_cargar.get())

	#Botones
	boton_capturar = Button(marco, text="Capturar", command=capturar_pos)
	boton_capturar.grid(row=7, column=0)

	boton_crear = Button(marco, text="Guardar", command=crear_hot)
	boton_crear.grid(row=7, column=1)

	boton_cargar = Button(marco, text="Cargar", command=cargar_combo)
	boton_cargar.grid(row=2, column=3)

	raiz.mainloop()

if __name__ == "__main__":
	usuario1 = Usuario()
	crear_interfaz()
