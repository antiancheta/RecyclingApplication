#!/usr/bin/python3
import tkinter
from tkinter.constants import *
import time

tk = tkinter.Tk()
tk.title("Recycling Application")
tk.call('wm', 'iconphoto', tk._w, tkinter.PhotoImage(file='pic.ico'))

frame = tkinter.Frame(tk, borderwidth=50,background="#42f486")
frame.pack(fill=BOTH,expand=2)

label = tkinter.Label(frame, font="Ubuntu", text="Recycling Application",bg="#42f486",fg="#232624")
label.pack(side=TOP, expand=2)

class Recyclable:
	def __init__(self):
		self.glassAmount = 0
		self.plasticAmount = 0
		self.aluminumAmount = 0
		self.amountCollected = 0.00
		self.totalAmount = 0
	def glass(self):
		self.glassAmount = self.glassAmount + 1
		self.amountCollected += 0.05
		self.totalAmount = self.totalAmount + 1
		print("Added a glass recyclable\n")
		time.sleep(1.25)
		print("Glass Amount: " + str(self.glassAmount) + "\nTotal Amount: " + str(self.totalAmount) + "\nDinero Collected: " + str(self.amountCollected))
	def plastic(self):
		self.plasticAmount = self.plasticAmount + 1
		self.amountCollected = self.amountCollected + 0.05
		self.totalAmount = self.totalAmount + 1
		print("Added a plastic recyclable\n")
		time.sleep(1.25)
		print("Plastic Amount: " + str(self.plasticAmount) + "\nTotal Amount: " + str(self.totalAmount) + "\nDinero Collected: " + str(self.amountCollected))
	def aluminum(self):
		self.aluminumAmount = self.aluminumAmount + 1
		self.amountCollected = self.amountCollected + 0.05
		self.totalAmount = self.totalAmount + 1
		print("Added an aluminum recyclable\n")
		time.sleep(1.25)
		print("Aluminum Amount: " + str(self.aluminumAmount) + "\nTotal Amount: " + str(self.totalAmount) + "\nDinero Collected: " + str(self.amountCollected))

boi = Recyclable()

def glassRecycle():
	boi.glass()

def plasticRecycle():
	boi.plastic()

def aluminumRecycle():
	boi.aluminum()

def byebye():
	print("\n\nThank you for recycling!\n\n")
	tk.destroy()

button2 = tkinter.Button(frame, font="Ubuntu", text="Glass Recyclable",command=glassRecycle,bg="#42f486",fg="#232624",highlightcolor="#232624",highlightbackground="#232624",activebackground="#232624")
button2.pack(expand=1)

button3 = tkinter.Button(frame, font="Ubuntu", text="Plastic Recycle",command=plasticRecycle,bg="#42f486",fg="#232624",highlightcolor="#232624",highlightbackground="#232624",activebackground="#232624")
button3.pack(expand=1)

button4 = tkinter.Button(frame, font="Ubuntu", text="Aluminum Recycle",command=aluminumRecycle,bg="#42f486",fg="#232624",highlightcolor="#232624",highlightbackground="#232624",activebackground="#232624")
button4.pack(expand=1)

button = tkinter.Button(frame, font="Ubuntu", text="Quit",command=byebye,bg="#42f486",fg="#232624",highlightcolor="#232624",highlightbackground="#232624",activebackground="#232624")
button.pack(side=BOTTOM)

tk.mainloop()
