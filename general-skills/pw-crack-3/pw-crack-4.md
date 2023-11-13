# PW Crack 3

## Information

- Beginner picoMini 2022
- General Skills
- 100 Points

## Description

Can you crack the password to get the flag?
Download the password checker [here](https://artifacts.picoctf.net/c/17/level3.py) and you'll need the encrypted [flag](https://artifacts.picoctf.net/c/17/level3.flag.txt.enc) and the [hash](https://artifacts.picoctf.net/c/17/level3.hash.bin) in the same directory too.
There are 7 potential passwords with 1 being correct. You can find these by examining the password checker script.

## Hints

1. To view the level3.hash.bin file in the webshell, do: `$ bvi level3.hash.bin`

2. To exit `bvi` type `:q` and press enter.

3. The `str_xor` function does not need to be reverse engineered for this challenge.

## Solution

The seven possible passwords are found on line 44 of level3.py. Simply enter use trial and error on all seven possible passwords and you will get the flag after the correct password has been entered.

## Flag

picoCTF{m45h_fl1ng1ng_cd6ed2eb}
