def check_vowels():
    nombre = input("> ").lower()
    vocalA = "a" in nombre
    vocalE = "e" in nombre
    vocalI = "i" in nombre
    vocalO = "o" in nombre
    vocalU = "u" in nombre
    print(f"Contiene a: {vocalA}")
    print(f"Contiene e: {vocalE}")
    print(f"Contiene i: {vocalI}")
    print(f"Contiene o: {vocalO}")
    print(f"Contiene u: {vocalU}")
