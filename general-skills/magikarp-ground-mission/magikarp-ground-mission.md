# Magikarp Ground Mission

## Information

- picoCTF 2021
- General Skills
- 30 Points

## Description

Do you know how to move between directories and read files in the shell? Start the container, `ssh` to it, and then `ls` once connected to begin. Login via `ssh` as `ctf-player` with the password, `b60940ca`

SSH `ssh ctf-player@venus.picoctf.net -p 53967`

## Hints

1. Finding a cheatsheet for bash would be really helpful!

## Solution

Launch the instance and login using `ssh` and the provided password. Once logged in, use the `ls` command to find the first part of the flag. In the same directory there are instruictions to find the second part of the flag by going to the root directory using `/`. There you will find the second part of the flag along with instructions to find the third part of the flag by going to the home directory using `~`. At the root directory you will find the third part of the flag. After finding all three parts concatenate the three parts to form the complete flag.

## Flag

picoCTF{xxsh*0ut_0f*\/\/4t3r_c1754242}
