from typing import List


def decrypt(numbers: List[int]) -> str:
    plaintext = ""
    for number in numbers:
        modded_number = number % 37
        if 0 <= modded_number <= 25:
            plaintext += chr(ord('A') + modded_number)
        elif 26 <= modded_number <= 35:
            plaintext += str(modded_number - 26)
        elif modded_number == 36:
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
