# fixme2.py

## Information

- Beginner picoMini 2022
- General Skills
- 100 Points

## Description

Fix the syntax error in this Python script to print the flag.
[Download Python script](https://artifacts.picoctf.net/c/5/fixme2.py)

## Hints

1. Are equality and assignment the same symbol?

2. To view the file in the webshell, do: `$ nano fixme2.py`

3. To exit `nano`, press Ctrl and x and follow the on-screen prompts.

4. The `str_xor` function does not need to be reverse engineered for this challenge.

5.

## Solution

Open `fixme2.py` using a code editor then on line 22 change `if flag = "":` to `if flag == "":` so that the `if` statement can run with the equality operator instead of the assignment operator. Run the file and the output should include the flag.

## Flag

picoCTF{3qu4l1ty_n0t_4551gnm3nt_4863e11b}
