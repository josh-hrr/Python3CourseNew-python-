var1 = 'testing'
print(var1[::-1])

var2 = 'testing2'
i = len(var2) - 1
result = ''

while i >= 0:
  i = i - 1
  print(i)
  result = result + var2[i]

print(result)

#using join
var3 = ' -- '
newJoin = var3.join(['world', 'here'])
print(newJoin)

var4 = 'enter'
print(''.join(reversed(var4)))
