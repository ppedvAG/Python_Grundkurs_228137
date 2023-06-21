# Module in Python
# Sind Libraries die zusätzliche Funktionalitäten in unseren Code einbinden können
# Beschäftigen sich generell mit einem Thema
# Müssen importiert und/oder installiert werden

# Wie importiere ich Module?
# Syntax:
# import <Modulname>
# from <Modulname> import <Name der Funktion>
# zusätzlich kann auch ein Alias vergeben mit as <Alias>

import datetime  # Zum Arbeiten mit Datumswerten
import os  # Generelle Informationen zur Umgebung
from turtle import *  # Funktionen des turtle Skripts in unser Skript integrieren

# color('red', 'yellow')
# begin_fill()
# while True:
#     forward(400)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()

# import turtle  # Funktionen des turtle Skripts extern belassen, müssen über den Modulnamen aufgerufen werden
#
# turtle.color('red', 'yellow')
# turtle.begin_fill()
# while True:
#     turtle.forward(400)
#     turtle.left(170)
#     if abs(pos()) < 1:
#         break
# turtle.end_fill()
# turtle.done()

# import turtle as t
#
# t.color('red', 'yellow')
# t.begin_fill()
# while True:
#     t.forward(400)
#     t.left(170)
#     if abs(pos()) < 1:
#         break
# t.end_fill()
# t.done()

def countCase(text: str):
	lower, upper, special = 0, 0, 0
	for char in text:
		if char.islower():
			lower += 1
		elif char.isupper():
			upper += 1
		else:
			special += 1
	print(f"Sonderzeichen: {special} | Groß: {upper} | Klein: {lower}")

def calcTax(price):
	return price * 1.2

if __name__ == "__main__":
	print("Das ist die Hauptfunktion von M008")