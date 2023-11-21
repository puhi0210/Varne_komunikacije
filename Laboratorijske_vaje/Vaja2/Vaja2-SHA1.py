def string_to_bits(data):
    bytes = ""
    for n in range(len(data)):
        bytes+='{0:08b}'.format(ord(data[n]))
    return bytes

def file_to_bits(file_path):
    try:
        with open(file_path, 'rb') as file:
            # Read the entire file content
            file_content = file.read()

            # Convert each byte to a binary string and concatenate them
            bits_string = ''.join(format(byte, '08b') for byte in file_content)

            return bits_string
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

    


def rol(n, b):
    return ((n << b) | (n >> (32 - b))) & 0xffffffff    


def split2words(data):
    words = chunks(data, 32)
    w = [0]*80
    for n in range(0, 16):
        w[n] = int(words[n], 2)
    for i in range(16, 80):
        w[i] = rol((w[i-3] ^ w[i-8] ^ w[i-14] ^ w[i-16]), 1)  
    return w


def chunks(podatki, dolzina_bloka):
    ### dopolnite funkcijo chunks, ki razbije podatke na bloke dolzine dolzina_bloka
    bloki = []
    for i in range(0, len(podatki), dolzina_bloka):
        bloki.append(podatki[i:i+dolzina_bloka])
    return bloki




def sha1(bytes):
    bits = string_to_bits(bytes)

    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476
    h4 = 0xC3D2E1F0

    bits += "1"

    bitsLen = '{0:064b}'.format(len(bits)-1)

    if len(bits)%512 > 448:
        bits += ("0"*(512 - (len(bits)%512)))

    bits += ("0"*(448 - (len(bits)%512)))

    bits += bitsLen

    bloki = chunks(bits, 512)
    
    for c in bloki:
        w = split2words(c)

        a = h0
        b = h1
        c = h2
        d = h3
        e = h4

        for t in range(80):
            if 0 <= t and t <= 19:
                k = 0x5A827999
                f = (b & c) | ((~b) & d)
            elif 19 < t and t <= 39:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif 39 < t and t <= 59:
                f = (b & c) | (b & d) | (c & d) 
                k = 0x8F1BBCDC
            elif 59 < t and t <= 79:
                f = b ^ c ^ d
                k = 0xCA62C1D6
        
            T = rol(a, 5) + f + e + k + w[t] & 0xffffffff

            
            e = d
            d = c
            c = rol(b, 30)
            b = a
            a = T

        h0 = (h0 + a) & 0xffffffff
        h1 = (h1 + b) & 0xffffffff
        h2 = (h2 + c) & 0xffffffff
        h3 = (h3 + d) & 0xffffffff
        h4 = (h4 + e) & 0xffffffff


    return   '{:08x}{:08x}{:08x}{:08x}{:08x}'.format(h0, h1, h2, h3, h4)

bytes = string_to_bits("hello world")

print (sha1(bytes)) 
print (sha1([])) 


#bytes = file_to_bits("Izpitna vprašanja Varkom2011.pdf")



