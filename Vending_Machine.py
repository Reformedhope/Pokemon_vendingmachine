from Pokemon import Pokemon, Charizard



class Vending():
    def __init__(self):
        self.human = None



    def user_funds_amount(self):
        user = input("Please enter the amount of money you wish you pay for a pokemon, Min is $1.00 ")
        if user == "1":
            charizard = Charizard()
            print(f'You may pick from the following pokemon{charizard}')
            
    



    def run_vending(self):
        self.user_funds_amount()
    
    

