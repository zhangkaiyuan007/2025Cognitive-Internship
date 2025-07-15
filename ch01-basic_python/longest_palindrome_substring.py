string = input("Enter a string: ")
if string == string[::-1]:
  print(string)
else:
  longest = ""
  for i in range(len(string)):
    for j in range(i, len(string)):
      substring = string[i:j+1]
      if substring == substring[::-1] and len(substring) > len(longest):
        longest = substring
  print(longest)