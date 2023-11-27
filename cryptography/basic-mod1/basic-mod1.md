# basic-mod1

## Information

- picoCTF 2022
- Cryptography
- 100 Points

## Description

We found this weird message being passed around on the servers, we think we have a working decryption scheme.
Download the message [here](https://artifacts.picoctf.net/c/128/message.txt).
Take each number mod 37 and map it to the following character set: 0-25 is the alphabet (uppercase), 26-35 are the decimal digits, and 36 is an underscore.
Wrap your decrypted message in the picoCTF flag format (i.e. `picoCTF{decrypted_message}`)

## Hints

1. Do you know what `mod 37` means?

2. `mod 37` means modulo 37. It gives the remainder of a number after being divided by 37.

## Solution

For this challenge, I wrote a [Python script](basic-mod1.py).

After getting all of the numbers, we need to go through each number and then perform a modulo 37 operation:

```py
modded_number = number % 37
```

Then we need to convert that number into either a letter, number or underscore.

```py
if 0 <= modded_number <= 25:
    plaintext += chr(ord('A') + modded_number)
elif 26 <= modded_number <= 35:
    plaintext += str(modded_number - 26)
elif modded_number == 36:
    plaintext += '_'
```

Repeat for all numbers and concatenate the resulting character and you will get the flag.

## Flag

picoCTF{crossingtherubiconvfhsjkou}
