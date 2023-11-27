import re


def brute_force_caesar_cipher(ciphertext: str) -> None:
    for shift in range(26):
        decrypted_text = ''
        for char in ciphertext:
            if char.isalpha():
                if char.isupper():
                    decrypted_text += chr((ord(char) - shift - 65) % 26 + 65)
                else:
                    decrypted_text += chr((ord(char) - shift - 97) % 26 + 97)
            else:
                decrypted_text += char
        print(f"Shift {shift}: {decrypted_text}")


def get_ciphertext() -> str:
    with open("ciphertext", "r") as file:
        contents = file.read()
        matches = re.findall(r'\{(.*?)\}', contents)
        ciphertext = ''.join(matches)
    return ciphertext


def main():
    ciphertext = get_ciphertext()
    brute_force_caesar_cipher(ciphertext)


if __name__ == "__main__":
    main()
