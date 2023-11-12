# Tab, Tab, Attack

## Information

- picoCTF 2021
- General Skills
- 20 Points

## Description

Using tabcomplete in the Terminal will add years to your life, esp. when dealing with long rambling directory structures and filenames: [Addadshashanammu.zip](https://mercury.picoctf.net/static/fe16c756149cfa85f23e73cd9dbd6a25/Addadshashanammu.zip)

## Hints

1. After `unzip`ing, this problem can be solved with 11 button-presses...(mostly Tab)...

## Solution

Unzip the compressed file and then navigate using tab until you see a file. Then open the file using`cat` and the flag should be somewhere in the file.

## Flag

picoCTF{l3v3l_up!\_t4k3_4_r35t!\_76266e38}
