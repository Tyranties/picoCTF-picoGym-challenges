# PW Crack 4

## Information

- Beginner picoMini 2022
- General Skills
- 100 Points

## Description

Can you crack the password to get the flag?
Download the password checker [here](https://artifacts.picoctf.net/c/21/level4.py) and you'll need the encrypted [flag](https://artifacts.picoctf.net/c/21/level4.flag.txt.enc) and the [hash](https://artifacts.picoctf.net/c/21/level4.hash.bin) in the same directory too.
There are 100 potential passwords with 1 being correct. You can find these by examining the password checker script.

## Hints

1. A for loop can help you do many things very quickly.

2. The `str_xor` function does not need to be reverse engineered for this challenge.

## Solution

Since there are now 100 possible passwords, using trial and error would be impracticle. Instead modify level4.py such that each possible password is checked using a `for` loop. Once the correct password has been entered, the output should be the flag.

## Flag

picoCTF{fl45h_5pr1ng1ng_d770d48c}
