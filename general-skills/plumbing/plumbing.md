# plumbing

## Information

- picoCTF 2019
- General Skills
- 200 Points

## Description

Sometimes you need to handle process data outside of a file. Can you find a way to keep the output from this program and search for the flag? Connect to `jupiter.challenges.picoctf.org 14291`.

## Hints

1. Remember the flag format is picoCTF{XXXX}

2. What's a pipe? No not that kind of pipe... This [kind](http://www.linfo.org/pipes.html)

## Solution

To save the output from the program we type the command `nc jupiter.challenges.picoctf.org 14291 > output.txt` and the output would be save in `output.txt`. After running for around 10 seconds, close the pipie using `^d` and then use `grep "picoCTF" output.txt` to find the flag.

## Flag

picoCTF{digital_plumb3r_ea8bfec7}
