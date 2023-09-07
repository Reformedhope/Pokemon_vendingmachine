from Pokemon import Pokemon
from Vending_Machine import Vending

class Vending:
    def __init__(self):
        self.human = None



    def user_funds_amount(self):
        user = int(input("Please enter the amount of money you wish you pay for a pokemon, Min is $1.00 "))
        if user == "1":
            print(f'You can select one of these pokemon{self.list_pokemon}')
            
    



    def run_vending(self):
        self.user_funds_amount()
    
    

