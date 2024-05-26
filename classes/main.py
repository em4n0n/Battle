from classes.game import Person, bcolors

magic = [{"name": "Fire", "cost": 10, "dmg": 60},
         {"name": "Thunder", "cost": 10, "dmg": 60},
         {"name": "fire", "cost": 10, "dmg": 60}]

player = Person(460, 65, 60, 34, magic)

print(player.generate_damage(0))
print(player.generate_damage(0))
print(player.generate_damage(0))