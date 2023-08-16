
## unlabeled data
info = ['Noha', 31, 'Engineering', 'iti', 'Computer science']

### dictionary ---> comma seperated key:value pair
## doesn't allow key duplication

"1- define dict"
d = {}
myd = dict()
print(type(d), type(myd))


""
info = {"name":'noha', 'track':'devops', 'age':31, 'sep':"Engineering", 'name':"Noha Shehab"}

""" get len of dict """
print(len(info))

""" access elements in dict using key """
print(info['age'])

info['city']= 'Mansoura'  # if key doesn't exists 00> will the new key value pair
print(info)

""" check if element exists in the dict ? """

print('Noha Shehab' in info) # False  # in operator --> check if elements exists in the keys

'loop over the dict '

for item in info:
    print(item)

" get keys of dicts"
dkeys = info.keys() # dict_keys --> you cast it to a list
print(dkeys)
dkeys = list(dkeys)
print(dkeys)

"get the values"
dvalues = info.values() # dict_keys --> you cast it to a list
print(dvalues)
dvalues = list(dvalues)
print(dvalues)

"""get dict items ? """

ditems = info.items()
print(ditems)
ditems = list(ditems)
print(ditems)

for k, v in ditems:
    print(f"key = {k}, value={v}")

'you can access dict elements using key '

# print(info[0])

std_info= {"fname":"Abdelrahman", 'lname':"Sayed", 'courses':['Python', 'docker']}

print(std_info['courses'][1])

# std_info.clear()
# print(std_info)
