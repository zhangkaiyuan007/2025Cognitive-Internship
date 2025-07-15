def test1(grade):
  if grade >= 85:
    print('Good')

def test2(grade):
  if grade >= 85:
    print('Good')
  else:
    print('Not good')

def test3(grade):
  if grade >= 85:
    print('Excellent')
  elif grade >= 70:
    print('Good')
  elif grade >= 60:
    print('Pass')
  else:
    print('Failed')

if __name__ == "__main__":
  test1(90)
  test1(70)
  test2(90)
  test2(70)
  test3(90)
  test3(80)
  test3(65)
  test3(50)