# 1_wanna_b3_a_r0ck5tar

## Information

- picoCTF 2019
- General Skills
- 350 Points

## Description

The Rockstar language has changed since this problem was released! Use this Wayback Machine URL to use an older version of Rockstar, [here](https://web.archive.org/web/20190522020843/https://codewithrockstar.com/online).

I wrote you another [song](https://jupiter.challenges.picoctf.org/static/96904d361d61fada5bd2d13536706f9a/lyrics.txt). Put the flag in the picoCTF{} flag format

## Hints

(None)

## Solution

For this question, directly using the transipler [online](https://web.archive.org/web/20190522020843/https://codewithrockstar.com/online) did not work. Therefore, I used [rockstar-py](https://github.com/yyyyyyyan/rockstar-py) which acted as the transpiler for this question. In the terminal, run this command `pip install rockstar-py` to install the package. After installing run rockstar-py with lyrics.txt using `rockstar-py -i lyrics.txt -o lyrics.py`. This should give a new python file, lyrics.py, which is the transpilled code.

```python
Rocknroll = True
Silence = False
a_guitar = 10
Tommy = 44
Music = 170
the_music = input()
if the_music == a_guitar:
    print("Keep on rocking!")
    the_rhythm = input()
    if the_rhythm - Music == False:
        Tommy = 66
        print(Tommy!)
        Music = 79
        Jamming = 78
        print(Music!)
        print(Jamming!)
        Tommy = 74
        print(Tommy!)
        They are dazzled audiences
        print(it!)
        Rock = 86
        print(it!)
        Tommy = 73
        print(it!)
        break
        print("Bring on the rock!")
        Else print("That ain't it, Chief")
        break
```

However, we can clearly see that there will be some syntax errors with this transipiled code. So we need to clean it up.

```python
a_guitar = 10
Tommy = 44
Music = 170
the_music = int(input())
if the_music == a_guitar:
    print("Keep on rocking!")
    the_rhythm = int(input())
    if the_rhythm - Music == 0:
        Tommy = 66
        print(Tommy)
        Music = 79
        Jamming = 78
        print(Music)
        print(Jamming)
        Tommy = 74
        print(Tommy)
        print(Tommy)
        Rock = 86
        print(Rock)
        Tommy = 73
        print(Tommy)
        print("Bring on the rock!")
    else:
      print("That ain't it, Chief")
```

Run the modified lyrics.py program with the inputs `the_music = 10` and `the_rythem = 170` to reveal decimal values. These values can be converted to ASCII characters using a simple script, where we append all decimal values into an array `values` and do the following:

```python
ascii_characters = [chr(value) for value in values]
print("".join(ascii_characters))
```

The output from this is BONJJVI, which is not the flag, however, the output is similar to BONJOVI which is the flag.

## Flag

picoCTF{BONJOVI}
