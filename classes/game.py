from classes.game import Person, bcolors

magic = [{"name": "Fire", "cost": 10, "dmg": 60}, # list of dictionaries
         {"name": "Thunder", "cost": 10, "dmg": 60},
         {"name": "fire", "cost": 10, "dmg": 60}] 

player = Person(460, 65, 60, 34, magic) # player stats

print(player.generate_damage(0)) # random damage
print(player.generate_damage(0))
print(player.generate_damage(0))