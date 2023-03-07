from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

shift %= 26

def encrypt(t = text, s = shift):

    result = ""

    for l in t:
        if l not in alphabet:
            result += l
        else:
            position = alphabet.index(l)
            new = alphabet[position + s]
            result += new

    print(result)

def decrypt(t = text, s = shift):
    result = ""

    for l in t:
        if l not in alphabet:
            result += l
        else:
            position = alphabet.index(l)
            new = alphabet[position - s]
            result += new

    print(result)

if direction == "encode":
    encrypt()

elif direction == "decode":
    decrypt()