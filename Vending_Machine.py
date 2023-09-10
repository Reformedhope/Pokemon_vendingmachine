from Pokemon import Pokemon, Charizard



class Vending:
    def __init__(self):
        self.human = None



    def user_funds_amount(self):
        user = int(input("Please enter the amount of money you wish you pay for a pokemon, Min is $1.00 "))
        if user == "1":
            charizard = Charizard()
            print(f'You can select one of these pokemon{charizard}')
            
    



    def run_vending(self):
        self.user_funds_amount()
    
    

