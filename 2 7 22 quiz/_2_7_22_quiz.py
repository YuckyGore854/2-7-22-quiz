import random

def programOne():
    print("First Program:")
    firstNum = 3
    while firstNum <= 21:
        print(firstNum)
        firstNum+=3

def programTwo():
    print("Second Program:")
    printTimes = int(input("User input: "))
    currTimes = 0
    while currTimes < printTimes:
        print("SNURFLE")
        currTimes+=1

def MonsterGen(biome):
    randNum = random.randint(0,99)
    if biome == 'd':
        if randNum < 20:
            print("Husk")
        elif randNum < 50:
            print("Spider")
        elif randNum < 100:
            print("Skeleton")
        else:
            print("Something went wrong")
    if biome == 'f':
        if randNum < 30:
            print("Zombie")
        elif randNum < 60:
            print("Skeleton")
        elif randNum < 70:
            print("Witch")
        elif randNum < 100:
            print("Nothing spawned")
        else:
            print("Something went wrong")

def programThree():
    print("Third Program:")
    print("###########FIELD MONSTERS ####################################")
    for i in range(20):
        MonsterGen('f')
    print("###########DESERT MONSTERS ###################################")
    for i in range(20):
        MonsterGen('d')

programOne()
programTwo()
programThree()
