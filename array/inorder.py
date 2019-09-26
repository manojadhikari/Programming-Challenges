'''
Take Out Orders: [1, 3, 5]
Dine In Orders: [2, 3, 4, 6]
Served Orders: [1, 2, 3, 4, 6, 5, 3]
'''

def in_order(a, b, c):
  i = 0
  j = 0
  k = 0
  dups = 0

  while k < len(c):
    print("looping")
    if i < len(a) and j < len(b) and c[k] == a[i] and c[k] == b[j]:
      dups += 1
      i += 1
      j += 1
      k += 1

    elif i < len(a) and c[k] == a[i]:
      k += 1
      i += 1
      if dups > 0:
        j += dups
      dups = 0
    elif j < len(b) and c[k] == b[j]:
      k += 1
      j += 1
      if dups > 0:
        i -= dups
      dups = 0
    else:
      return False

  return True


a = [1,3,3,3,5]
b = [2, 3,3,3, 4, 6]
c = [1, 2, 3,3,3, 4, 6, 3,3, 5]

print(in_order(a,b,c))
