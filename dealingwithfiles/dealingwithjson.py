

## read data from json
import json
try:
    with open('users.json', 'r') as fileobj:
        print(fileobj)
        data = fileobj.read()
        # print(data)
        dataa = json.loads(data)
        print(dataa)
except Exception as e:
    print(e)




# write data in json

# myinfo ={"id":3,"name":"noha"}
# try:
#     with open('users.json', 'a') as fileobj:
#         print(fileobj)
#         # convert dictionary to string
#         myinfo = json.dumps(myinfo)
#         # print(myinfo)
#         fileobj.write(myinfo)
# except Exception as e:
#     print(e)




def read_data():
    try:
        with open('users.json', 'r') as fileobj:
            print(fileobj)
            data = fileobj.read()
            # print(data)
            dataa = json.loads(data)
            return dataa  # list of dict
    except Exception as e:
        print(e)


myinfo ={"id":3,"name":"noha"}
try:
    old_data = read_data()  # list of dicts
    with open('users.json', 'w') as fileobj:
        old_data.append(myinfo)
        # data = json.dumps(["ffff", 'ffff'])
        data = json.dumps(old_data, indent=4)  # convert list of dicts to string
        fileobj.write(data)  # write data to the file ?
except Exception as e:
    print(e)