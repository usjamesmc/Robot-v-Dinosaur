from weaponone import Weaponone
from weapontwo import Weapontwo
from weaponthree import Weaponthree
class Robot:
    def __init__(self, name):
        self.health = 100
        self.name = name
        self.weapon_one = Weaponone('Tank', 20)
        self.weapon_two = Weapontwo('Napalm', 50)
        self.weapon_three = Weaponthree('Cannon', 10)
    def attack(self, dinosaur):
        weapon_options = '[Tank, Napalm, Cannon]'
        user_input = input(f'Choose a weapon from {weapon_options}')
        if dinosaur.health > 0 and self.health > 0:
            if user_input == 'Tank':
                dinosaur.health -= self.weapon_one.attack_power
                print(f'Robot has attacked Dinosaur on the Battlefield dealing {self.weapon_one.attack_power} damage. Dinosaur is down to {dinosaur.health} health.')
            
            if user_input == 'Napalm':
                dinosaur.health -= self.weapon_two.attack_power
                print(f'Robot has attacked Dinosaur on the Battlefield dealing {self.weapon_two.attack_power} damage. Dinosaur is down to {dinosaur.health} health.')
            
        
            if user_input == 'Cannon':
                dinosaur.health -= self.weapon_three.attack_power
                print(f'Robot has attacked Dinosaur on the Battlefield dealing {self.weapon_three.attack_power} damage. Dinosaur is down to {dinosaur.health} health.')
        