tupl = (1,2,3,"sea")
print("tupl = (1,2,3,'sea') : " + str (  tupl ))

tupl1 = (1)
print("tuple of 1 element : " + str (  tupl1 ))

llist = list('example for tuple 234')
print ('source list: '+str(llist))
tupl = tuple(llist)
print("tupl = tuple(llist) : " + str (  tupl ))

res = len(tupl)
print("res = len(tupl) : " + str (  res ))

res = min(tupl)
print("res = min(tupl) : " + str (  res ))

res = max(tupl)
print("res = max(tupl) : " + str (  res ))

t2 = tupl+(5,5,5)
print("t2 = tupl+(5,5,5) : " + str (  t2 ))



print('iterating: for x in t2: print(x)')
for x in t2:
	print(x)
	
	
	
# это должно быть последним, т.к. вызывает исключение
del t2
print("del t2 : " + str (  t2 ))
