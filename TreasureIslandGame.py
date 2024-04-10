print('''
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|                           
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.\n") 

choice1 = input("You are at a cross road. Where do you want to go? Type 'left' or 'right' \n").lower()

if choice1 =="left":
  choice2 = input("You came to the edge of the lake. There is a boat on the lake. Type 'boat' or 'walk' \n ").lower()
  if choice2=="boat":
    choice3 = input("You crossed the lake. After walking for a while, you across 3 different colored doors. Which one will you choose? Type 'red', 'blue' or 'yellow' \n").lower()
    if choice3 == "red":
      print("The bomb behind the door exploded. Game Over!")
    elif choice3== "blue":
      print("YOU WON THE GAME!")
    elif choice3== "yellow":
      print("The bomb behind the door exploded. Game Over!")
    else:
      print("GAME OVER!")
  else:
    print("You encountered a wild animal and it killed you. Game Over!")
else:
  print("You encountered a wild animal and it killed you. Game Over!")