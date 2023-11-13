# PW Crack 1

## Information

- Beginner picoMini 2022
- General Skills
- 100 Points

## Description

Can you crack the password to get the flag?
Download the password checker [here](https://artifacts.picoctf.net/c/11/level1.py) and you'll need the encrypted [flag](https://artifacts.picoctf.net/c/11/level1.flag.txt.enc) in the same directory too.

## Hints

1. To view the file in the webshell, do: `$ nano level1.py`

2. To exit `nano`, press Ctrl and x and follow the on-screen prompts.

3. The `str_xor` function does not need to be reverse engineered for this challenge.

## Solution

Run the Python file and you should be prompted for a password. The password can be found on line 19 of `level1.py`. Enter the password and you should be given the flag.

## Flag

picoCTF{545h_r1ng1ng_fa343060}
