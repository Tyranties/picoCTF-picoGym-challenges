# PW Crack 5

## Information

- Beginner picoMini 2022
- General Skills
- 100 Points

## Description

Can you crack the password to get the flag?
Download the password checker [here](https://artifacts.picoctf.net/c/32/level5.py) and you'll need the encrypted [flag](https://artifacts.picoctf.net/c/32/level5.flag.txt.enc) and the [hash](https://artifacts.picoctf.net/c/32/level5.hash.bin) in the same directory too. Here's a [dictionary](https://artifacts.picoctf.net/c/32/dictionary.txt) with all possible passwords based on the password conventions we've seen so far.

## Hints

1. Opening a file in Python is crucial to using the provided dictionary.

2. You may need to trim the whitespace from the dictionary word before hashing. Look up the Python string function, `strip`

3. The `str_xor` function does not need to be reverse engineered for this challenge.

## Solution

Modify level5.py such that it will go through the list of potential passwords in dictionary.txt using `open` and a `for` loop. Once the correct password is entered, the flag will be shown.

## Flag

picoCTF{h45h_sl1ng1ng_40f26f81}
