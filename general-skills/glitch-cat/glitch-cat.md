# Glitch cat

## Information

- Beginner picoMini 2022
- General Skills
- 100 Points

## Description

Our flag printing service has started glitching!
`$ nc saturn.picoctf.net 55826`

## Hints

1. ASCII is one of the most common encodings used in programming

2. We know that the glitch output is valid Python, somehow!

3. Press Ctrl and c on your keyboard to close your connection and return to the command prompt.

## Solution

Open a Linux terminal and enter `nc saturn.picoctf.net 55826`. Then run python using `print` and the output from the terminal to get the flag.

## Flag

picoCTF{gl17ch_m3_n07_9c42a45d}
