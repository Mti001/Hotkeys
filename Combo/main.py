import pyautogui
import keyboard
import time

def capturar_posicion():
	print(pyautogui.position())
	#x,y = pyautogui.position()
	#pyautogui.mouseDown(x, y, button="left")
	#pyautogui.moveTo(x+20,y+20)
	#pyautogui.mouseUp(x+40, y+40)
	#pyautogui.mouseDown(x+40, y+40, button="left")
	#pyautogui.moveTo(x+60,y+60)

def pri_hot():
	x,y = 888, 420
	keyboard.send("1") #Presiona 1
	pyautogui.moveTo(x, y) # Mueve el cursor a las coordenadas x e y
	pyautogui.mouseDown(x, y, button="left") # Mantiene presionado el boton izquierdo del raton
	time.sleep(1) # Este sirve para dejarlo un segundo presionado
	pyautogui.mouseUp(x, y) # Deja de presionar el boton izquierdo 

	x,y = 1038, 361
	keyboard.send("3")
	for i in range(4):
		keyboard.send("x")
	pyautogui.moveTo(x, y)
	pyautogui.mouseDown(x, y, button="left")
	time.sleep(1.1899)
	pyautogui.mouseUp(x, y)

	x,y = 895, 404
	keyboard.send("5")
	keyboard.send("c")
	pyautogui.moveTo(x, y)
	pyautogui.mouseDown(x, y, button="left")
	time.sleep(1)
	pyautogui.mouseUp(x, y)

def seg_hot():
	pass

keyboard.add_hotkey("f1", lambda:capturar_posicion())
keyboard.add_hotkey("f2", lambda:pri_hot())
keyboard.add_hotkey("f3", lambda:seg_hot())
keyboard.wait("end")


#pri_hot() (888, y=420)
#seg_hot() (1038, 361)
#Diferencia (+150, -59)
