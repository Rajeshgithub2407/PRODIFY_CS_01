def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            decrypted_text += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            decrypted_text += char
    return decrypted_text

def main():
    while True:
        print("Choose an option:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            text = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value: "))
            encrypted_text = caesar_cipher_encrypt(text, shift)
            print(f"Encrypted message: {encrypted_text}")

        elif choice == '2':
            text = input("Enter the message to decrypt: ")
            shift = int(input("Enter the shift value: "))
            decrypted_text = caesar_cipher_decrypt(text, shift)
            print(f"Decrypted message: {decrypted_text}")

        elif choice == '3':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
