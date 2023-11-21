import sys
sys.path.append(".")
from DES_funkcije import *


def prepare_keys(kljuc):
    bin_kljuc = text2bin(kljuc)
    bin_kljuc = permute(bin_kljuc, keyp, 56)
    left = bin_kljuc[0:28]
    right = bin_kljuc[28:56]
    keys = []
    for i in range(16):
        left = shift_left(left, shift_table[i])
        right = shift_left(right, shift_table[i])
        combine = left + right
        round_key = permute(combine, key_comp, 48)
        keys.append(round_key)
    return keys


def encrypt(cistopis, kljuc):
    keys = prepare_keys(kljuc)

    bin_cistopis = text2bin(cistopis)
    bin_cistopis = permute(bin_cistopis, initial_perm, 64)
    left = bin_cistopis[0:32]
    right = bin_cistopis[32:64]
    for i in range(16):
        str_right = F(right, keys[i])
        left = xor(left, str_right)

        if i < 15:
            temp = left
            left = right
            right = temp
    
    combined = left + right
    koncni_bin = permute(combined, final_perm, 64)
    return bin2text(koncni_bin)

print(encrypt("skrivnost","geslogeslo"))

#   Naloga 3
print(encrypt("cistopis","12345678"))
print(encrypt("Cistopis","12345678"))
print(diff_bits("cistopis","Cistopis"))

#   Naloga 4
def decrypt(cistopis, kljuc):
    keys = prepare_keys(kljuc)

    bin_cistopis = text2bin(cistopis)
    bin_cistopis = permute(bin_cistopis, initial_perm, 64)
    left = bin_cistopis[0:32]
    right = bin_cistopis[32:64]
    for i in range(16):
        str_right = F(right, keys[15 - i])
        left = xor(left, str_right)

        if i < 15:
            temp = left
            left = right
            right = temp
    
    combined = left + right
    koncni_bin = permute(combined, final_perm, 64)
    return bin2text(koncni_bin)


print(decrypt("Qc¦Å2BGñ","geslogeslo"))


#   Naloga 5
def ECB(cistopis, kljuc, smer):
    izhod = ""
    for i in range(0, len(cistopis), 8):
        block = cistopis[i:8+i]
        if not smer:
            block = block.ljust(8, '0')
            izhod += encrypt(block, kljuc)

        else:
            cistopis_block = decrypt(block, kljuc)
            izhod += cistopis_block.rstrip('0')

    return izhod

print(ECB("skrivnostskrivnostooo", "geslogeslo", 0))
print(ECB(ECB("skrivnostblabla", "geslogeslo", 0), "geslogeslo", 1))




# Domača naloga
# Naloga 6
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
allKeys = []
for i in alphabet:
    for j in alphabet:
        allKeys. append(i + j + "000000")

for i in allKeys:
    print(decrypt(bin2text("1111011101000011001110010110111101110011100000000011110100111010"),i))


# Naloga 7
def  fun_3TDEA(cistopis, kljuc1, kljuc2, kljuc3, smer): # smer: 1=>encript, 0=>decript
    if smer:
        return encrypt(decrypt(encrypt(cistopis, kljuc1),kljuc2),kljuc3)
    else:
        return decrypt(encrypt(decrypt(cistopis, kljuc3),kljuc2),kljuc1)

def  fun_2TDEA(cistopis, kljuc1, kljuc2, smer): # smer: 1=>encript, 0=>decript
    if smer:
        return fun_3TDEA(cistopis, kljuc1, kljuc2, kljuc1, 1)
    else:
        return fun_3TDEA(cistopis, kljuc1, kljuc2, kljuc1, 0)
       
       
print(fun_2TDEA("cistopis","12345678","87654321",1))
print(fun_2TDEA(fun_2TDEA("cistopis","12345678","87654321",1),"12345678","87654321",0))