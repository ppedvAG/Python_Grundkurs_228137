def rechner():
	while True:
		zahl1 = zahl()
		zahl2 = zahl()

		while True:
			operation = int(input("Gib eine Operation ein (1 = +, 2 = -, 3 = *, 4 = /): "))
			if operation >= 1 or operation <= 4:
				break

		if operation == 1:
			print(f"{zahl1} + {zahl2} = {zahl1 + zahl2}")
		if operation == 2:
			print(f"{zahl1} - {zahl2} = {zahl1 - zahl2}")
		if operation == 3:
			print(f"{zahl1} * {zahl2} = {zahl1 * zahl2}")
		if operation == 4:
			print(f"{zahl1} / {zahl2} = {zahl1 / zahl2}")

		if input("Wiederholen? (Y)") != "Y":
			break

def zahl():
	while True:
		try:
			return int(input("Gib eine Zahl ein: "))
		except ValueError:
			continue

if __name__ == "__main__":
	rechner()