


text = []

def read():
    global text
    file = open('test1.txt', 'r')
    while True:
        line = file.readline()

        text.append(line)




        if not line:
            break


    print(text)
    file.close()


read()




def write():
    global text
    file = open('./test1.txt', 'a')

    file.write('wow, so cool!')
    file.write('\n')
    file.write('wow, so cool!')

    file.close()



write()
read()

