class Dinosaur:
    def __init__(self, name, attack_power):
        self.health = 100
        self.name = name
        self.attack_power = attack_power
    def attack(self, robot):   
        if robot.health > 0 and self.health > 0:
            robot.health -= self.attack_power
            print(f'Dinosaur has attacked Robot on the Battlefield dealing {self.attack_power} damage. Robot is down to {robot.health} health.')
            
       