
# par kljucev

def fnRSA(besedilo, kljuc, n):
    sifropis = ""
    for char in besedilo:
        coded = chr(((ord(char))**kljuc)%n)
        sifropis += coded
    return sifropis

print(fnRSA("Preizkus delovanja", 7, 143))
print(fnRSA(fnRSA("Preizkus delovanja", 7, 143), 103, 143))