str = 'Hello, IoT'

for i in range(0, 3, 1):
    print(str)

print(str[0:4])
print(str[-4:])
print(str.lower())

j = 1
destring = ""
while j <= len(str) :
    destring += str[0 - j]
    j += 1

print(destring)

