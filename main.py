import random

def Solution():
    Doors = [1, 2, 3]
    Stay = 0
    Switch = 0
    for i in range(1000):
        door = random.choice(Doors)
        player = random.choice(Doors)
        if player == door:
            Stay += 1
        else:
            Switch += 1
    print("Stay: count {} = {}% | Switch : count {} = {}%".format(Stay, Stay/10, Switch, Switch/10))

Solution()
