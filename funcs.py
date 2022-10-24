import random

def chooser(path, thing):
    f = open(path, 'r')
    list = f.readlines()
    
    if len(list) == 0:
        print("Empty list, add something to watch :P")
        return

    num = random.randrange(0, len(list))

    chosen = list[num]

    #Delete chosen line from the file
    f = open(path, 'w')
    for i in range(len(list)):
        if (i != num):
            f.write(list[i])

    print(f'The chosen {thing} was {chosen}')

    return chosen

def add(path, name=None):
    f = open(path, 'a')

    if name == None:
        name = input('Name to add: ')
    if name != '':
        f.write(f'{name}\n')
