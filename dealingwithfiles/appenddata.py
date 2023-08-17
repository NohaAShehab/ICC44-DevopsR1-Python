

""" file ... read data from file
    write data to the file
"""

""" dealing with resource 
    open ---> open file 
        for what  ---> decide mode of openning?
            read content  'r'
            write content 'w'  --> open file for writing starting from the beginning of the file
            -              'a' --> open file for writing starting from the end of the file
         
    do operation  --> read / write
        READ:
            read()
            readlines()
        WRITE:
            write
            writelines
    close ---> close file
            CLOSE
"""


### OPEN FILE  for reading


try:
    fileobject = open('dataa.txt', 'a') # TextIOWrapper --->
    # when you open file with append mode --> if file doesn't exists --->
    # python will try to create it
    # if file exists --> open file for writing starting from the end of the file
    # remove old content
except Exception as e:
    print(e)
else:
    print(fileobject)
    fileobject.write('Hii')
    fileobject.seek(0)
    fileobject.write("bye\n")
    fileobject.writelines(['rrr\n', 'test\n'])
    fileobject.close()


############
try:
    with open('mycv.txt','r') as myfile:
        data = myfile.read()
        print(data)
except Exception as e:
    print(e)




