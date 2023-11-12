flag = ""

with open('netcat-output.txt', 'r') as file:
    for line in file:
        decimal_number = int(line.strip())
        character = chr(decimal_number)
        flag += character

file.close()

print(flag)