llist = list('list')
print ('source list: '+str(llist))

obj = '-example'
print ('obj: '+str(obj))
seq = '+seq'
print ('seq: '+str(seq))
index = 2
print ('index: '+str(index))

llist.append(obj) # Добавляет объект obj в список
print ('after append(): '+str(llist))

cnt = llist.count(obj) # Возвращает кол-во, сколько раз obj входит в список
print('count(obj): '+str(cnt))

llist.extend(seq) # Добавляет содержимое seq  в список
print ('after extend(): '+str(llist))

ndx = llist.index(obj) # Возвращает наименьший индекс в списке, который появляется в obj
print('index(obj): '+str(ndx))

llist.insert(index, obj) # Вставки объект obj в список по смещению index
print ('after insert(): '+str(llist))

ppp = llist.pop() # Удаляет и возвращает последний объект или obj из списка
print('pop(): '+str(ppp))

llist.remove(obj) # Удаляет объект obj из списка
print ('after remove(): '+str(llist))

llist.reverse() # Меняет объекты списка на месте
print ('after reverse(): '+str(llist))

llist.sort() # Сортирует объекты списка
print ('after sort(): '+str(llist))

ln = len(llist)
print ('len(llist): '+str(ln))

li2 = llist.copy()
print ('li2 = llist.copy(): '+str(li2))

li2.clear()
print ('li2 = li2.clear(): '+str(li2))

li2 = llist.copy()

res = 's' in li2
print ('res = "s" in li2: '+str(res))

res = 'w' not in li2
print ('res = "w" not in li2: '+str(res))

w = list('fasdf')
li3 = li2 + w
print(" w = list('fasdf') ")
print ('li3 = li2 + w: '+str(li3))

li2 = li2 * 2
print ('li2 = li2 * 2: '+str(li2))

res = li2[3]
print ('res = li2[3]: '+str(res))

res = li2[-3]
print ('res = li2[-3]: '+str(res))

res = li2[3:8]
print ('res = li2[3:8]: '+str(res))

res = li2[3:8:2]
print ('res = li2[3:8:2]: '+str(res))

res = min(li2)
print ('res = min(li2): '+str(res))

res = max(li2)
print ('res = max(li2): '+str(res))

del li2[3:5]
print ('del li2[3:5]: '+str(li2))

li2[3] = 'replaced'
print ('li2[3] = "replaced": '+str(li2))

lreplace = list('reebok')
li2[4:10] = lreplace
print ('lreplace = list("reebok"): '+str(lreplace))
print ('li2[4:10] = lreplace: '+str(li2))

lreplace = list('123')
li2[4:10:2] = lreplace
print ('lreplace = list("123"): '+str(lreplace))
print ('li2[4:10:2] = lreplace: '+str(li2))

del li2[4:8:2]
print ('del li2[4:8:2]": '+str(li2))

res = li2[:]
print ('res = li2[:]": '+str(res))

print('iterating: for x in li2: print(x)')
for x in li2:
	print(x)
