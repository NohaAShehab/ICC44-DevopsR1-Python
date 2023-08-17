


# def divnums(num1, num2):
#     if num2==0:
#         raise ZeroDivisionError("---- not valid divided by ")
#     print(f'num1= {num1}, num2={num2}')
#     res  = num1/ num2
#     print( res)
#
# divnums(5,0)


message = 'ooo ____ 355'
# print(message.replace('o', 0))


def sumnum(num1, num2):
    if not(isinstance(num1, int) and isinstance(num2, int)):
        print("--------- please restart the system -------------")
        raise TypeError("num1, num2 should integers")
    print(num1 + num2)

sumnum('tt', 'ttt')