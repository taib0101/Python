str1 = "Mustain Murtaza "
str1 += "Taib"
print(str1)
print(str1.upper())
print(str1.lower())
print("taib".capitalize())

print("Bro Taib".split())
print(str1[0:8])
print(str1.replace("Mustain", 'Bro'))
print(len(str1))
print(str1[::-1])
print(str1.index('s'))

str1 = str1.replace('b', '')

for value in str1:
    print(value)