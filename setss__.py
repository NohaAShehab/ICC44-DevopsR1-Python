

# allow only items from hashable datatypes -->
# un-ordered datatype
# doesn't allow duplication
# mutable

info = ['Hossam', 'Sheikh Zayed']

"to define empty set "
ss = set()

myset = {"GCP", "Machine learning", 'Generative learning', 'Hekam AlAteya',100
        ,("python", 'django'),  "Machine learning"}
print(myset)
#
myset.add('new element ')
print(myset)

""" pop element from set """
# popped_element = myset.pop()
# print(popped_element)


""" remove element from set"""
myset.remove('GCP')
print(myset)

""" loop over the set """
for element in myset:
    print(element)

'len, in '
print(len(myset))

courses = {"django", 'odoo', 'Terraform'}
print(myset.update(courses))
print(myset)

# myset.add(courses)

# "cast list to a set"
grades = [80, 70, 60 , 50 ,60,70, 90, 70 ]

print(set(grades))