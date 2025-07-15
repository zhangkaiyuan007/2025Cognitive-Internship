def foo1(a, b):
  d = a + b

def foo2(a, b):
  global c
  c = a + b

f = lambda a, b: a + b

if __name__ == "__main__":
  print(type(f))
  foo2(1, 2)
  print(c)
  foo1(1, 2)
  print(d)
  # The first function foo1 does not define d, so it will raise an error.
  # The second function foo2 defines c as a global variable, so it will print the value of c.