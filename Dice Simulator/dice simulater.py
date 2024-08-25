import random

# ● ┌ ─ ┐ │ └ ┘

dice_art={
     1: ("┌─────────┐",
         "│         │",
         "│    ●    │",
         "│         │",
         "└─────────┘"),

    2: ( "┌─────────┐",
         "│ ●       │",
         "│         │",
         "│       ● │",
         "└─────────┘"),

    3: ( "┌─────────┐",
         "│    ●    │",
         "│    ●    │",
         "│    ●    │",
         "└─────────┘"),

    4: ( "┌─────────┐",
         "│ ●     ● │",
         "│         │",
         "│ ●     ● │",
         "└─────────┘"),

    5: ( "┌─────────┐",
         "│ ●     ● │",
         "│    ●    │",
         "│ ●     ● │",
         "└─────────┘"),

    6: ( "┌─────────┐",
         "│  ●   ●  │",
         "│  ●   ●  │",
         "│  ●   ●  │",
         "└─────────┘")               

}

dice=[]
total=0
no_of_dies= int(input("How many rolls:"))

for die in range(no_of_dies):
    dice.append(random.randint(1,6))

print(dice)    

for die in range(no_of_dies):
    for line in dice_art.get(dice[die]):
        print(line)

for die in dice:
    total+=die

print(f"Total: {total}")    