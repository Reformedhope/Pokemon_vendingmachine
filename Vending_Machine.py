from Pokemon import Pokemon

class Vending:
    def __init__(self):
        self.human = None



    def user_funds_amount(self):
        user_coins = int(input("Please enter the amount of money you wish you pay for a pokemon, Min is 1.00 "))
        if user_coins == "1":
            print(f"You can select one of these pokemon{self.list_pokemon}")
            
    



    def run_vending(self):
        self.user_funds_amount()
    
    

