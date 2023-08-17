

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
    fileobject = open('names.txt', 'r') # TextIOWrapper --->
except Exception as e:
    print(e)
else:
    print(fileobject)
    # read function --> read file content from the beginning of the file
    #
    data = fileobject.read()  # in one string
    print(data)
    fileobject.seek(0)
    # lines  =fileobject.readlines()
    lines = fileobject.read()
    print(lines)
    fileobject.close()







