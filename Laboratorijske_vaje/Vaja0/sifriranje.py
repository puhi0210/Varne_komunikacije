
# Cezarjeva šifra
"""
sypher = "CerffNALxrlgbpbagvahr"
"""
def fnCezar(syph, key, devided):
    txt = ""
    # razdeljeno
    if devided != 0:
        for i in syph:
            if i.islower():
                codedChar = chr(((ord(i) -ord("a")+ key)%26) + ord("a"))
            elif i.isupper():
                codedChar = chr(((ord(i) -ord("A")+ key)%26) + ord("A"))
            elif i.isnumeric():
                codedChar = chr(((ord(i) -ord("0")+ key)%10) + ord("0"))
            
            txt += codedChar
    
    # nerazdeljeno
    else:
        for i in syph:
            codedChar = chr(((ord(i) - 32+ key)%95) + 32)
            txt += codedChar
        
    return txt;

"""

for j in range(26):
    print(fnCezar(sypher, j, 1) + "  key:" + str(j) + "\n")

sypher = "szwo"
sypher = "Hzgxkcdhi" # 11
sypher = "l#,9b-zz|9g~1.)(9$~9(z*)0~}z&9%)(~|9-0~.z94z9&~.)9KIOIG"

for j in range(126):
    print(fnCezar(sypher, j, 0) + "  key:" + str(j) + "\n")

"""

"""
# Vigenerjeva koda

def fnVigenere(cistopis, kljuc, smer):
    cistopis = cistopis.upper()
    txt = ""
    i = 0
    
           
    for char in cistopis:
        kljuc_n = ord(kljuc[i]) - ord("A")
        if smer: 
            kljuc_n = -kljuc_n
        codedChar = fnCezar(char, kljuc_n, 1)
        txt += codedChar
        i += 1
        i = i% len(kljuc)
    return txt;
    
print(fnVigenere(fnVigenere("attackatdawn", "LEMON", 0), "LEMON", 1))

print(fnVigenere("OHVIWYXIEIRQAICEIVGSFZTYBRGYZNTEMHMDNXNZHAVBVGWUMZXKOMMLDNXNGWKDEJBTAGOEIJCNXICRRGSKXIGUSJL", "VARNOST", 1))
"""

"""
def fnSubstitucija(cistopis, smer):
    abeceda =   "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    kljuc =     "QWERTYUIOPASDFGHJKLZXCVBNM"
    sifropis = ""
    
    for char in cistopis:
        if char == " " or char == "," or char == ".":
            coded_char = char
        else:
            lower = 0
            if char.islower():
                char = char.upper()
                lower = 1
                
            if smer:
                coded_char = kljuc[abeceda.index(char)]
            else:
                coded_char = abeceda[kljuc.index(char)]
                
            if lower:
                coded_char = coded_char.lower()
                
        sifropis += coded_char
    return sifropis
    
    
print(fnSubstitucija("Test ENA", 1))
print(fnSubstitucija(fnSubstitucija("Test ENA", 1), 0))
"""


def txt2bin(text):
    return ''.join(format(ord(i),'08b') for i in text)
    
print(txt2bin("BCDCADDD"))

