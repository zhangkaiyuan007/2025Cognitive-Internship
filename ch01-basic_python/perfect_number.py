m = int(input("The given range: "))
def is_perfect(n):
  a = [1]
  if n == 1:
    return True
  for i in range(2, n):
    if n % i == 0:
      a.append(i)
  if n == sum(a):
    return True
  else:
    return False
  
b = []
for i in range(1, m+1):
  if is_perfect(i):
    b.append(i)
  else:
    continue

print(b)
