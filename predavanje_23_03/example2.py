# generator akorda
alphabet = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "H"]
print("Glazbena abeceda sadrži tonove:")


for key in alphabet:
    print(key, end=" ")
print("\n")


i = 0
length = len(alphabet)
while i < length:
    # dok je i manji od dužine abecede
    # toliko puta izvrši sljedeće
    slovo = alphabet[i]
    # print(slovo) # slovo + "\n"
    print(slovo, end=" ")
    i += 1


startKey = (input("Unesite početni ton: ")).upper()
try:
    secondKeyDur = alphabet[(alphabet.index(startKey) + 4) % len(alphabet)]
    secondKeyMol = alphabet[(alphabet.index(startKey) + 3) % len(alphabet)]
    thirdKey = alphabet[(alphabet.index(startKey) + 7) % len(alphabet)]
    print(f"{startKey}dur = {startKey}{secondKeyDur}{thirdKey}")
    print(f"{startKey}mol = {startKey}{secondKeyMol}{thirdKey}")
except ValueError as ve:
    print(f"Unijeli ste simbol {startKey} koji nije dio glazbene abecede")
