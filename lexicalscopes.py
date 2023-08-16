

course= 'python' # defined in the global scope ---> global variable
# print(course)
#
# x = 10
# print(course)
#
# def myfun():
#     name = input('please enter name: ')  # any variable defined inside the function
#     # can be accessed only inside it .
#     # name --> scope -->local scope
#     print(f'from inside the function name={name}')
#
#
# myfun()
# # print(name)
# print("-----------------------")


"""--------------------------- access global variable from inside function ------------------------------------"""


# course = 'python'
#
# def printcourse():
#     # you read the value of global variable inside the function
#     print(f"from inside the function {course}")
#
#
#
# printcourse()
#
#
# def modifycourse():
#     global course
#     course = input('please enter course name : ')
#     print(f'form modify course {course}')
#
#
# modifycourse()
# print(course)

""" ------------------------------------------------------------------------"""


# define function inside a function


def myinfo():
    name= 'Mohamed'  # local variable
    def formatname():
        print(name , name.upper())

    # formatname()

    def modifyname():
        nonlocal name
        name= input('please enter name: ') # new local variable for the inner function
        print(f"==== {name}")

    modifyname()
    print(name)


myinfo()














