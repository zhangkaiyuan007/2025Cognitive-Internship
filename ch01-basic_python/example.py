import math

def calculate(a, b):
  sum = 0
  for x in range(a, b):
    sum += x
  return math.sqrt(sum)

if __name__ == "__main__":
  a = 2
  b = 5
  c = calculate(a, b)
  print("The square root of sum of numbers [%d, %d) is: %d"%(a, b, c))