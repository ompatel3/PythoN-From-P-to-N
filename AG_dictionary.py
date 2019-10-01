print("keys of dictionary are imutable")
d={}
print(type(d))
d1={"arpit":'blue','bittu':'black','ankit':'pink'}
print(d1.keys())
print(d1.values())
d1["newDict"]="{'a':'apple','b':'boy','c':'cat'}"
print(d1)
print(d1['newDict'])


d_new=d1.copy()
d_new['naya']='ye naya hai'
print(d1)
print(d_new)

del d1['ankit']
print(d1)