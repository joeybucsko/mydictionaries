def main():
    codes = create_codes()
    encrypted_text = file_encryption(codes)
    write_encryption(encrypted_text)

#create codes
def create_codes():
    codes = {
        'A': '%', 'a': '9', 'B': '@', 'b': '#', 'C': '$', 'c': '1',
        'D': '^', 'd': '2', 'E': '&', 'e': '3', 'F': '*', 'f': '4',
        'G': '(', 'g': '5', 'H': ')', 'h': '6', 'I': '-', 'i': '7',
        'J': '_', 'j': '8', 'K': '=', 'k': '+', 'L': '[', 'l': ']',
        'M': '{', 'm': '}', 'N': '|', 'n': ';', 'O': ':', 'o': '"',
        'P': ',', 'p': '.', 'Q': '<', 'q': '>', 'R': '?', 'r': '/',
        'S': '!', 's': '~', 'T': '`', 't': 'A', 'U': 'B', 'u': 'C',
        'V': 'D', 'v': 'E', 'W': 'F', 'w': 'G', 'X': 'H', 'x': 'I',
        'Y': 'J', 'y': 'K', 'Z': 'L', 'z': 'M'
    }
    return codes

#open file and encyrpt it

def file_encryption(codes):
    unencrypted_text = open('info_security-1.txt', 'r')
    text = unencrypted_text.read()
    unencrypted_text.close()

    #Encrypted text
    encrypted_text = ''
    for char in text:
        if char in codes:
            encrypted_text += codes[char]
        else:
            encrypted_text += char
    
    return encrypted_text

#write encyrpted text in file
def write_encryption(encrypted_text):
    encrypted_file = open('encrypted.txt','w')
    encrypted_file.write(encrypted_text)
    encrypted_file.close()

main()