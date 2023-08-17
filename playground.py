#
#
# def askforint(message='please enter number: '):
#     while True:
#         num = input(message)
#         if num.isdigit():
#             return  int(num)
#         print(f'===== Invalid input: {message}')
#
#
# def calculator():
#     num1 = askforint("num1 = ")
#     num2 = askforint("num2 = ")
#     return num1 + num2
#
# print(calculator())

#####################################################
""" import module """
# import inputsmodule
#
# def calculator():
#     num1 = inputsmodule.askforint("num1 = ")
#     num2 = inputsmodule.askforint("num2 = ")
#     return num1 + num2
#
# print(calculator())
#
#
# name = inputsmodule.askforstring('please enter name: ')
# print(name)

""" alias module name """
# import inputsmodule as inputt
#
# def calculator():
#     num1 = inputt.askforint("num1 = ")
#     num2 = inputt.askforint("num2 = ")
#     return num1 + num2
#
# print(calculator())
#
#
# name = inputt.askforstring('please enter name: ')
# print(name)
#

""" import part of the module """

# from inputsmodule import  askforstring
#
# print(askforstring('please enter mood: '))

""" ----------------------------------"""
from inputsmodule import  askforstring as moodfunction

# print(askforstring('please enter mood: '))
# print(moodfunction('please enter mood: '))

"""
    package ==== directory 
    contains set of modules
"""

##################
""" import module from package """
""" import packagename.modulename"""
# import  devops.artihemticmodule
#
# devops.artihemticmodule.sumnum(3,5)

# import  devops.artihemticmodule as dv
#
# dv.sumnum(3,5)

'import part of the module from package '

# from devops.artihemticmodule import  sumnum
# sumnum(34,5)

''' import from iti package '''

# import  iti.greetingmodule

# iti.greetingmodule.sayhello('Hadeer')

""" get function from package """
# from iti import sayhello
#
# sayhello('hhhhh')

#
# from iti import sayhello
# sayhello('rrrr')

from iti.shortcuts import  helloworld

import testmain


import iti
print('-----------------------')
from iti.greetingmodule import sayhello
print('-----------------------------')
sayhello('grrr')
iti.greetingmodule.sayhello('ooo')

