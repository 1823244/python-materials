dddd = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6,}
print ('source dict: '+str(dddd))

dddd2 = dict([('zero',0),('nine',9)])
print ('source dict 2: '+str(dddd2))

dddd['one'] = 2
print ('dddd["one"] = 2 : '+str(dddd))

dddd['seven'] = 7
print ('add key: dddd["seven"] = 7 : '+str(dddd))

# здесь будет ошибка, т.к. чтение по отсутствующему ключу невозможно
#res = dddd["eight"]
#print ('read absent key: res = dddd["eight"] : '+str(res))

del dddd["seven"]
print ('del key: del dddd["seven"] : '+str(dddd))

# ошибка. обращение к переменной после удаления невозможно
#del dict
#print(dict)

dddd2.clear()
print ('clear dddd2.clear() : '+str(dddd2))

dddd2 = {"one": 1, "one": 2, "two":2}
print ('dup: dddd2 = {"one": 1, "one": 2, "two":2} : '+str(dddd2))

res = len(dddd2)
print('res = len(dddd2) : ' + str(res))

res = type(dddd2)
print('res = type(dddd2) : ' + str(res))

newcopy = dddd2.copy()
print('newcopy = dddd2.copy() : ' + str(newcopy))

seq = ('name','sex','age',)
dseq = dict.fromkeys(seq, 'yes')
print('dseq = dict.fromkeys(seq) : ' + str(dseq))

res = dseq.get("address", "no")
print('res = dseq.get("address", "no") : ' + str(res))

res = dseq.items()
print('res = dseq.items() : ' + str(res))
lres = list(res)
print('для обхода dict_items надо создать list. list[0] (tuple) : ' + str(lres[0]))
print('type(lres[0]) : ' + str(type(lres[0])))

res = dseq.keys()
print('res = dseq.keys() : ' + str(res))
lres = list(res)
print('type(res) : ' + str(type(res)))
print('для обхода dict_keys надо создать list. list[0] (string) : ' + str(lres[0]))
print('type(lres[0]) : ' + str(type(lres[0])))

res = dseq.setdefault("address", "no")
print('res = dseq.setdefault("address", "no") : ' + str(res))
print('dseq  : ' + str(dseq))

res = dseq.setdefault("age", "no")
print('res = dseq.setdefault("age", "no") : ' + str(res))
print('dseq  : ' + str(dseq))

dddd.update(dseq)
print('dddd.update(dseq) : ' + str(dddd))

res = dddd.values()
print('res = dddd.values() : ' + str(res))
lres = list(res)
print('type(res) : ' + str(type(res)))
print('для обхода dict_values надо создать list. list[0] : ' + str(lres[0]))
print('type(lres[0]) : ' + str(type(lres[0])))


res = dddd.pop("four")
print('res = dddd.pop("four") : ' + str(res))
print('dddd : ' + str(dddd))

res = dddd.pop("ten", 12) # если не указать default(12), будет ошибка, т.к. ключа 'ten' в словаре нет
print('res = dddd.pop("ten") : ' + str(res))
print('dddd : ' + str(dddd))

res = dddd.popitem()
print('res = dddd.popitem() : ' + str(res))
print('type(res) : ' + str(type(res)))
print('dddd : ' + str(dddd))

it = iter(dddd) # dict_keyiterator
print('it = iter(dddd) : ' + str(it))

print('for x in dddd:')
for x in dddd:
	print(x)
	
print('for x in it:')
for x in it:
	print(x)

it = iter(dddd.values())
print('it = iter(dddd) : ' + str(it))
print(next(it))



