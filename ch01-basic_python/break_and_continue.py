def test1():
  n = 0
  while n < 7:
    n = n + 1
    print(n)
  print("While-Loop End!")
  print("The final n is: %d" % (n))

def test2():
  n = 0
  while n < 7:
    n = n + 1
    if n >= 3 and n <= 5:
      break
    print(n)
  print("While-Loop End!")
  print("The final n is: %d" % (n))

def test3():
  n = 0
  while n < 7:
    n = n + 1
    if n >= 3 and n <= 5:
      continue
    print(n)
  print("While-Loop End!")
  print("The final n is: %d" % (n))

if __name__ == "__main__":
  test1()
  test2()
  test3()