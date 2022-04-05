from weapon import Weapon
class Robot:
    def __init__(self, name):
        self.health = 100
        self.name = name
        self.active_weapon = Weapon('Flamethrower', 20)
    def attack(self, dinosaur):
        if dinosaur.health > 0:
            dinosaur.health -= self.active_weapon.attack_power
            print(f'Robot has attacked Dinosaur on the Battlefield dealing {self.active_weapon.attack_power} damage. Dinosaur is down to {dinosaur.health} health.')
            
        

        