number = int(input("Enter a number: "))

def narcissistic(number):
  original = number
  a = []
  answer = 0

  while number > 0:
    b = number % 10
    a.append(b)
    number = (number - b) / 10

  for i in range(len(a)):
    answer += a[i]**3

  if int(answer) == original:
    return True
  else:
    return False
  
if narcissistic(number):
  print("This number is narcissistic number")
else:
  print("This number is not narcissistic number")

