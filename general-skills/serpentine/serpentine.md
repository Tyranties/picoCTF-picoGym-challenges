# Serpentine

## Information

- Beginner picoMini 2022
- General Skills
- 100 Points

## Description

Find the flag in the Python script!
[Download Python script](https://artifacts.picoctf.net/c/37/serpentine.py)

## Hints

1. Try running the script and see what happens

2. In the webshell, try examining the script with a text editor like `nano`

3. To exit `nano`, press Ctrl and x and follow the on-screen prompts.

4. The `str_xor` function does not need to be reverse engineered for this challenge.

## Solution

When initially running the file, you will notice, the `print_flag()` function has been misplaced. Simply add a call to the `print_flag()` function in the correct location such that when you enter `b` the flag will be shown.

## Flag

picoCTF{7h3_r04d_l355_7r4v3l3d_8e47d128}
