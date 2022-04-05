from dinosaur import Dinosaur
from robot import Robot
class Battlefield:
    def __init__(self):  
        self.robot = Robot('Mayhem')
        self.dinosaur = Dinosaur('Destruction', 25)
    

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()

    def display_welcome(self):
        display_message = 'Welcome to the Ultimate Battlefield of Robots and Dinosaurs' 
        print(display_message)       

    def battle_phase(self):
        self.robot.attack(self.dinosaur)
        self.dinosaur.attack(self.robot)     

    def display_winner(self):
        pass    