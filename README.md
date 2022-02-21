# Challenge

### Code Explanation and Instructions to compile

```python
import random
```

1) import random = Importing the Random module inorder to get random choices.
2) Doors = [1, 2, 3] = Declaring the Doors variable and passing a list of doors.
3) Stay = 0 = Declaring the Stay variable, assigning 0 as the value to it and it functions as a counter for the number of times the player Stays with the same door.
4) Switch = 0 = Declaring the Switch variable, assigning 0 as the value to it and it functions as a counter for the number of times the player Switches to the other door.
5) for i in range(1000): = Declaring a For loop that will run for 1000 times.
6) door = random.choice(Doors) = Choosing a Random door and assigning to a variable named as door which is the correct order.
7) player = random.choice(Doors) = Choosing a Random door and assigning to a variable named as player which is the order that is chosed by the player.
8) if player == door: Stay += 1  = Defining an if statement that checks if the player chosed the correct door as the door variable's value, if the statement is True then will add +1 to the Stay Variable.
9) else: Switch +=1  = if the statement is False then will add +1 to the Switch Variable.
10) print("Stay: count {} = {}% | Switch : count {} = {}%".format(Stay, Stay/10, Switch, Switch/10))  = Print statement to prints the number of times the player stays with the same door and the percentage of times the player stays with the same door.
### Dependencies Used
 
1) Random
