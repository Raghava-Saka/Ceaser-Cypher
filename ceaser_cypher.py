alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

direction = input("Type 'encode' to encrypt or 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift no.:\n"))

def encrypt():
    z = ""
    letters = list(text)
    for i in letters:
        index = alphabets.index(i)
        new_index = index + shift
        new_index %= len(alphabets)
        new_letter = alphabets[new_index]
        z += new_letter
    print(f"Here is the encoded result: {z}")

def decrypt():
    z = ""
    letters = list(text)
    for i in letters:
        index = alphabets.index(i)
        new_index = index - shift
        while new_index < 0:
            new_index += len(alphabets)
        new_letter = alphabets[new_index]
        z += new_letter
    print(f"Here is the decoded result: {z}")

if direction == "encode":
    encrypt()
elif direction == "decode":
    decrypt()