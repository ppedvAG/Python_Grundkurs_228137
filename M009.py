# Klassen und Objekte

# Klasse
# Bauplan für Objekte, aus einer Klasse können beliebig viele Objekte erzeugt werden
# Klassen haben Strukturen (Variablen, Funktionen, ...) die Objekte haben dann diese Struktur
# Die Objekte haben im Anschluss konkrete Werte
# Aus einer Klasse können beliebig viele Objekte erzeugt werden
# z.B.: Klasse Auto (Marke, MaxV, AnzSitze) -> Objekte: [Audi, 250, 5], [BMW, 300, 5], [VW, 150, 7]

# Objekt
# Speicherbereich im RAM der reserviert wird und in dem die Werte der Variablen enthalten sind
# Können in Variablen gespeichert und später weiter verwendet werden
# Alles in Python ist ein Objekt (int, str, bool, List, Funktionen, ...)

i = 12  # int Objekt mit dem Wert 12
i.as_integer_ratio()  # Diese Funktion wurde in der Integer Klasse definiert, alle Integer haben diese Funktion

print(type(i))  # <class 'int'>

i = "123"
print(type(i))  # <class 'str'>
i.lower()  # Diese Funktion wurde in der str Klasse definiert, alle Strings haben diese Funktion

# Typvergleiche

# isinstance(Variable, Typ)
# Überprüft, ob eine Variable einen bestimmten Typ hat
if isinstance(i, str):
	print("i ist ein String")

if type(i) == str:
	print("i ist ein String")

# Eigene Klasse erstellen
class Person:
	"""
	docstring

	Ermöglicht Dokumentation von Strukturen (Klassen und Funktionen)

	Eine Klasse, die eine reale Person repräsentiert. Diese Person hat die Felder vorname und nachname.
	Die Person kann sprechen und ihren eigenen Namen über die Konsole ausgeben.
	"""

	# Konstruktor
	# Legt die Struktur der Klasse fest
	# Hier kann ich die Variablen der Klasse definieren
	# Hier können auch Parameter hinzugefügt werden, die bei der Objekterstellung gegeben sein sollen
	def __init__(self, vorname: str, nachname: str):  # Hier Vorname und Nachname erzwingen
		self.vorname = vorname  # Vorname zu Person hinzugefügt
		self.nachname = nachname  # Nachname zu Person hinzugefügt

	# self
	# Das Objekt selbst, nachdem es aus dem Bauplan heraus erzeugt wurde
	# Wenn eine Funktion in einer Klasse enthalten ist, hat diese generell immer self als ersten Parameter
	def sprechen(self, text: str):
		"""
		Diese Funktion schreibt den gegebenen Text Parameter (text) in die Konsole.
		"""
		print(text)

	# Hier mit self auf die konkreten Werte des fertigen Objekts greifen
	def printName(self):
		print(f"Hallo mein Name ist {self.vorname} {self.nachname}")

person = Person("Lukas", "Kern")  # Hier wird die __init__ Methode aufgerufen, Bauplan verwenden um ein Objekt zu erzeugen (new)
person.vorname = "Lukas"  # Hier konkrete Werte setzen
person.nachname = "Kern"

def printPerson(p: Person):  # Person Objekte verarbeiten
	print(f"Die Person heißt {p.vorname} {p.nachname}")  # Hier auf Variablen vom Person Objekt zugreifen

printPerson(person)
person.sprechen("Ich bin eine Person")  # Auf dem Person Objekt ist die Funktion laut Bauplan enthalten

# Dynamische Variablen
# In Python können Klassen einfach so neue Felder bekommen
# Sollte vermieden werden
person.xyz = 123
del person.xyz  # Feld wieder löschen


# Objekte in Action
# Beispiele: Büro Mitarbeiter, Account auf Webseite
# Jedes dieser Objekte enthält Daten
personenListe = []
personenListe.append(Person("Lukas", "Kern"))
personenListe.append(Person("Paul", "Blaurock"))
personenListe.append(Person("Richard", "König"))

for p in personenListe:
	print(f"Es ist {p.vorname} {p.nachname} im Raum")

# Übung 1:
# 1. Erstelle eine Fahrzeug-Klasse
# 2. Diese Klasse soll typische Eigenschaften eines Fahrzeuges enthalten:
#     - Fahrzeug-Name
#     - Preis
#     - Maximale Geschwindigkeit
#     - Derzeitige Geschwindigkeit
#     - Motorzustand (An/Aus)
# 3. Die Klasse soll auch folgende Methoden enthalten:
#     - Beschleunigen(Erhöhe bzw Verringere die Derzeitige Geschwindigkeit aber übersteige nicht das Maximum)
#     - StarteMotor
#     - StoppeMotor
#     - Beschreibung (Gibt alle Informationen über die Klasse wieder)
# 4. Erstelle eine Instanz der Klasse und nutze die Beschreibungs Funktion
