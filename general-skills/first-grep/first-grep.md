# First Grep

## Information

- picoCTF 2019
- General Skills
- 100 Points

## Description

Can you find the flag in [file](https://jupiter.challenges.picoctf.org/static/315d3325dc668ab7f1af9194f2de7e7a/file)? This would be really tedious to look through manually, something tells me there is a better way.

## Hints

1. grep [tutorial](https://ryanstutorials.net/linuxtutorial/grep.php)

## Solution

In a linux terminal type `grep 'picoCTF file` which searches the file for any string containing 'picoCTF' which is the flag.

## Flag

picoCTF{grep_is_good_to_find_things_f77e0797}
