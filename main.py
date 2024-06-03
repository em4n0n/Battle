from classes.game import Person, bcolors
from classes.magic import Spell

# Create Black Magic
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 10, 100, "black")
blizzard = Spell("Blizzard", 10, 100, "black")
meteor = Spell("Meteor", 20, 200, "black")
quake = Spell("Quake", 14, 140, "black")

# Create White Magic
player = Person(460, 65, 60, 34)
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 18, 200)

# Instantiate People

player = Person(460, 65, 60, 34, [fire, thunder, blizzard, meteor, cure, cura]) # instantiate player
enemy = Person(1200, 65, 45, 25, [fire, thunder, blizzard, meteor, cure, cura]) # instantiate (creating object from a blueprint(enemy 

running = True # run the loop
i = 0

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

while running:
    print("======================")
    player.choose_action() # call the method
    choice = input("Choose action:")
    index = int(choice) - 1 # reduce the choice by 1 since index starts at 0
    
    if index == 0:
        dmg = player.generate_damage() # randrange of atkl + atkh
        enemy.take_damage(dmg) # take damage method
        print("You attacked for", dmg, "points of damage.")
    elif index == 1:
        player.choose_magic()
        magic_choice = int(input("Choose magic:")) - 1 # wrap input in int
        magic_dmg = player.generate_spell_damage(magic_choice)
        spell = player.get_spell_name(magic_choice)
        cost = player.get_spell_mp_cost(magic_choice) # reduce magic points by the cost of the spell
    
        current_mp = player.get_mp() # get mp

        if cost > current_mp:
            print(bcolors.FAIL + "\nNot enough MP\n" + bcolors.ENDC)
            continue

        player.reduce_mp(cost) # reduce mp by cost
        enemy.take_damage(magic_dmg) # enemy takes magic damage
        print(bcolors.OKBLUE + "\n" + spell + " deals", str(magic_dmg), "points of damage" + bcolors.ENDC)

    enemy_choice = 1 # only attack

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacks for", enemy_dmg)

    print("==========================")
    print("Enemy HP:", bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + bcolors.ENDC + "\n")

    print("Your HP:", bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + bcolors.ENDC)
    print("Your MP:", bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_max_mp()) + bcolors.ENDC + "\n")

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "You Win!" + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + "Your enemy has defeated you!" + bcolors.ENDC)
        running = False