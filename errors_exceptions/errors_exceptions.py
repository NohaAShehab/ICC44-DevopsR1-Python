"""
    errors
        1- syntax error ((parser --> interpreter ))--> must be solved
        2- logical error
        3- runtime error

"""

"""
Developer --- (())
to detect logical --> write unit testing  ,,, 
debugger 
"""
# def sumnum(num1, num2):
#     print(num1 * num2)

# sumnum(2, 2)
# sumnum(20, 2)
num=10
"""runtime error  --> exceptions 
    unexpected actions caused the application to stop
    
"""

print("--------- Welcome to errors and exceptions --------------")

print("------------------------ hello world -----------")
# print(name) # NameError
print('############################')

# num = int(input('please enter age ')) #ValueError: invalid literal for int() with base 10: 'ueiryiuweyriyweiy'
# print(num, type(num))


# dealing with files, db connections, network
# print(6/0) #ZeroDivisionError: division by zero
# """ ---------- try --- except """
#
# try:
#     num = int(input("please enter number : "))
#     print(num)
# except:
#     print("---- problem happened ")
#
# print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")




""" ---------- try --- except """

# try:
#     num = int(input("please enter number : "))
#     print(10/num)
# except Exception as e:
#     print(f"---- problem happened {e}")
#
# print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
import abcccccccccccccc
#### order alphabetically
# import built-in modules

## import modules from installed package

# import userdefined module


# try:
#     num = int(input("please enter number : "))
#     print(10/num)
# except ValueError as ve:
#     print(f"---- {ve}---")
#     print("--- we cannot complete the process because not valid input number: ")
#
# except ZeroDivisionError as ze:
#     print(ze)
#     print("------------- Division by zero results in infinity")
# except Exception as e:
#     print(e)
# print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")


# try:
#     num = int(input("please enter number : "))
#     res = 100/num
# except ValueError as ve:
#     print(f"---- {ve}---")
#     print("--- we cannot complete the process because not valid input number: ")
#
# except ZeroDivisionError as ze:
#     print(ze)
#     print("------------- Division by zero results in infinity")
# except Exception as e:
#     print(e)
# else:
#     print("---- this block will be executed if there is no problems")
#     print(res)
# finally:
#     print("--------- this code will be executed always -----------")
# print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")



def askforInt():
    try:
        num = int(input('please enter number '))
    except Exception as E:
        return None
    else:
        return num
    finally:
        # the content of this block will be executed before any return
        print("---------- process completed --------")
    print("------------------------------")

print(askforInt())






