#Take tet input
text = input(" Enter a text : ")

#Take shift key
shift = int(input(" Enter a shift key : "))

#Encrypt the text
encrypted_text = ""

for char in text:
    if char.isupper ():
        position = ord(char) - ord("A")
        new_position = (position + shift)%26
        new_character = chr(new_position + ord("A"))
        encrypted_text = encrypted_text + new_character

    elif char.islower():
        position = ord(char) - ord("a")
        new_position = (position + shift)%26
        new_character = chr(new_position +ord("a"))
        encrypted_text = encrypted_text + new_character

    else:
        encrypted_text = encrypted_text + char

print("Encrypted Text : " , encrypted_text)

#Decrypt the encrypted text
decrypted_text = ""

for char in encrypted_text:
    if char.isupper ():
        position = ord(char) - ord("A")
        new_position = (position - shift)%26
        new_character = chr(new_position + ord("A"))
        decrypted_text = decrypted_text + new_character

    elif char.islower():
        position = ord(char) - ord("a")
        new_position = (position - shift)%26
        new_character = chr(new_position +ord("a"))
        decrypted_text = decrypted_text + new_character

    else:
        decrypted_text = decrypted_text + char

print("Decrypted Text : " , decrypted_text)