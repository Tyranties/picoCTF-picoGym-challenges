# Mod 26

## Information

- picoCTF 2021
- Cryptography
- 10 Points

## Description

Cryptography can be easy, do you know what ROT13 is? cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_Ncualgvd}

## Hints

1. This can be solved online if you don't want to do it by hand!

## Solution

ROT13 (ROTate by 13 places) is an encryption method that is a special case of the Caesar cipher in which a letter is substituted with the 13th letter after it. Read more [here](https://en.wikipedia.org/wiki/ROT13).

To solve this, we can either use an online rot13 decoder, solve by hand, or write a simple script. This [script](rot13-decryption.py) is the one I used for this challenge.

## Flag

picoCTF{next_time_I'll_try_2_rounds_of_rot13_Aphnytiq}
