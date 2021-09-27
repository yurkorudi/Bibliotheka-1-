import json


list_of_file = []

def read():
    global list_of_file
    file = open('son_file.txt')
    data = json.load(file)
    
    for obj in data:
        list_of_file.append(obj)


    print(list_of_file)

def save(list):
    with open('son_file.txt', 'w') as opened:
        str_to_write = json.dumps(list, indent=4, sort_keys=True)
        opened.write(str_to_write)


read()
list_of_file.append({"kaka" : "lolol"})
save(list_of_file)








