# chrono

## Information

- picoCTF 2023
- General Skills
- 100 Points

## Description

How to automate tasks to run at intervals on linux servers?

## Hints

(None)

## Solution

Using a Linux terminal use `ssh` to login to the remote instance instance. This is done with `ssh username@server -p port-number`, replacing username, server and port-number with the appropriate values. Once prompted enter the password.

Once logged in, navigate to the root directory with `cd /`, then navigate to the etc directory with `cd etc`. Open the file crontab with `cat crontab` and the flag should be inside the file.

## Flag

picoCTF{Sch3DUL7NG_T45K3_L1NUX_9d5cb744}
