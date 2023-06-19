# List
# Kann mehrere Werte in einer Variable speichern
# Hat einen Index wie String
# Ist veränderbar, neue Elemente können hinzugefügt und bestehende Elemente können entfernt werden
# Duplikate sind erlaubt
# Verschiedene Datentypen sind erlaubt (sollte vermieden werden)

meineListe = [1, 2, 3, 4, True, "Ein Element"]
print(meineListe)  # Liste kann einfach mit print ausgegeben werden

# Auf einzelne Werte mittels Index zugreifen
print(meineListe[4])  # -> True, da Index von 0 beginnt

# Range Operator
print(meineListe[2:5])  # [3, 4, True], Obergrenze wieder exkludiert

# Range ohne (Ober/Unter-) Grenze
print(meineListe[2:])  # [3, 4, True, 'Ein Element'], Range mit einer fehlenden Grenze gibt den Rest (bis zum Maximum)
print(meineListe[:4])  # [1, 2, 3, 4]
print(meineListe[-3:-1])  # [4, True]

# list(Objekt)
# Konvertiert das gegebene Objekt zu einer Liste
text = "Ein Text"
stringListe = list(text)  # Wandelt den String in eine Liste um, jedes Zeichen wird ein Element in der Liste
print(stringListe)

# list.append(Wert)
# Fügt den Wert ans Ende der Liste an
meineListe.append(10)
print(meineListe)

# list.pop(Index)
# Entfernt das Element am gegebenen Index
meineListe.pop(4)
meineListe.pop(4)
print(meineListe)

# list.sort()
# Sortiert die Liste, funktioniert nur bei numerischen Listen oder String Listen
meineListe.sort()

# len(List)
# Gibt die Anzahl der Elemente zurück
print(len(meineListe))

# Element bearbeiten
meineListe[0] = 20


# Tupel
# Verhalten sich ähnlich wie Listen
# Können nicht verändert werden, keine neuen Elemente, bestehende Elemente können nicht verändert werden
# Duplikate sind erlaubt
# Index

meinTupel = (1, 2, 3, 4)
print(meinTupel)

# Tupel über Umweg verändern
tempListe = list(meinTupel)
tempListe[0] = 10
meinTupel = tuple(tempListe)
print(meinTupel)

# Unpacking
# Löst interierbare Objekt in ihre einzelnen Elemente auf und schreibt sie in Variablen
(zahl1, zahl2, zahl3, zahl4) = meinTupel
print(zahl1)

# Funktioniert auch bei String
unpackString = "Test"
(b1, b2, b3, b4) = unpackString
print(b1)
print(b2)
print(b3)
print(b4)


# Range
# Sequenz von Zahlen
# Wird häufig in Schleifen verwendet

# Syntax:
# range(Endzahl) -> Gibt den Bereich von 0 bis Endzahl
# range(Startzahl, Endzahl) -> Gibt den Bereich von Startzahl bis Endzahl
# range(Startzahl, Endzahl, Schrittgröße) -> Gibt den Bereich von Startzahl bis Endzahl mit einer Schrittgröße
print(range(100))  # Das Range Objekt
print(list(range(100)))  # Die komplett durchiterierte Range
print(list(range(50, 100)))  # 50 bis 99
print(list(range(50, 100, 2)))  # 50 bis 98, +1 um 100 auch zu inkludieren
print(list(range(50, 101, 2)))  # 50 bis 100


# Set
# Funktioniert ähnlich wie die Liste
# Elemente müssen eindeutig sein
# Werte können nicht angepasst werden

meinSet = {1, 2, 3, 4, 1}
print(meinSet)  # Die zweite eins wurde entfernt

# set.add(Element)
# Fügt ein Elemente am Ende des Sets hinzu

meinSet.add(10)
print(meinSet)

# set.pop()
# Entfernt das erste Element

meinSet.pop()
print(meinSet)

# set.update(Liste)
# Fügt alle Elemente hinzu, die nicht in dem Set vorhanden sind

meinSet.update([3, 4, 5, 6, 7])
print(meinSet)


# Dictionary
# Liste von Key-Value Paaren
# Sind veränderbar
# Keys müssen eindeutig sein

meinAuto = {
	"Marke": "Audi",
	"Modell": "A3",
	"Baujahr": 2017
}

print(meinAuto)
print(meinAuto["Marke"])  # Dictionary ansprechen mit String Index (Name vom Key)

# Werte anpassen
meinAuto["Baujahr"] = 2020
print(meinAuto)

# dict.get(String)
# Gibt den Wert an dem entsprechenden Key zurück, oder None
# print(meinAuto["Reifen"])  # KeyError, weil Reifen nicht existiert
print(meinAuto.get("Reifen"))
print(meinAuto.get("Modell"))

# dict.setdefault(Key, Value)
# Fügt den Key hinzu, wenn er nicht existiert
meinAuto.setdefault("Reifen", 4)
meinAuto.setdefault("Reifen", 8)
print(meinAuto)

# dict.pop(Key)
# Entfernt den gegebenen Key
meinAuto.pop("Modell")
print(meinAuto)


# Übung 1
# Wir haben 3 vorgegebene Listen
list1 = [1, 2, 3, 4]
list2 = [2, 3, 4, 5, 6]
list3 = [5, 6, 7, 8]
# Kombiniere die drei Listen in eine ganze Liste und schließe Duplikate aus

# Übung 2
# Erstelle einen String und wandele ihn in eine Liste um, dabei soll jedes einzelne Zeichen ein Element der Liste werden

# Übung 3
# Lasse eine Liste erstellen die bei 0 beginnt und alle geraden Zahlen bis 20 enthält
# Nicht selbst schreiben, sondern Python machen lassen
