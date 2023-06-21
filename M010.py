# Vererbung
# Klassen können eine Oberklasse haben und damit eine Vererbungshierarchie herstellen
# Die Oberklasse gibt ihre Member (Variablen, Funktionen) nach unten weiter
# Beispiel: Lebewesen ist eine Oberklasse von Mensch, Hund, Katze
# Lebewesen enthält Alter:int und Bewegen() -> Mensch, Hund, Katze werden diese Member auch haben

class Lebewesen:
	# __init__ kommt von der object Klasse
	def __init__(self, alter:int):
		self.alter = alter

	def bewegen(self):
		print("Das Lebewesen bewegt sich")

	# __str__
	# Gibt eine Stringrepräsentation von dem Objekt zurück
	def __str__(self):
		return f"Das Lebewesen ist {self.alter} Jahre alt"

class Mensch(Lebewesen):  # In der Klammer eine Vererbungshierarchie herstellen (Mensch ist ein Lebewesen)
	def __init__(self, alter: int, name: str):
		super().__init__(alter)  # Wenn ich einen Menschen erstelle muss ich den Code aus Lebewesen auch ausführen
		self.name = name

	# Methode von Lebewesen überschreiben, eigenes Verhalten implementieren
	def bewegen(self):
		print("Der Mensch bewegt sich")

	# Mit super() auf Funktion und Felder der Oberklasse zugreifen
	def __str__(self):
		return super().__str__() + " und bin ein Mensch"


mensch = Mensch(20, "Test")
mensch.bewegen()  # bewegen wurde jetzt von oben weitergegeben
print(mensch)  # Hier wird die __str__ Funktion aufgerufen
print([1, 2, 3])  # Hier wurde auch die __str__ Funktion überschrieben

# Übung
# 1. Erstelle die drei folgenden Subklassen der Fahrzeug-Klasse:
#     - PKW
#     - Schiff
#     - Flugzeug
# 2. Füge jeweils eine neue passende Eigenschaft hinzu
# 3. Überschreibe die Beschreibungs-Funktion der Basis-Klasse um auch die neuen Eigenschaften wiederzugeben
# 4. Erstelle jeweils eine Instanz der Klassen und nutze die Beschreibungs Funktionen