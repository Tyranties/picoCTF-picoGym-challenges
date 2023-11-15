# Specialer

## Information

- picoCTF 2023
- General Skills
- 400 Points

## Description

Reception of Special has been cool to say the least. That's why we made an exclusive version of Special, called Secure Comprehensive Interface for Affecting Linux Empirically Rad, or just 'Specialer'. With Specialer, we really tried to remove the distractions from using a shell. Yes, we took out spell checker because of everybody's complaining. But we think you will be excited about our new, reduced feature set for keeping you focused on what needs it the most. Please start an instance to test your very own copy of Specialer.
`ssh -p 58695 ctf-player@saturn.picoctf.net`. The password is `fd7746b4`

## Hints

1. What programs do you have access to?

## Solution

Login to the remote instance using the given `ssh` command and the password. Initially login will reveal you cannot use some command such as `ls`. Use the command `compgen -c` or double press `tab` to view all commands you are allowed to use.

To view all the contents of the current directory use the command `echo *`, which should reveal three directories: `abra`, `ala` and `sim`.

Navigate to the `ala` directory using `cd ala` and using `echo *` again should reveal two text files: `kazam.txt` and `mode.txt`.

The flag is located in `kazam.txt` and to open the file use the command `echo "$(<kazam.txt)"`.

## Flag

picoCTF{y0u_d0n7_4ppr3c1473_wh47_w3r3_d01ng_h3r3_38f5cc78}
