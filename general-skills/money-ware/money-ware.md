# money-ware

## Information

- picoCTF 2023
- General Skills
- 100 Points

## Description

Flag format: picoCTF{Malwarename}
The first letter of the malware name should be capitalized and the rest lowercase.
Your friend just got hacked and has been asked to pay some bitcoins to `1Mz7153HMuxXTuR2R1t78mGSdzaAtNbBWX`. He doesn’t seem to understand what is going on and asks you for advice. Can you identify what malware he’s being a victim of?

## Hints

1. Some crypto-currencies abuse databases exist; check them out!

2. Maybe Google might help.

## Solution

Going on [chainabuse.com](https://www.chainabuse.com/), a report correspondong to the address can be [found](https://www.chainabuse.com/report/a8505449-41bb-4b55-9c0c-7b934a377c65?context=search-address&a=1Mz7153HMuxXTuR2R1t78mGSdzaAtNbBWX&chain=BTC). The description of the report links to a [blog](https://blog.avira.com/petya-strikes-back/) with details about the Petya malware. Therefore the answer is Petya.

## Flag

picoCTF{Petya}
