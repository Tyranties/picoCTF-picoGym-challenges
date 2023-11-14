# flag_shop

## Information

- picoCTF 2019
- General Skills
- 300 Points

## Description

There's a flag shop selling stuff, can you buy a flag? [Source](https://jupiter.challenges.picoctf.org/static/dd28f0987f28c894f35d5d48564c3402/store.c). Connect with `nc jupiter.challenges.picoctf.org 44566`.

## Hints

1. Two's compliment can do some weird things when numbers get really big!

## Solution

After entering the `nc` command given in the description into a Linux terminal, we are meet with an interface for a flag shop. Entering `1` will reveal our balance, `2` for buying flags and `3` to exit the shop. If we press `1` we see our balance is 1100. If we press `2` we get to buy two flags "Defintely not the flag Flag" which costs 900 and "1337 Flag" which is the flag we want, however it costs 100000.

Buy the "Defintely not the flag Flag" and you will be prompted to enter the quantity to buy. Here we enter a large positive number that is less than 2147483647. If you've done it correctly then the final cost shown should be a negative number and thus add money to our balance. Once you have 100000 you can buy the "1337 Flag" for the flag for this challenge.

## Flag

picoCTF{m0n3y_bag5_68d16363}
