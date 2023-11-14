# useless

## Information

- picoCTF 2023
- General Skills
- 100 Points

## Description

There's an interesting script in the user's home directory

The work computer is running SSH. We've been given a script which performs some basic calculations, explore the script and find a flag.
Hostname: `saturn.picoctf.net`
Port: `62785`
Username: `picoplayer`
Password: `password`

## Hints

(None)

## Solution

Login to the remote instance and in the home directory there should be a script called `useless`. Running the script using `./useless` tells us that we need to read the code. This can be done by `man usless` and the flag is located in the Authors section.

## Flag

picoCTF{us3l3ss_ch4ll3ng3_3xpl0it3d_8504}
