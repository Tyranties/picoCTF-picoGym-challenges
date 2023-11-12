# strings it

## Information

- picoCTF 2019
- General Skills
- 100 Points

## Description

Can you find the flag in [file](https://jupiter.challenges.picoctf.org/static/94d00153b0057d37da225ee79a846c62/strings) without running it?

## Hints

1. [strings](https://linux.die.net/man/1/strings)

## Solution

To find the flag we need to use `strings` and `grep`. In the linux terminal enter `strings strings | grep -i picoCTF` and it will search for any string containing the 'picoCTF'. The flag will be the only string with this.

## Flag

picoCTF{5tRIng5_1T_d66c7bb7}
