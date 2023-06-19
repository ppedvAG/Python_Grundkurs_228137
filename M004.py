# Schleife

# for Schleife
# Verhält sich wie foreach in anderen Sprachen
# Wird verwendet um eine Collection durchzugehen (List, Tuple, Set, String, Dictionary, ...)
# Syntax:
# for <Variablenname> in <Liste>

liste = ["Ich", "bin", "eine", "Liste"]

for wort in liste:  # Liste durchgehen und jedes Element ausgeben
	print(wort)
	if "e" in wort:  # Schauen ob ein Buchstabe in einem String ist
		print("Das derzeitige Wort enthält ein e")  # Mehrere Zeilen Code pro Schleifendurchlauf

# for-Schleife mit Zähler mithilfe von Range
for i in range(10):  # C#/Java/JS: for (int i = 0; i < 10; i++)
	print(i)

# for-Schleife um String durchzugehen
text = "Ein Text"
for zeichen in text:
	print(zeichen)

# break und continue
# Schleifen steuern
# break: Bricht die Schleife ab und führt den Code nach der Schleife aus
# continue: Springt zum Schleifenkopf zurück
for i in range(50):
	print(i)
	if i == 25:
		break  # Hier die Schleife abbrechen

print("Test")

for i in range(50):
	if i == 25:
		continue  # Hier den Code danach überspringen und zum Kopf zurückgehen
	print(i)

# else bei einer Schleife:
# Wird am Ende der Schleife ausgeführt, wenn kein break verwendet wurde
for i in range(0, 10):
	print(i)
else:
	print("Schleife fertig")


for i in range(0, 10):
	print(i)
	if i == 5:
		break  # Durch break wird das else übersprungen
else:
	print("Schleife fertig")

# fstring
# Formatted String
# Gibt die Möglichkeit, Code in einen String einzubauen
# Konvertiert automatisch das Ergebnis von dem eingebauten Code zu einem String
# Syntax:
# f"Text1 {Code} Text2"

a = 5
output = "Die Zahl ist " + str(a)
output2 = f"Die Zahl ist {a}"

for i in range(0, 20):
	# Die Zahl selber, die Zahl^2, die Gleichung von Zahl^2

	# Ohne fstring
	# print("Die Zahl ist " + str(i))
	# print("Die Zahl hoch 2 ist " + str(i ** 2))
	# print(str(i) + "^2=" + str(i ** 2))

	print(f"Die Zahl ist {i}")
	print(f"Die Zahl hoch 2 ist {i ** 2}")
	print(f"{i}^2={i ** 2}")


# Übung 1
# FizzBuzz
# 1. Schleife schreiben, die von 1 bis inklusive 100 hochzählt
# 2. Wir müssen in der Schleife jede Zahl auf ihre Teilbarkeit prüfen:
# Falls sie durch 3 teilbar ist, soll in der Konsole "Fizz" ausgegeben werden
# Falls sie durch 5 teilbar ist, soll in der Konsole "Buzz" ausgegeben werden
# Falls sie sowohl durch 3 als auch 5 teilbar ist, soll in der Konsole "FizzBuzz" ausgegeben werden
# Falls sie weder durch 3 noch 5 teilbar ist, soll die Zahl selbst in der Konsole ausgegeben werden
# 1
# 2
# Fizz
#  4
# Buzz
# ...
# 14
# FizzBuzz

# Übung 2
# Schreibe eine Schleife die dir alle Zahlen von 1 bis 200 zur Verfügung stellt
# Lass dir jede Zahl erst in der kardinalen und dann daneben in der ordinalen Schreibweise darstellen
# Zahl + Endung 'st', 'nd', 'rd' oder 'th'
# 1st, 2nd, 3rd, 4th, ..., 21st, 22nd, 23rd, 24th
# Bonus: Berücksichtige alle Zahlen die mit 11, 12 oder 13 enden