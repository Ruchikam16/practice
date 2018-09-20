import collections
dict1=collections.OrderedDict()
dict1['a']='ruchika'
dict1['d']='prateek'
dict1['b']='hello'
dict1['c']='world'
print("ordered dict")
for k,v in dict1.items():
    print(k ,':' ,v)
    

dict2=collections.OrderedDict(sorted(dict1.items()))
print("sorted ordered dict")
for k,v in dict2.items():
    print(k ,':' ,v)
    
dict3=collections.OrderedDict(sorted(dict1.items(), key=lambda v :v[1]))
print("ordered dict  sorted by Value")
for k,v in dict3.items():
    print(k ,':' ,v)

#In Python3 since unpacking is not allowed [1] we can use
#x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
#sorted_by_value = sorted(x.items(), key=lambda kv: kv[1])
