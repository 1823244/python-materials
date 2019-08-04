#еще примеры https://pynative.com/python-range-function/

ran = range(0,20,2)
print('ran = range(0,20,2) : ' + str(ran))

llist = list(ran)
print('llist = list(ran) : ' + str(llist))

res = ran[5]
print('res = ran[5] : ' + str(res))

res = ran[:5]
print('res = ran[:5] : ' + str(res))

res = ran.index(2)
print('res = ran.index(3) : ' + str(res))
