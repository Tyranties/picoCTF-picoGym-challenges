# Permissions

## Information

- picoCTF 2023
- General Skills
- 100 Points

## Description

Can you read files in the root file?

The system admin has provisioned an account for you on the main server:
`ssh -p 52339 picoplayer@saturn.picoctf.net`
Password: `e3pn6lmvHt`
Can you login and read the root file?

## Hints

1. What permissions do you have?

## Solution

Login to the remote instance using the given `ssh` command and password. Going to the root directory we can see the `challenge` directory, but we cannot access it.

By typing the command `sudo -l`, we can see that we are able to use `vim` from `/usr/bin/vi`. Typing in the command `sudo vi /challenge` will allow us to access the directory. Inside `challenge` we see a file called `metadata.json` which contains the flag.

## Flag

picoCTF{uS1ng_v1m_3dit0r_f6ad392b}
