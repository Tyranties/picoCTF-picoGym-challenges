# Wave a flag

## Information

- picoCTF 2021
- General Skills
- 10 Points

## Description

Can you invoke help flags for a tool or binary? [This program](https://mercury.picoctf.net/static/cfea736820f329083dab9558c3932ada/warm) has extraordinarily helpful information...

## Hints

1. This program will only work in the webshell or another Linux computer.

2. To get the file accessible in your shell, enter the following in the Terminal prompt: `$ wget https://mercury.picoctf.net/static/cfea736820f329083dab9558c3932ada/warm`

3. Run this program by entering the following in the Terminal prompt: `$ ./warm`, but you'll first have to make it executable with `$ chmod +x warm`

4. -h and --help are the most common arguments to give to programs to get more information from them!

5. Not every program implements help features like -h and --help.

## Solution

In a Linux terminal type `./warm -h` and the output should be in the form:

```
Oh, help? I actually don't do much, but I do have this flag here: x
```

where x is the flag.

## Flag

picoCTF{b1scu1ts_4nd_gr4vy_30e77291}
