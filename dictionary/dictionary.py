height = {'Jun':174, "Kim":170, 'Lee':165}
print(height)

test = dict()

print(height['Kim'])
print(height['Lee'])
print('Kim' in height)

height["Ihm"] = 167
print(height)

print(height.keys())
print(height.values())
print(height.items())

a = {'kim': [4, 1, 17], 'lee': 170, 'park': 85, 'choi': 'IoT'}

for key in a.keys() :
    print(key)

for val in a.values() :
    print(val)

for key, val in a.items():
    print('key={}, value={}'.format(key, val))

fruits = {'melon':2, 'banana':1, 'plum':0, 'pear':2, 'apple':1}
print(sorted(fruits))

print(sorted(fruits.keys()))

print(sorted(fruits, reverse=True))

print(fruits.items())

print(sorted(fruits.items()))

print(sorted(fruits.items(), key=lambda t: t[1]))

height.pop('Ihm')
print(height)

height.clear()
print(height)