# PW Crack 2

## Information

- Beginner picoMini 2022
- General Skills
- 100 Points

## Description

Can you crack the password to get the flag?
Download the password checker [here](https://artifacts.picoctf.net/c/13/level2.py) and you'll need the encrypted [flag](https://artifacts.picoctf.net/c/13/level2.flag.txt.enc-) in the same directory too.

## Hints

1. Does that encoding look familiar?

2. The `str_xor` function does not need to be reverse engineered for this challenge.

## Solution

Run the Python file and you should be prompted for a password. The password can be found on line 18 of `level2.py`, but it is encoded as hexidecimal ASCII. Decode it using an ASCII table to characters for the password. Enter the password and you should be given the flag.

## Flag

picoCTF{tr45h_51ng1ng_489dea9a}
