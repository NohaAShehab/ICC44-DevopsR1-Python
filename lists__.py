
""" 1- define a list"""
l = []
myl = list()

""" empty list are falsy value """


""" 2- list can hold different data from different datatypes"""

names = ['Ahmed', 'Habiba', 'Nada', 'Shereen', 29, 2023, 15, True, 'iti', 'devops','iti',9.8]
print(names)

"3- get len elements of list "
print(len(names))

"4- access element in the list using index "
print(names[5])
names[5] = 'updated'  # list is mutable datatype
print(names)
# names[20]='iii' # list assignment index out of range

"5- count element occurence in the list"
print(names.count('iti'))

'6- get index of element '
print(names.index('iti'))

'7- check element existence '
print('noha' in names)

'8- appending element in the list'
names.append('Abderahman sayed')
print(names)

'9- insert element at specific index '
names.insert(50, 'Hossam')
print(names)
names.insert(3, 'nada')
print(names)

"remove elements "
'1- pop element '
popped_element=names.pop()
print(names)
print(popped_element)

'2- pop element at certain index '
popped_element=names.pop(5)  #
print(names)
print(popped_element)

'3- remove element --> the first occurence '
print(names.remove('iti'))


""" common list operations """

"1- concat"
l1 =['python', 'django', 'AWS']
courses = ['Kubernates', 'docker', 'ansible']

devops = l1 + courses
print(devops)

'2- extend a list ? '
l1.extend(courses)
print(l1)


'3- sort list  ===> list items must be from the same type '
print(courses)
courses.sort()
print(courses)
courses.sort(reverse=True)
print(courses)
# sorted

'reverse a list'
print(names)
names.reverse()
print(names)


l = list([5, 6, 7])
l3 = ["a", 5, "test", True, l]
print(l3[4][2])


""" min , max ---> list items must be from the same type"""
print(min(l1))

'loop over the list '

# for item in names:
#     print(f'item = {item}')
# count = 0
# for item in names:
#     print(f'item = {item}, {count}')
#     count +=1

"enumrate function --> create index for iterable "
for index, item in enumerate(names):
    print(f"index ={index}, item = {item}")


## generate list of numbers




num = range(0, 10, 2)
print(num)


for i in num:
    print(f"i = {i}")


if 'iti' and 'test':  # logical expression
    print("hii")
else:
    print('bye')


nums = list(num)
print(nums)

