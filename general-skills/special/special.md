# special

## Information

- picoCTF 2023
- General Skills
- 300 Points

## Description

Don't power users get tired of making spelling mistakes in the shell? Not anymore! Enter Special, the Spell Checked Interface for Affecting Linux. Now, every word is properly spelled and capitalized... automatically and behind-the-scenes! Be the first to test Special in beta, and feel free to tell us all about how Special streamlines every development process that you face. When your co-workers see your amazing shell interface, just tell them: That's Special (TM)
Start your instance to see connection details.
`ssh -p 58491 ctf-player@saturn.picoctf.net`
The password is `af86add3`

## Hints

1. Experiment with different shell syntax

## Solution

Once logged in to the remote instace we find out that we cannot use the typical shell syntax, for example `ls` in Special is `Is`. Therefore we need to use a differnet shell syntax if we want to solve this challenge.

Using the syntax `${parameter=x}`, where x is the command solves this problem.

Therefore we can type `${parameter=ls}` to view the contents of the directory. The directory we are in currently has one sub-directory called `blargh`. Using the command `${parameter=ls blargh}` reveals a file inside `blargh` called `flag.txt`. To open `flag.txt` we write `${parameter= cat blargh/flag.txt}` into the terminal where the output will be the flag.

## Flag

picoCTF{5p311ch3ck_15_7h3_w0r57_6a2763f6}
