s = {1,2,3,4,5}

e = set() #empty set


# print(s,type(s))

s.add(222)

print(s)

s.remove(2)
print(s)

print(s.pop())
print(s.pop())

s1 = {1,2,3,4,5,13,26,39}
s2 = {1,2,3,5,4,13,26,39}

print(s1.union(s2))
print(s1.intersection(s2))

print(s1-s2)

print(s1.issuperset(s2))