# Kontrollstrukturen

# if-Anweisungen
# Überprüft eine Bedingung und führt den enthaltenen Code aus wenn die Bedingung wahr ist
# Werden in Kombination mit Vergleichsoperatoren und Logischen Operatoren verwendet

# Vergleichsoperatoren
# Bedingungen aufbauen
# <, >, <=, >=
# ==, !=

a = 4
b = 8
if a > b:  # Code unterhalb wird nur ausgeführt wenn die Bedingung True ist
	print("a größer b")  # Durch Tabs die Ebenen festlegen
	print("If Ende")  # Mehrere Teile Code in der selben if

print("Nach der if")

# else
# Falls die if nicht True ist
if a > b:
	print("a größer b")
else:  # Wird nur ausgeführt, wenn die if nicht ausgeführt
	print("a kleiner gleich b")

# elif
# else-if
# else mit Bedingung

if a > b:
	print("a größer b")
elif a == b:
	print("a gleich b")
else:
	print("a kleiner gleich b")

# Verschachtelte if-else-Blöcke
if a < b:
	print("a kleiner b")
	if a % 2 == 0:  # Anwendung Modulo
		print("a ist gerade")
	else:
		print("a ist ungerade")

# Logische Operatoren
# Bedingungen kombinieren
# and (&), or (|): Zwei Bedingungen verknüpfen
# not (~): Bedingungen invertieren
# is: Schaut ob zwei Objekte identisch sind (Speicheradressen)
# in: Ist ein Element in einer Liste enthalten?

if a < b and a == 5:
	print("a kleiner als b und a gleich 5")

if not (a < b and a == 5):
	print("nicht a kleiner als b und a gleich 5")

liste = [1, 2, 3, 4, 5, 6]
if 3 in liste:
	print("Die Liste enthält die Zahl 3")

# Ternary Operator:
# Ermöglicht das Kürzen von if-elses auf eine einzige Zeile
if a <= b:
	print("a kleiner gleich b")
else:
	print("a größer b")

# Die obere if auf eine einzige Zeile komprimieren in Python
output = "a kleiner gleich b" if a <= b else "a größer b"
print("a kleiner gleich b" if a <= b else "a größer b")

output2 = "a kleiner b" if a < b else "a gleich b" if a == b else "a größer b"


# Übung 1
# Wir haben 3 vorgegebene Listen
list1 = [1, 2, 3, 4]
list2 = [2, 3, 4, 5, 6]
list3 = [5, 6, 7]
# Finde heraus welche Liste die längste ist (es können auch mehrere Listen die längsten sein)

# Übung 2
# Nimm die oberen drei Listen und überprüfe ob eine der Listen eine der drei Zahlen enthält: 3, 7, 10
