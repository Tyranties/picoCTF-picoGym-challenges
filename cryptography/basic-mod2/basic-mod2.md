# basic-mod2

## Information

- picoCTF 2022
- Cryptography
- 100 Points

## Description

A new modular challenge!
Download the [message](https://artifacts.picoctf.net/c/180/message.txt) here.
Take each number mod 41 and find the modular inverse for the result. Then map to the following character set: 1-26 are the alphabet, 27-36 are the decimal digits, and 37 is an underscore.
Wrap your decrypted message in the picoCTF flag format (i.e. `picoCTF{decrypted_message}`)

## Hints

1. Do you know what the modular inverse is?

2. The inverse modulo _z_ of _x_ is the number, _y_ that when multiplied by _x_ is 1 modulo _z_

3. It's recommended to use a tool to find the modular inverses

## Solution

For this challenge, I wrote a [Python script](basic-mod2.py).

After getting all of the numbers, we need to go through each number and find the modular inverse of the number and 41:

```py
modular_inversed_number = pow(number, -1, 41)
```

Then we need to convert that number into either a letter, number or underscore.

```py
if 1 <= modular_inversed_number <= 26:
    plaintext += chr(ord('A') + modular_inversed_number - 1)
elif 27 <= modular_inversed_number <= 36:
    plaintext += str(modular_inversed_number - 27)
elif modular_inversed_number == 37:
    plaintext += '_'
```

Repeat for all numbers and concatenate the resulting character and you will get the flag.

## Flag

picoCTF{1NV3R53LY_H4RD_8A05D939}
