i = 0
j = 0
string = "My name is ilhan"

print(len(string))

while i < 10 :
    print(string)
    i = i+1

print(string[0])

print(string[:4])
print(string[-4:])

j = 1
destring = ""
while j <= len(string) :
    destring += string[0 - j]
    j += 1

print(destring)


print(string[1:15])

print(string.upper())

print(string.lower())

print(string.replace('a', 'e'))