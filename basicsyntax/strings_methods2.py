"""
Examples to show available string methods in python
"""

# Replace Method
a = "1abc2abc3abc4abc"
print(a.replace('abc', 'ABC'))

# Sub-Strings
# starting index is inclusive
# Ending index is exclusive
sub = a[1:6]
step = a[1:6:2]

print("****************")

print(sub)
print(step)


a = "one two three"
l = ['one', 'two', 'three']
print (a)
print (l)

l=a.split()
print(l)


print("***************")
s = "Pies, lis i 2 koty"

lista = s.split()

print (lista)

s1 = "*".join(lista)

print (s1)