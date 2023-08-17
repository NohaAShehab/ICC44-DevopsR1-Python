

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
    fileobject = open('mycv.txt', 'w') # TextIOWrapper --->
    # when you open file with write mode --> if file doesn't exists --->
    # python will try to create it
    # if file exists --> open file for writing starting from the begining of the file
    # remove old content
except Exception as e:
    print(e)
else:
    print(fileobject)
    fileobject.write('Hello world\n')
    fileobject.write('-------------------------\n')
    data = ['Ahmed', 'Ali', 'Mohmed']
    fileobject.write('\n'.join(data))
    fileobject.seek(0)
    fileobject.writelines(data)  # iterables
    fileobject.close()







