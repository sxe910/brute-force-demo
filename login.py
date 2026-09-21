import random
import secrets
import string
from passlib.hash import sha512_crypt


OUTPUT_FILE = "hashas.txt"

def slaptiko_gerneratorius(lygis: int) -> str:


	if lygis == 1:
		return "".join(random.choices(string.ascii_lowercase, k=4))

	elif lygis == 2:
		aibe = string.ascii_lowercase + string.digits
		return "".join(random.choices(aibe, k=6))

	elif lygis == 3:
		raide_did = random.choice(string.ascii_uppercase)
		raides_maz = "".join(random.choices(string.ascii_lowercase,k=7))
		skaitmuo = random.choice(string.digits)
		specialus = random.choice("!@#$%")
		return raide_did + raides_maz + skaitmuo + specialus

	elif lygis == 4:
		aibe = string.ascii_letters + string.digits + "!@#$%^&*"
		return "".join(secrets.choice(aibe) for _ in range(16))

	elif lygis == 5:
		ilgos = []
		with open ("rockyou.txt", "r", encoding="latin-1") as f:
			for eilute in f:
				zodis = eilute.strip()
				if len(zodis) >= 12:
					ilgos.append(zodis)

		return random.choice(ilgos)
	else:
		raise ValueError("Sudėtingumo lygis turi būti 1-5")

def uzmaisyti_slaptazodi(slaptazodis:str) -> str:
	return sha512_crypt.using(rounds=5000).hash(slaptazodis)


def main():
	print("Slaptažodžių sudėtingumo demonstracija")
	print("1 - labai silpnas (4 raidės)")
	print("2 - silpnas (6 simboliai, raidės+skaitmenys)")
	print("3 - vidutinis (10 simbolių, atitinka sudėties taisykles)")
	print("4 - stiprus (16 simbolių)")
	print("5 - tiesiog slaptažodis iš rockyou.txt")
 
	try:
		lygis = int(input("Pasirinkite sudėtingumo lygį (1-5): "))
	except ValueError:
		print("Reikia įvesti skaičių nuo 1 iki 5.")
		return
 
	if lygis not in (1, 2, 3, 4, 5):
		print("Netinkamas lygis. Pasirinkite 1, 2, 3, 4 arba 5.")
		return
 
	slaptazodis = slaptiko_gerneratorius(lygis)
	hash_reiksme = uzmaisyti_slaptazodi(slaptazodis)
 
    
	eilute = f"demo_vartotojas:{hash_reiksme}\n"
 
	with open(OUTPUT_FILE, "w") as f:
		f.write(eilute)
 
	print(f"\nSugeneruotas slaptažodis (jūsų akims, palyginimui): {slaptazodis}")
	print(f"Maišos reikšmė įrašyta į failą: {OUTPUT_FILE}")
 
 
if __name__ == "__main__":
	main()


		