# Obedient Cat

## Information

- picoCTF 2021
- General Skills
- 5 Points

## Description

This file has a flag in plain sight (aka "in-the-clear") [Download flag](https://mercury.picoctf.net/static/33996e32dce022205a6a36f69aba56f0/flag).

## Hints

1. Any hints about entering a command into the Terminal (such as the next one), will start with a '$'... everything after the dollar sign will be typed (or copy and pasted) into your Terminal.

2. To get the file accessible in your shell, enter the following in the Terminal prompt: `$ wget https://mercury.picoctf.net/static/33996e32dce022205a6a36f69aba56f0/flag`

3. `$ man cat`

## Solution

Simply type `cat flag` in a Linux terminal in the same directoty as `flag`. The output should be the flag.

Alternatively, open the file and the flag should be there.

## Flag

picoCTF{s4n1ty_v3r1f13d_2aa22101}
