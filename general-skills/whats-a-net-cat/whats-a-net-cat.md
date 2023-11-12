# what's a net cat?

## Information

- picoCTF 2019
- General Skills
- 100 Points

## Description

Using netcat (nc) is going to be pretty important. Can you connect to `jupiter.challenges.picoctf.org` at port `25103` to get the flag?

## Hints

1. nc [tutorial](https://linux.die.net/man/1/nc)

## Solution

In a Linux terminal type `nc jupiter.challenges.picoctf.org 25103` and the output should be of the form:

```
You're on your way to becoming the net cat master
x
```

where x is the flag.

## Flag

picoCTF{nEtCat_Mast3ry_d0c64587}
