# Static ain't always noise

## Information

- picoCTF 2021
- General Skills
- 20 Points

## Description

Can you look at the data in this binary: [static](https://mercury.picoctf.net/static/7495259e963bd5b67d0fb8b616652618/static)? This [BASH script](https://mercury.picoctf.net/static/7495259e963bd5b67d0fb8b616652618/ltdis.sh) might help!

## Hints

None

## Solution

In a Linux terminal enter `sh ltdis.sh static`. Two files should then appear in the directory `static.litdis.strings.txt` and `staticsltdis.x86_64.txt`. Open `static.litdis.strings.txt` and the flag should be somewhere in there. For me it was on line 15.

## Flag

picoCTF{d15a5m_t34s3r_f6c48608}
