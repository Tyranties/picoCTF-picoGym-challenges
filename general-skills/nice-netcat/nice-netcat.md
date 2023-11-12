# Nice netcat...

## Information

- picoCTF 2021
- General Skills
- 15 Points

## Description

There is a nice program that you can talk to by using this command in a shell: `$ nc mercury.picoctf.net 35652`, but it doesn't speak English...

## Hints

1. You can practice using netcat with this picoGym problem: [what's a netcat](https://play.picoctf.org/practice/challenge/34)?

2. You can practice reading and writing ASCII with this picoGym problem: [Let's Warm Up](https://play.picoctf.org/practice/challenge/22)

## Solution

In a Linux terminal enter, `nc mercury.picoctf.net 35652`.

The output for me was:

```
112
105
99
111
67
84
70
123
103
48
48
100
95
107
49
116
116
121
33
95
110
49
99
51
95
107
49
116
116
121
33
95
57
98
51
98
55
51
57
50
125
10
```

The numbers represent ASCII digits in the form of decimal numbers. After converting all digits to ASCII characters you will get the flag.

`netcat.py` converts all ASCII digits into ASCII characters.
`netcat-output.txt` is a text file containing the netcat output.

## Flag

picoCTF{g00d_k1tty!\_n1c3_k1tty!\_9b3b7392}
