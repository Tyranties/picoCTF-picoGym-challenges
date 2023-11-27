import codecs

def decode(cipher_text: str) -> str:
    return codecs.decode(cipher_text, 'rot_13')

def main():
    cipher_text = input()
    plain_text = decode(cipher_text)
    print(plain_text)

if __name__ == "__main__":
    main()