print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to the Treasure Island!\n")
print("Your mission is finding the treasure.\n")
first_choice = input(
    "You´re at a cross road. Where do you want to go? Type \"left\" or \"right\".\n"
)
if first_choice.lower() == "left":
  second_choice = input(
      "You arrived in a lake, there's an island in the middle of it. Type: \"wait\" to wait for a boat or \"swim\" to swim until there.\n"
  )
  if second_choice.lower() == "wait":
    third_choice = input(
        "You arrived the island safe, there's a house with 3 doors, one red, one yellow and one blue. What color do you choose?\n"
    )
    if third_choice.lower() == "red":
      print("You came in a room full of fire. GAME OVER!")
    elif third_choice.lower() == "yellow":
      print("You found the treasure! YOU WIN!")
    elif third_choice.lower() == "blue":
      print("You came in a room full of starving monsters. GAME OVER!")
    else:
      print("You chose an nonexistent door. GAME OVER!")
  else:
    print("You were attacked for an angry trout. GAME OVER!")
else:
  print("You felt in a hole, GAME OVER!")
