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
    return




def sha1(bytes):

    ####dopolnite


    return   

bytes = string_to_bits("hello world")

print (sha1(bytes)) 

bytes = file_to_bits("Izpitna vprašanja Varkom2011.pdf")



