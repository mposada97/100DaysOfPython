alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encrypt(message, shift, direction):
    shift *= direction
    encrypted_message = ""
    for a in message:
        if a in alphabet:
            i = alphabet.index(a)
            encrypted_message += alphabet[i+shift]
        else:
            encrypted_message += a
    return encrypted_message

action = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
message = input('Type your message: \n').lower()
shift_number = int(input('Type the shift number: \n'))
if action == 'encode':
    result = encrypt(message, shift_number, 1)
    print(f"Here is the encoded result: {result}")
elif action == 'decode':
    result = encrypt(message, shift_number, -1)
    print(f"Here is the decoded result: {result}")
