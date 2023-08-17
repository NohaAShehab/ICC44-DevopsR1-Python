""" any .py file is considered to be python module
 --> you can import the module
 or import part of the module
"""

print('----------- hello world ----------------------')

def askforint(message='please enter number: '):
    while True:
        num = input(message)
        if num.isdigit():
            return  int(num)
        print(f'===== Invalid input: {message}')

def askforstring(message):
    while True:
        inputstr = input(message)
        if inputstr.isalpha():
            return inputstr
        print(f'--- invalid input: {message}')

# age = askforint('please enter age: ')
if __name__ == '__main__':
    print('--------------------')
    age = askforint('please enter age: ')