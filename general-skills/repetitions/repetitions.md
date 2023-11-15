# repetitions

## Information

- picoCTF 2023
- General Skills
- 100 Points

## Description

Can you make sense of this file?
Download the file [here](https://artifacts.picoctf.net/c/475/enc_flag).

## Hints

1. Multiple decoding is always good.

## Solution

The contents of the file are encrypted using Base64. Decrypting the string multiple times with a [decoder](https://www.base64decode.org/) will reveal the flag.

## Flag

picoCTF{base64_n3st3d_dic0d!n8_d0wnl04d3d_492767d2}
