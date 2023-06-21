import M008  # Alle Funktionen, Klassen von M008 importieren
from M008 import countCase, calcTax  # Nur bestimmte Member von einem Skript importieren
import sys
import numpy
import math

M008.countCase("Das ist ein Text")

# __name__: Der Name des Skripts
# __main__ wenn das Skript direkt gestartet wird
# Der Name des Skripts selbst, wenn es importiert wird
print(__name__)

# Modul Suchpfade
# 1. Im selben Ordner wie das ausgeführte Skript
# 2. PYTHONPATH, Ordner in dem Python enthalten ist
# 3. Pfade die bei der Installation von Python extra angegeben werden können
# Wenn nach Punkt 3 das Modul nicht gefunden wird -> ModuleNotFoundError

# sys
# Gibt Informationen über die Python Umgebung
print(sys.path)  # Zeigt die Modul Suchpfade
print(sys.version)  # Zeigt die Python Version
# sys.exit(10)  # Programm beenden mit Exit Code (Code 0 -> kein Fehler, nicht 0 -> Fehler der in einer Dokumentation festgehalten werden sollte)

# Pakete installieren:
# 2 Möglichkeiten
# - Über Python Packages
# - Über pip
# -- pip install <Name>
# -- pip uninstall <Name>
math.floor(4.4)  # math für simple Mathematik
numpy.floor(5.5)  # numpy für komplexe Mathematik

# __init__.py
# Beschreibt ein Init Skript
# Wird ausgeführt bei import von dem entsprechenden Paket (Ordner)

# Main Funktion soll am Start des Programms ausgeführt werden
def main():
	print("Das ist die Hauptfunktion von M008b")
	pass  # pass: Mach nichts, Platzhalter

# Diese if ist in vielen Python Skripten vorhanden
# Sie wird ausgeführt, wenn das Skript direkt gestartet wird (über PyCharm oder über die Python Runtime)
if __name__ == "__main__":
	main()  # Main Funktion ist nicht erzwungen, wird aber oftmals so gemacht

# Übung
# Rechner anpassen
# - Die vier Rechenarten in ein eigenes Skript namens Rechner.py geben
# - Im anderen Skript importieren und verwenden
# - Die vier Rechenarten müssen in Funktionen gegeben werden
# - In der Main den Rechner starten