lista = list()

for item in range(0, 10):
    print('primeiro for')
    for subitem in range(0, 10):
        list.append(subitem)
        print('segundo for')
    for subitem in lista:
        print(subitem)
        print('terceiro for')
        if subitem == 5:
            break
    break