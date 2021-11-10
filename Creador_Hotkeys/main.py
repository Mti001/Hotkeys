from tkinter import *
from tkinter import messagebox
import keyboard
import pyautogui
from io import open
import time
import mouse


#-------------------------------------Usuario---------------------------------------
def obtener_posicion():
	x, y = pyautogui.position()
	posicion_x.set(str(x))
	posicion_y.set(str(y))
	

def guardar_hot_archivo(cod_mapa_guardar_hot, tipo_canon, sentido_giro, cantidad_giros, posicion_x, posicion_y, girar_con_ctrl, mantener_presionado):
	archivo_mapa = cod_mapa_guardar_hot + ".txt" #@123.txt
	archivo = open(archivo_mapa, "a+") #Abrir el archivo en modo añadir y lectura
	archivo.seek(0) #Movemos el puntero al principio 
	cant_hotkeys = len(archivo.readlines()) #Leemos los combos por linea y lo guardamos en una lista. Luego obtenemos la longitud de la lista
	id_hotkey = str(cant_hotkeys + 1) #Asignamos una id al hotkey. De acuerdo a su posicion o número de linea
	girar_con_ctrl = str(girar_con_ctrl) #Convertimos el estado del boton de verificacion a str
	mantener_presionado = str(mantener_presionado)
	archivo.write(cod_mapa_guardar_hot + "," + tipo_canon + "," + sentido_giro + "," + cantidad_giros + "," + posicion_x + "," + posicion_y + "," + girar_con_ctrl + "," + mantener_presionado + "," + id_hotkey + "\n") 
	archivo.close() #Cerramos el archivo en memoria

def guardar_combo_archivo(cod_mapa_guardar_combo, id_hotkey1, id_hotkey2):
	archivo_mapa = cod_mapa_guardar_combo + ".txt" #@123.txt
	archivo = open(archivo_mapa, "a+")
	archivo.seek(0)
	cant_hotkeys = len(archivo.readlines())
	id_combo = str(cant_hotkeys + 1)
	archivo.write(cod_mapa_guardar_combo + "," + id_hotkey1 + "," + id_hotkey2 + "," + id_combo + "\n") 
	archivo.close() #Cerramos el archivo en memoria

def capturar_pos():
	keyboard.unhook_all()
	keyboard.add_hotkey("f1", lambda:obtener_posicion())


def ejecutar_combo(lista_combo, tecla):
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
			for i in range(cantidad_giros):
				keyboard.press("ctrl")
				mouse.wheel(sentido_giro)
				keyboard.release("ctrl")
		else:
			for i in range(cantidad_giros):
				keyboard.send(sentido_giro)

	#Posicion
	pyautogui.moveTo(posicion_x, posicion_y)

	#Mantener presionado
	if mantener_presionado == 1:
		pyautogui.mouseDown(posicion_x, posicion_y, button="left") #Mantener presionado el boton izquierdo del mouse
		time.sleep(1.02) #Tiempo de presion del boton izquierdo del mouse
		pyautogui.mouseUp(posicion_x, posicion_y) #Dejar de presionar

def elegir_combo(lista_combo):
	keyboard.unhook_all()
	keyboard.add_hotkey("f1", lambda:ejecutar_combo(lista_combo, 0))
	keyboard.add_hotkey("f2", lambda:ejecutar_combo(lista_combo, 1))

def cargar_combo(codigo_mapa_cargar):
	archivo_mapa = codigo_mapa_cargar + ".txt"
	archivo = open(archivo_mapa, "r")
	lista_combo = archivo.readlines()
	archivo.close()

	elegir_combo(lista_combo)


#----------------------------------------------------Interfaz-------------------------------------------------------------
#Ventana
raiz = Tk()
raiz.title("Generador de combos")

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

#Frame
marco = Frame(raiz)
marco.pack()
marco.config(width = 700, height = 700)#, bg="Lightblue")


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


#Entradas guardar hotkey
entrada1 = Entry(marco, textvariable=cod_mapa_guardar_hot)
entrada1.grid(row=1, column=1)		

entrada2 = Entry(marco, textvariable=tipo_canon)
entrada2.grid(row=2, column=1)		

entrada3 = Entry(marco, textvariable=sentido_giro)
entrada3.grid(row=3, column=1)		

entrada4 = Entry(marco, textvariable=cant_giros)
entrada4.grid(row=4, column=1)	

entrada5 = Entry(marco, textvariable=posicion_x)
entrada5.grid(row=5, column=1)	

entrada6 = Entry(marco, textvariable=posicion_y)
entrada6.grid(row=6, column=1)	

#Entrada cargar
entrada7 = Entry(marco, textvariable=cod_mapa_cargar)
entrada7.grid(row=1, column=4, padx=5)	

#Entradas guardar combo
entrada8 = Entry(marco, textvariable=cod_mapa_guardar_combo)
entrada8.grid(row=11, column=1)	

entrada9 = Entry(marco, textvariable=id_hotkey1)
entrada9.grid(row=12, column=1)	

entrada10 = Entry(marco, textvariable=id_hotkey2)
entrada10.grid(row=13, column=1)	

#Botones de verificación
boton_vrf = Checkbutton(marco, text="Ctrl+Rueda", variable=girar_con_ctrl)
boton_vrf.grid(row=7, column=0)

boton_vrf2 = Checkbutton(marco, text="Presionado", variable=mantener_presionado)
boton_vrf2.grid(row=8, column=0)


#Funciones
def presionar_guardar_hot():
	guardar_hot_archivo(cod_mapa_guardar_hot.get(), 
		tipo_canon.get(), 
		sentido_giro.get(), 
		cant_giros.get(), 
		posicion_x.get(), 
		posicion_y.get(), 
		girar_con_ctrl.get(),
		mantener_presionado.get())
	messagebox.showinfo("Guardado",f"Se ha guardado el hotkey correctamente")

def presionar_guardar_combo():
	print(cod_mapa_guardar_combo.get(), id_hotkey1.get(), id_hotkey2.get())
	guardar_combo_archivo(cod_mapa_guardar_combo.get(), id_hotkey1.get(), id_hotkey2.get())
	messagebox.showinfo("Guardado",f"Se ha guardado el combo correctamente")

def presionar_capturar():
	capturar_pos()

def presionar_cargar():
	cargar_combo(cod_mapa_cargar.get())

#Botones
boton_capturar = Button(marco, text="Capturar", command=presionar_capturar)
boton_capturar.grid(row=9, column=0, pady=5)

#Guardar hotkey
boton_guardar_hotkey = Button(marco, text="Guardar", command=presionar_guardar_hot)
boton_guardar_hotkey.grid(row=9, column=1, pady=5)

#Guardar combo
boton_guardar_combo = Button(marco, text="Guardar", command=presionar_guardar_combo)
boton_guardar_combo.grid(row=14, column=1, pady=5)

boton_cargar = Button(marco, text="Cargar", command=presionar_cargar)
boton_cargar.grid(row=2, column=4)



raiz.mainloop()

