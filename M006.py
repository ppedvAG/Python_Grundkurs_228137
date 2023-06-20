# Funktionen
# Code der wiederverwendet werden kann
# Beispiele: print(...), len(...), str.split(...)

# Wir können auch eigene Funktion definieren
# Funktionen für Wiederverwendbarkeit innerhalb der Codebasis
# Syntax:
# def <Name>(Optional: Parameter1, Parameter2, ...):
# 	Code

def hallo():  # Funktion anlegen mittels def, Funktion werden klein geschrieben in Python
	print("Hallo")  # Einrückungen beachten
# Ab hier ist hallo() sichtbar

hallo()  # Funktion verwenden mit <Name>(<Parameter>...)
hallo()
hallo()  # Funktionen können mehrmals verwendet werden

# Funktion mit Parameter
def halloName(name):
	print(f"Hallo {name}")

halloName("Lukas")
halloName(123)
halloName(True)
halloName([1, 2, 3])  # Alle möglichen Parameter möglich, str kann nicht erzwungen werden

# Parameter können einen empfohlenen Typen haben (wird trotzdem nicht erzwungen)
def halloName2(name: str):
	print(f"Hallo {name}")

halloName2("Lukas")
halloName2(123)  # Zahl trotzdem möglich

# Mehrere Parameter
def addiere(x: int, y: int):
	print(x + y)

addiere(12, 23)
addiere(12.5, 29.4)
addiere("Abc", "Def")
addiere([1, 2, 3], [4, 5, 6])

# Funktionen können auch ein Ergebnis haben
# Dieses wird über return am Ende der Funktion zurückgeben
# z.B. len(...) -> Gibt die Zahl zurück mit der Anzahl der Elemente
def addiereReturn(x: int, y: int):
	return x + y

ergebnis = addiereReturn(4, 5)  # Das Ergebnis der Funktion (= der return Wert) in eine Variable schreiben
print(f"Das Ergebnis ist: {addiereReturn(4, 5)}")

# Rückgabetyp explizit angeben
def dividiere(x: int, y: int) -> int:
	return x / y

print(dividiere(7, 3))

# Default Werte
# Bei einem Parameter angeben was der Standardwert ist, muss beim Aufruf nicht übergeben werden, kann allerdings übergeben werden
def subtrahiere(x: int, y: int, z: int = 0):
	return x - y - z

subtrahiere(4, 6)  # z = 0 (Standardwert)
subtrahiere(4, 6, 8)  # z = 8 (Überschrieben)

# Alle Parameter sind optional, später kann der Benutzer auswählen welche Parameter er übergeben möchte
def generierePerson(vorname=None, nachname=None, gebdat=None, adresse=None, geschlecht=None):
	print()  # Code hier einfügen

generierePerson(vorname="Lukas", adresse="Eine Adresse")  # Nur Vorname und Adresse
generierePerson(adresse="Eine Adresse", geschlecht="M")  # Nur Adresse und Geschlecht

subtrahiere(y=4, x=1)  # Reihenfolge der Parameter ändern

# * Parameter (Arbitrary Arguments): Gibt die Möglichkeit, beliebig viele Parameter zu verlangen
# Innerhalb der Funktion kann dieser Parameter als Tuple verwendet werden
def addiere(*zahlen: int):  # Hier kann auch angegeben werden, welche Typen in dem Tuple enthalten sein sollen
	summe = 0
	for zahl in zahlen:
		summe += zahl
	return summe

addiere(1, 2, 3)  # 3 Parameter
addiere(1, 2, 3, 4, 5, 6, 7)  # 7 Parameter
addiere()  # Keine Parameter

# ** Parameter (Arbitrary Keyword Arguments): Gibt die Möglichkeit, beliebig viele Parameter in einer Dictionary Form zu verlangen
# Innerhalb der Funktion kann dieser Parameter als Dictionary verwendet werden
def halloTeilnehmer(**kwargs):
	for key, value in kwargs.items():
		print(f"{key} ist {value}")

testDict = {"Teilnehmer1": "Paul", "Teilnehmer2": "Richard"}
halloTeilnehmer(**testDict)

# Unpacking
# Listen/Dictionaries in seine Einzelteile zerlegen
# Mit * oder **
# -> args oder kwargs befüllen

intList = [1, 2, 3, 4]
addiere(*intList)

# Übung 1:
# Wir wollen eine Funktion erstellen, die beliebig viele Zahlen als Parameter erhalten kann
# Und uns die größte dieser Zahlen zurückgibt

# Übung 2:
# Wir wollen eine Funktion erstellen, die einen String als Paramter erhält
# Die Funktion soll dann in der Konsole ausgeben, aus wie vielen Klein- und Großbuchstaben der String besteht
# Die Funktion soll zusätzlich zählen wie viele Sonderzeichen (Nummern inkludiert) enthalten sind und das
# ebenfalls ausgeben
# Sonderzeichen: 4 | Groß: 3 | Klein: 12
