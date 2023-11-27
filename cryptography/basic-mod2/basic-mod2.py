from typing import List

def decrypt(numbers: List[int]) -> str:
    plaintext = ""
    for number in numbers:
        modular_inversed_number = pow(number, -1, 41)
        if 1 <= modular_inversed_number <= 26:
            plaintext += chr(ord('A') + modular_inversed_number - 1) 
        elif 27 <= modular_inversed_number <= 36:
            plaintext += str(modular_inversed_number - 27)
        elif modular_inversed_number == 37:
            plaintext += '_'
    return plaintext

def get_message() -> List[int]:
    with open("message.txt", "r") as file:
        contents = file.read()
    numbers = contents.split()
    return [int(number) for number in numbers]

def main():
    numbers = get_message()
    plaintext = decrypt(numbers)
    print("Decrypted Message:", plaintext)

if __name__ == "__main__":
    main()