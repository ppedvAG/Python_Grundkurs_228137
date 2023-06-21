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

# Übung 1:
# Funktion die dem User die Möglichkeiten (w, r, a) gibt
# User soll eine davon auswählen über input()
# Wenn der User keine valide Möglichkeit eingibt, soll die Eingabe wiederholt werden
# Danach soll einfach das File geöffnet werden

# Funktionsdefinition
# Abfrage der Eingabe des Users
# Überprüfung der Eingabe auf w, r oder a
# Wenn der User w, r oder a eingegeben hat, dann open
# Wenn keine valide Eingabe -> Wiederholen (while True)
def auswahl():
	while True:  # Endlosschleife bis der User etwas korrektes eingibt
		# if choice == "w" or choice == "r" or choice == "a":
		choice = input("Gib w, r oder a ein: ")
		if choice in ["w", "r", "a"]:  # in statt if/or
			break
	print("Valide Eingabe, File wird geöffnet")
	return open("Test.txt", choice)

auswahl()

# Übung 2:
# Erstelle ein Programm, das zwei Integer oder Floats abfragt
# Gib dem Nutzer die Möglichkeit per Tastendruck zwischen Addition, Subtraktion, Multiplikation und Division zu wählen.
# -> Zahl zwischen 1 und 4 -> Rechenoperation auswählen
# Bei Ungültiger Eingabe soll der Benutzer erneut nach seiner Entscheidung gefragt werden.
# Lasse das Ergebnis inklusive der Rechnung in der Konsole ausgeben
# Frage nach Ende der Operation ob der Benutzer eine neue Rechnung durchführen will
