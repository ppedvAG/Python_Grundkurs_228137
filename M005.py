# List Comprehension
# Schnell eine Liste erzeugen anhand eines Musters
# Das Muster wird über Schleifen dargestellt

# Eine Liste von 1 bis 10

# Mit Schleife
zahlen = []
for i in range(1, 11):
	zahlen.append(i)
print(zahlen)

# Mit List Comprehension
zahlenLC = [i for i in range(1, 11)]  # Normale For-Schleife schreiben und danach i vor die Schleife schreiben
print(zahlenLC)

# Alle geraden Zahlen von 1 bis 100 in eine Liste schreiben
zahlenGerade = []
for i in range(1, 101):
	if i % 2 == 0:
		zahlenGerade.append(i)
print(zahlenGerade)

# Mit List Comprehension
zahlenGeradeLC = [i for i in range(1, 101) if i % 2 == 0]  # Zu List Comprehensions können auch ifs hinzugefügt
print(zahlenGeradeLC)

# Alle geraden Zahlen von 1 bis 100 multipliziert mit sich selbst in eine Liste schreiben
zahlenGeradePotenz = []
for i in range(1, 101):
	if i % 2 == 0:
		zahlenGeradePotenz.append(i ** i)
print(zahlenGeradePotenz)

# Mit List Comprehension
zahlenGeradePotenzLC = [i ** i for i in range(1, 101) if i % 2 == 0]  # Bei List Comprehensions kann auch der Wert vor dem Einfügen bearbeitet werden
print(zahlenGeradePotenzLC)

# Kleines 1x1 mit normalen Schleifen darstellen
for zahl1 in range(1, 11):
	for zahl2 in range(1, 11):
		print(f"{zahl1}x{zahl2}={zahl1 * zahl2}")

# Verschachtelte Schleife mit List Comprehension
einmaleins = [f"{i}x{j}={i * j}" for i in range(1, 11) for j in range(1, 11)]
print(einmaleins)

for text in einmaleins:
	print(text)

# Beispiel für List Comprehension
for text in [f"{i}x{j}={i * j}" for i in range(1, 11) for j in range(1, 11)]:
	print(text)

# List Comprehension mit Ternary Operator
# Liste mit Zahl + Info ob die Zahl gerade ist oder nicht
oddEven = []
for i in range(1, 101):
	if i % 2 == 0:
		oddEven.append(f"{i}: even")
	else:
		oddEven.append(f"{i}: odd")
print(oddEven)

# Mit LC
oddEvenLC = [f"{i}: even" if i % 2 == 0 else f"{i}: odd" for i in range(1, 101)]
print(oddEvenLC)

# List Comprehension mit String Liste
stringListe = ["IcH", "bIN", "eiN", "TexT"]

stringsUpper = [wort.upper() for wort in stringListe]  # Links den Wert bearbeiten, Rechts den Wert anschauen (if)
print(stringsUpper)

# Schreibe alle Wörter groß die einen großen Anfangsbuchstaben haben, schreibe alle anderen Wörter klein
stringsUpperLower = [wort.upper() if wort[0].isupper() else wort.lower() for wort in stringListe]  # Links den Wert bearbeiten
print(stringsUpperLower)

# In einem Text alle Wörter finden die ein e enthalten
text = "Das ist ein Text dieser Text enthält einige Wörter"

textList = text.split(" ")
print(textList)

woerterMitE = [wort for wort in textList if wort.count("e") > 0]
print(woerterMitE)

# Match Case
# Switch in anderen Sprachen
# if/elif einfacher darstellen
x = 5
if x == 5:
	print("Fünf")
elif x == 6:
	print("Sechs")
elif x == 7:
	print("Sieben")
elif x == 8:
	print("Acht")
else:
	print("Andere Zahl")

match x:
	case 5:
		print("Fünf")
	case 6:
		print("Sechs")
	case 7:
		print("Sieben")
	case 8:
		print("Acht")
	case _ if x < 5:
		print("Zahl kleiner 5")
	case _:  # Else
		print("Andere Zahl")

# Übung 1
# Schreibe eine List-Comprehension die nur Zahlen aus einer Range von 1 bis inklusive 30 in die neue Liste packt,
# falls die Zahl durch 6 teilbar ist
# Bevor die Zahl in die neue Liste gepackt wird, soll sie um 12 erhöht werden
print([num + 12 for num in range(1, 31) if num % 6 == 0])

# Übung 2
# Schreibe eine List-Comprehension die aus einem Text alle Kleinbuchstaben nimmt und Groß in die Liste schreibt
text = "Ich bin ein Text"
print([b.upper() for b in text if b.islower()])

# Übung 3
# Schreibe eine List-Comprehension die aus einem Text alle Anfangsbuchstaben nimmt
print([wort[0] for wort in text.split(" ")])
print([wort[0] for wort in text.title() if wort.isupper()])

# Übung 4
# Schreibe eine List-Comprehension die aus einem Text alle Wörter nimmt die 3 oder weniger Zeichen haben
print([wort for wort in text.split(" ") if len(wort) <= 3])