string = input("Enter a string: ")
a = []

for i in range(len(string)):
  for j in range(i, len(string)):
    substring = string[i:j+1]
    a.append(substring)

print(len(a))

