# caesar

## Information

- picoCTF 2019
- Cryptography
- 100 Points

## Description

Decrypt this [message](https://jupiter.challenges.picoctf.org/static/49f31c8f17817dc2d367428c9e5ab0bc/ciphertext).

## Hints

1. caesar cipher [tutorial](https://learncryptography.com/classical-encryption/caesar-cipher)

## Solution

As the title of this challenge suggests, this challenge is all about the Caeser cipher. We are given a file `ciphertext` which contains an ecnrypted version of the flag. _Note: Only the string in between teh curly brackets is encrypted._

```
picoCTF{ynkooejcpdanqxeykjrbdofgkq}
```

We don't know what the shift number is so we must use brute force. This means shifting our encrypted string 26 times and finding the decrypted string which makes the most sense. A python file of this can be found [here](caesar_brute_force.py).

The output from the above program is the following:

```
Shift 0: ynkooejcpdanqxeykjrbdofgkq
Shift 1: xmjnndiboczmpwdxjiqacnefjp
Shift 2: wlimmchanbylovcwihpzbmdeio
Shift 3: vkhllbgzmaxknubvhgoyalcdhn
Shift 4: ujgkkafylzwjmtaugfnxzkbcgm
Shift 5: tifjjzexkyvilsztfemwyjabfl
Shift 6: sheiiydwjxuhkrysedlvxizaek
Shift 7: rgdhhxcviwtgjqxrdckuwhyzdj
Shift 8: qfcggwbuhvsfipwqcbjtvgxyci
Shift 9: pebffvatgurehovpbaisufwxbh
Shift 10: odaeeuzsftqdgnuoazhrtevwag
Shift 11: nczddtyrespcfmtnzygqsduvzf
Shift 12: mbyccsxqdrobelsmyxfprctuye
Shift 13: laxbbrwpcqnadkrlxweoqbstxd
Shift 14: kzwaaqvobpmzcjqkwvdnparswc
Shift 15: jyvzzpunaolybipjvucmozqrvb
Shift 16: ixuyyotmznkxahoiutblnypqua
Shift 17: hwtxxnslymjwzgnhtsakmxoptz
Shift 18: gvswwmrkxlivyfmgsrzjlwnosy
Shift 19: furvvlqjwkhuxelfrqyikvmnrx
Shift 20: etquukpivjgtwdkeqpxhjulmqw
Shift 21: dspttjohuifsvcjdpowgitklpv
Shift 22: crossingtherubiconvfhsjkou
Shift 23: bqnrrhmfsgdqtahbnmuegrijnt
Shift 24: apmqqglerfcpszgamltdfqhims
Shift 25: zolppfkdqeboryfzlkscepghlr
```

Looking at the results, we find a message on shift 22 which says `crossingtherubiconvfhsjkou`. This message alludes to Caesar's crossing of the rubicon and is thus likely plaintext message.Therefore, we have found our flag.

## Flag

picoCTF{crossingtherubiconvfhsjkou}
