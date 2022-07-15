import random

def chooser(path, thing):
    f = open(path, 'r')
    list = f.readlines()
    
    if len(list) == 0:
        print("Empty list, add something to watch :P")
        return

    num = random.randrange(0, len(list))

    chosen = list[num]

    print(f'The chosen {thing} was {chosen}')

def add(path):
    f = open(path, 'a')
    name = input('Name to add: ')
    f.write(f'{name}\n')
    #add on file

    ans = input('Keep adding? y/n\n')
    if ans.lower() == 'y':
        add(path)