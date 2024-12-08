char_array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
              'v', 'w', 'x', 'y', 'z']


def encrypt(message, scale):
    encrypted_message = ""
    for char in message:
        if char_array.count(char) == 0:
            encrypted_message += char
            continue
        char_index = char_array.index(char)
        encrypted_char_index = char_index + scale
        if encrypted_char_index > len(char_array) - 1:
            encrypted_char_index = encrypted_char_index - len(char_array)
        encrypted_message += char_array[encrypted_char_index]

    return encrypted_message


def decrypt(message, scale):
    decrypted_message = ""
    for char in message:
        if char_array.count(char) == 0:
            decrypted_message += char
            continue
        char_index = char_array.index(char)
        decrypted_char_index = char_index - scale
        if decrypted_char_index < 0:
            decrypted_char_index = len(char_array) + decrypted_char_index
            print(decrypted_char_index)
        decrypted_message += char_array[decrypted_char_index]

    return decrypted_message


encrypt_or_decrypt = ""
while encrypt_or_decrypt.lower() != "encrypt" and encrypt_or_decrypt.lower() != "decrypt":
    encrypt_or_decrypt = input("What do you want encrypt or decrypt? ")
    if encrypt_or_decrypt.lower() != "encrypt" and encrypt_or_decrypt.lower() != "decrypt":
        print("Invalid argument. Please choose either encrypt option or decrypt option.")

message = input("Please enter message: ")
scale = int(input("Please enter the scale between 0-9 "))
if encrypt_or_decrypt == "encrypt":
    print(encrypt(message.lower(), scale))
else:
    print(decrypt(message.lower(), scale))
