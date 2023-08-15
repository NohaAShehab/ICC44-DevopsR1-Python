
""" 1- define string """
name = ''  # sequence of chars
" string is immutable  ---> cannot be changed "

"2- get len of the string "
track = '#devops#'
print(len(track))

"3- count no of char in the string "
print(track.count('o'))

"4- check existance of char in the string "
print('m' in track)

"5- string is treated like an array --. access string parts using index start from 0"
print(track[2])
print(track[2:])
print(track[::])
print(track[::-1])


"6- get index of char in the string ?--> get index of the first occurence of the char ? "
print(track.index('#'))

"7- loop over the string?"
for char in track:
    print(char)


print('------------------')


print(char)



""" accept user input """
""" input function always  return with  string """
# name = input('please enter name: ')
# print(name , type(name))
# age = input("please enter age: ")
# print(age, type(age))
#
#
# """ examine string content """
#
#
# print(age.isdigit())  # return True if the string consists only from digits 0-->9
# print(age.isalpha())  # return True of the string consists only from alphas a->z
# print(age.isspace()) # retrun true if the string consists only from spaces
# print(age.isnumeric()) # # return True if the string consists only from digits 0-->9 --> subscript, superscript
# print(age.isupper())
# print(age.islower())


# num1 = int(input("please enter num1: "))
# print(num1)

# num = input("please enter num: ")
# if num.isdigit():
#     num = int(num)
# else:
#     print('please enter valid number : ')
#     exit()

#######################################
"""
    Never Trust user input 
    Keep it simple and stupid

"""

""" formating string """
"1- string concat"
fname = 'noha '
midname= 'abdelhady '
lname ='shehab'

fullname= fname + midname + midname + lname  # + operator concat only strings
print(fullname)


"2- string interpolation "
fullname= fname + midname *2 + lname  # + operator concat only strings
print(fullname)

""" format string to capital for each word"""
## string immuatable --> return new string
print(fullname.title())
print(fullname.capitalize())
print(fullname.upper())
print(fullname.lower())


"---> format "
no_of_studnets=  29
track = 'devops'
# message = 'we have {0} happy students in {1} track'
# print(message.format(no_of_studnets, track))
# print(message.format(track, no_of_studnets))
""" format keyword"""
message = 'we have {mystudents} happy students in {mytrack} track'
print(message.format(mytrack=track, mystudents=no_of_studnets))
"""--- replace"""

message = 'I love python  ooooooooooooooo'
print(message.replace('o', '@', 3))


""" f-format string """

" formatting the string depends on existing variables in the script "
# name=  input("please enter name: ")
# track = input("please enter track: ")
# temp = f'Student with name {name} studies at {track} track'
# print(temp)


for char in 'noha':
    print(f"char = {char}")



""" ---> strip """

message = '       The lecture is very very interesting                        '
print(message, len(message))
print(message.strip())  # remove spaces from the beginning and the end of the string
print(message.lstrip())  # remove spaces from the beginning of the string
print(message.rstrip())

print(message.strip('T@ '))  # strip any of these chars from begining and end of the string


name = 'Hosam' + '    ' + str(10) + '10'
print(name)


" min , max for string "
print(min('Ahmed', 'Ali' , 'iti', 'abc'))
