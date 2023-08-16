
################ functions with mandatory arguments ########################333
# def myfunction():
#     pass
#
#
# res = myfunction()
# print(res)


# def myfunction():
#     return
#
#
# res = myfunction()
# print(res)

# def sayHelloWorld():
#     print('---- Hello world -------')
#
#
# res= sayHelloWorld()  # calling the function
# print(res)

""" function accept arguments"""


# def sumnum(num1, num2):
#     res = num1 + num2
#     print(res)
#     return res
#
# summ__=sumnum(4,5)
# print(summ__)

""" ----------------------------------------------------------------------"""
# def sumnum(num1, num2):
#     res = num1 + num2
#     print(res)
#     return res
#
# summ__=sumnum("ahmed", "ali")
# print(summ__)


# def sumnum(num1, num2):
#     res = num1 + num2
#     print(res)
#     return res
#
# summ__=sumnum("ahmed", 10)
# print(summ__)



""" define datatype in the arguement scope"""

# def sumnum(num1 :int, num2: int):
#     res = num1 + num2
#     print(res)
#     return res
#
# sumnum(10, 20)
# sumnum('Ahmed', 'Ali')



print(isinstance("Ahmed", int ))

# def sumnum(num1 :int, num2: int):
#     if isinstance(num1, int) and isinstance(num2, int):
#         res = num1 + num2
#         print(res)
#         return res
#     print("------ num1 , num2 should be intgers-------------")
# sumnum(10, 20)
# sumnum(33,'44')
# sumnum(4,4)
#
#
#
#
# def sumnum(num1 :int, num2: int):
#     if num1.isdigit() and num2.isdigit():
#         num1 = int(num1)
#         num2 = int(num2)
#         res = num1 + num2
#         print(res)
#     else:
#         print("--- not valid")
# sumnum(3,4)


"============================functions with optional arguments (default arguments) ========================================="

# def saymessage (name, message='Nice to meet you:::'):
#     print(f'message: {message} to {name}')
#
#
# saymessage('Ahmed', 'Hi')
#
# saymessage('Toka', input('please leave your message : '))
#
# saymessage('Alaa')

""" function with variable number of arguments """



# print('ahmed', 'ali', 'mohamed')
# print()
# print(23,5)

"function accepts zero or more argument"
# def askforstudents(*students):
#     print(students)
#
# askforstudents()
# askforstudents('Ahmed', 'Mohamed', 'omar', 'ali')
# askforstudents('Alaa')
#
print('hello',end='______')
print('world')
# print('ahmed', 'mohamed', sep='|||')


""
""" functions with keyword arguments.===> accept them in dict """

def introduceyourself(**info):
    print(info)


introduceyourself(name='noha', sep='engineering', work='iti', age='')
introduceyourself()
introduceyourself(fname='Toka')


temp = 'My name is {username} , I works at {work}'
print(temp.format(username='Abdelrahman', work='microsoft'))