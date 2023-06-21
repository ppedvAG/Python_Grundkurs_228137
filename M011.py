# Fehlerbehandlung
import traceback


# xyz  # NameError
# type()  # TypeError
def rec():
	rec()

# rec()  # RecursionError

# eingabe = input("Gib eine Zahl ein: ")
# zahl = int(eingabe)  # ValueError, falls der User keine Zahl eingibt

# try
# Hier ist der Code enthalten der potenziell einen Fehler bringen könnte
try:
	eingabe = input("Gib eine Zahl ein: ")
	zahl = int(eingabe)
	print(5 / zahl)
except ValueError:  # Im except Block findet die Fehlerbehandlung statt
	print("Keine Zahl eingegeben")  # Programm stürzt hier nicht ab
except ZeroDivisionError:  # Mehrere Except Blöcke um mehrere Fehler abzufangen
	print("Division durch 0 ist nicht erlaubt")
except Exception as e:  # Except ohne Error fängt alle anderen Fehler ab
	print(f"Anderer Fehler: {e}")  # Mit as e können Errors nochmal spezifisch angesprochen werden
else:  # Wird ausgeführt wenn keine Fehler auftreten
	print("Keine Fehler")
finally:  # Wird immer ausgeführt (auch bei Fehlern)
	print("Wird immer ausgeführt")


raise OSError("eine Nachricht")  # Fehler werfen (Programm abstürzen lassen), anderer Entwickler muss mit try/except hier arbeiten

print("Programm läuft weiter")

class NoCoffeeError(Exception):
	pass

raise NoCoffeeError()