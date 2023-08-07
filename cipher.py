def build_cipher(shift):
    # Create the basic alphabet
    lowercase_letters = [chr(i) for i in range(ord('a'), ord('z')+1)]
    uppercase_letters = [chr(i) for i in range(ord('A'), ord('Z')+1)]

    # Build cipher dictionary
    cipher = {}

    # Add lowercase letters to cipher
    for i in range(26):
        cipher[lowercase_letters[i]] = lowercase_letters[(i+shift)%26]

    # Add uppercase letters to cipher
    for i in range(26):
        cipher[uppercase_letters[i]] = uppercase_letters[(i+shift)%26]

    return cipher

def encrypt_text(text, cipher):
    encrypted_text = ""

    for char in text:
        if char in cipher:
            encrypted_text += cipher[char]
        else:
            encrypted_text += char

    return encrypted_text

def main():
    text = input("Please enter a sentence: ")
    cipher = build_cipher(5)
    encrypted_text = encrypt_text(text, cipher)
    print(f"The encrypted text is: {encrypted_text}")

if __name__ == "__main__":
    main()
# add your code here
