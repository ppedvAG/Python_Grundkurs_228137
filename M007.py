# Input/Output
from os.path import exists


# Es gibt in Python mehrere Funktion für Ein-/Ausgaben
# print(...)

# input(string)
# Wartet auf den Input vom Benutzer und nimmt diesen Input schreibt diesen in eine Variable
# Programm bleibt stehen bis der User etwas eingegeben hat

def inputTest():
	name = input("Gib deinen Namen ein: ")
	print(f"Dein Name ist: {name}")

	zahl1 = int(input("Gib eine Zahl ein: "))  # mit Typ(Wert) kann ein Wert in einen Typen konvertiert werden
	zahl2 = int(input("Gib eine weitere Zahl ein: "))
	print(f"Die Summe ist: {zahl1 + zahl2}")

# inputTest()

# Escape-Sequenzen
# Erlauben Sonderzeichen die nicht mit der Tastatur getippt werden können in Strings einzubauen
# \n: Zeilenumbruch, \t: Tabulator
text = "Ein Text\n\tZwei Text"
print(text)

# open(string, string)
# Öffnet einen Stream auf die gegebene Datei mit dem gegebenen Modus
# w: Write, Overwrite
# a: Append, kein Overwrite
# r: Read
# x: Create
# r+: Read/Write
# w+: Write, erstellt die Datei neu

# Öffnet das File mit dem gegebenen Dateinamen
file = open("test.txt", "w+")
file.writelines("123\n")  # Inhalt schreiben
file.writelines("456\n")
file.writelines("789\n")
file.close()  # Mit close den Stream schließen

file = open("test.txt", "r")
readText = file.readlines()
print(readText)

# Exists
# Prüfen ob eine Datei bereits existiert
# Kommt von os.path (import)
dateiExistiert = exists("test.txt")
if dateiExistiert:
	print("Datei existiert bereits")
else:
	print("Datei existiert nicht")

# with-Block
# Ermöglicht die automatische Schließung des Streams am Ende des Blocks
# Sollte generell immer gemacht werden
with open("test.txt", "r") as file:
	zeile = 1
	for line in file.readlines():
		print(f"Zeile {zeile}: {line}")
		zeile += 1
# Hier wird automatisch close() ausgeführt

# rstring
# Rawstring
# Erkennt keine Escape-Sequenzen
# Besonders nützlich für Pfade
normal = "C:\\Users\\lk3\\source\\repos\\Python_Grundkurs_2023_06_19"
rstring = r"C:\Users\lk3\source\repos\Python_Grundkurs_2023_06_19"

# Übung:
# Funktion die dem User die Möglichkeiten (w, r, a) gibt
# User soll eine davon auswählen über input()
# Wenn der User keine valide Möglichkeit eingibt, soll die Eingabe wiederholt werden
# Danach soll einfach das File geöffnet werden