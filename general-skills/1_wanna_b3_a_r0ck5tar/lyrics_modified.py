values = []

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
        values.append(Tommy)
        Music = 79
        Jamming = 78
        print(Music)
        values.append(Music)
        print(Jamming)
        values.append(Jamming)
        Tommy = 74
        print(Tommy)
        values.append(Tommy)
        print(Tommy)
        values.append(Tommy)
        Rock = 86
        print(Rock)
        values.append(Rock)
        Tommy = 73
        print(Tommy)
        values.append(Tommy)
        print("Bring on the rock!")
    else:
      print("That ain't it, Chief")

ascii_characters = [chr(value) for value in values]
print("".join(ascii_characters))