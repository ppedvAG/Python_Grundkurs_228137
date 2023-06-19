# Ich bin ein Kommentar
# Mehrzeilige Kommentare existieren nicht, also muss vor jeder Zeile das # Zeichen gesetzt werden

# Wie werden Variablen deklariert?
# name = Wert

x = 5  # x ist eine Variable

# Alle Variablen sind dynamisch, d.h. ihre Datentypen können sich ändern
x = 1.5  # Hier steht jetzt eine Kommazahl darin

# Datentypen

# Jede Variable hat einen Typen, dieser wird über den Inhalt der Variable definiert

# Integer (int)
# Ganze Zahl, egal ob positiv oder negativ
# Beliebig groß

zahl = 5

grosseZahl = 375298375904218459843765812390687421869386700

# Float (float)
# Kommazahl

kommazahl = 49.28  # Kommazahlen immer mit . statt ,

# String (str)
# Text, wird mit "" oder mit '' definiert

meinText = "Ein Text"
meinText2 = 'Zwei Text'

# Boolean (bool)
# Wahr/Falsch Wert, True oder False möglich

wahr = True
falsch = False

# Methoden
# Methode = Funktion
# Code der bereits existiert und von uns verwendet werden kann
# Haben oft ein Ergebnis (Rückgabewert)

# print(Wert)
# Gibt den gegebenen Wert auf der Konsole aus
print(zahl)
print(kommazahl)
print(meinText)

# Methoden von Strings

# str.lower(), str.upper()
# Gibt eine Kopie des gesamten Texts in lowercase oder UPPERCASE zurück
meinText.upper()  # Output der Funktion wird nicht verwendet
print(meinText)  # Originaler Text
print(meinText.upper())  # Hier wird jetzt der Text in UPPERCASE ausgegeben

meinText.upper()

# str.count(Text)
# Zählt wie oft ein Text in dem gegebenen Text vorkommt

anzahlN = meinText.count('n')  # 1 wird in die Variable anzahlN geschrieben
print(anzahlN)

# Methoden verketten
# Ich kann das Ergebnis von einer Methode mit einer anderen Methode weiterverwenden
print(meinText.count("t"))  # 1, weil Groß-/Kleinschreibung nicht beachtet wird
print(meinText.lower().count("t"))  # Nimm das Ergebnis von lower, und mache einen Count darauf -> 2

# str.title()
# Schreibt den ersten Buchstaben jedes Worts groß, den Rest klein
meinName = "MaX muSTerMann"
print(meinName.title())

# str.is...
# Gibt einen Wahr-/Falsch Wert zurück wenn der String ein Kriterium erfüllt
meinText.islower()  # Sind alle Zeichen in dem String klein geschrieben?
meinText.isalpha()  # Besteht der Text nur aus Buchstaben? (keine Zahlen, keine Sonderzeichen)

# Strings verbinden
meinText + meinText2  # + alleine hat keinen Effekt -> Ergebnis der Addition muss verwendet werden
meinKombiText = meinText + meinText2
print(meinText + meinText2)

# Index (eckige Klammern)
# Eine Liste an einer bestimmten Stelle angreifen
# Funktioniert bei allen Listentypen (list, dict, set, tuple, str, ...)
# Startet bei 0 und endet bei Länge - 1
meinText[0]  # Gibt das erste Zeichen des Texts zurück
print(meinText[0])

# Ein Text -> Länge 8, Index 0 bis 7
ersterBuchstabe = meinText[0]
ersterBuchstabe.islower()  # Das Ergebnis von einer Indizierung auf einen String ist selbst wieder ein String

# len(Variable)
# Gibt die Länge der Variable zurück
# Funktioniert nur auf Variablen, die auch eine Länge haben
print(len(meinText))

# Auch Funktionen können im Index verwendet werden
# meinText[len(meinText)]  # Versucht an Stelle 8 zu greifen -> Fehler, weil Indizes von 0 bis 7 gehen
meinText[len(meinText) - 1]  # letztes Zeichen

# Index von rechts benutzen
print(meinText[-1])  # Das erste Zeichen von rechts (das letzte Zeichen)

# Range Operator
# Mehrere Elemente mit dem Index nehmen
print(meinText[4:6])  # Alle Elemente von 4 bis exklusive 6 -> Te
print(meinText[0:5])  # 0, 1, 2, 3 ,4 -> Ein T
print(meinText[0:5].lower())  # 0, 1, 2, 3 ,4 -> ein t

# complex
# Komplexe Zahlen
# j steht für den imaginären Teil
comp = 5 + 12j

# Arithmetische Operatoren
# +, -, *, /
# % Modulo: Gibt den Rest einer Division zurück
# Anwendungen
# - Wieviel Platz habe ich noch, wenn eine Liste in 4er Teile teilen möchte? 19 Elemente -> 19 % 4 = 3
# - Ist eine Zahl gerade? zahl % 2, wenn 1 -> ungerade, wenn 0 -> gerade
# ** Potenzierung
# // Ganzzahldivision

zahl1 = 5
zahl2 = 8
zahl1 + zahl2  # Diese Addition hat keinen Effekt, Ergebnis muss weiterverwendet werden

summe = zahl1 + zahl2
print(zahl1 + zahl2)

zahl1 += zahl2  # Nimm das Ergebnis dieser Addition, und schreibe es in zahl1
zahl1 = zahl1 + zahl2  # Selbiges wie oben

# += funktioniert auch mit allen anderen Operatoren (-=, *=, /=, %=, **=, //=)

# Ist zahl2 durch 4 teilbar?
print(zahl2 % 4)  # Bei Rest 0 -> ist teilbar, sonst nicht teilbar

# **: zahl1 hoch zahl2 (zahl1^zahl2)
print(zahl1 ** zahl2)  # 13^8 = 37822859361

# //: Division ohne Rest
print(15 / 7)  # 2.142
print(15 // 7)  # 2 -> Kommastellen werden abgeschnitten

# Arithmetik mit Strings
# Strings addieren
meinText += meinText2
text = "Mein Name ist "
text += "Lukas"
print(text)

# Strings multiplizieren
print(text * 5)
text *= 5
print(text)