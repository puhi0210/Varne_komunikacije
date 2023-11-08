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