""" tuple --> sequence based datatype  --> immutable datatype"""
""" 1- define a tuple"""
t = ()
myt = tuple()
#
""" empty tuple are falsy value """
#
#
""" 2- tuple can hold different data from different datatypes"""
#
names = ('Ahmed', 'Habiba', 'Nada', 'Shereen', 29, 2023, 15, True, 'iti', 'devops','iti',9.8)
print(names)
#
"3- get len elements of tuple "
print(len(names))

"4- access element in the tuple using index "
print(names[5])
# names[5] = 'updated'  # tuple is immutable datatype3
# # TypeError: 'tuple' object does not support item assignment
# # print(names)
#
"5- count element occurence in the tuple"
print(names.count('iti'))
#
'6- get index of element '
print(names.index('iti'))

'7- check element existence '
print('noha' in names)






""" common tuple operations """

"1- concat"
# t1 =('python', 'django', 'AWS')
# courses = ('Kubernates', 'docker', 'ansible')
#
# devops = t1 + courses
# print(devops)
#


# t = tuple([5, 6, 7])
# t3 = ("a", 5, "test", True, t)
# print(t3[4][2])


# l = list([5, 6, 7])
# t3 = ("a", 5, "test", True, l)
# print(t3[4][2])
# t3[4].append('iti')
# print(t3)



""" min , max ---> tuple items must be from the same type"""
# print(min(t1))
# #
'loop over the tuple '

# for item in names:
#     print(f'item = {item}')
# count = 0
# for item in names:
#     print(f'item = {item}, {count}')
#     count +=1
#
# "enumrate function --> create index for iterable "
# for index, item in enumerate(names):
#     print(f"index ={index}, item = {item}")

#
# ## generate tuple of numbers
#
#
#
#
num = range(0, 10, 2)
print(num)
nums= tuple(num)
print(nums)


"tuple of one item ? "

myt = ('iti',)
print(myt, type(myt))


"casting list to tuple and viceversa"

names = ['Mahmoud', 'Seif', 'Abdelrahman']  # list
names.append('Nada')
names = tuple(names)  # tuple

#############################
newlist = list(names)
print(newlist)

print(list('Hussien'))

'name'.capitalize()