from classes.game import Person, bcolors

magic = [{"name": "Fire", "cost": 10, "dmg": 60},
         {"name": "Thunder", "cost": 12, "dmg": 80},
         {"name": "Blizzard", "cost": 10, "dmg": 60}]

player = Person(460, 65, 60, 34, magic) # instantiate player
enemy = Person(1200, 65, 45, 25, magic) # instantiate (creating object from a blueprint(enemy 

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTAKCS!" + bcolors.ENDC)

while running:
    print("==============")
    player.choose_action()
    choice = input("Choose action:")

    print("You chose", choice)
    running = False