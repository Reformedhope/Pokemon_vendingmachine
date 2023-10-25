from Pokemon import Pokemon, Charizard, Blastoise, Ninetails, Squirtle

class Vending():
    def __init__(self):
        self.human = None

    def user_funds_amount(self):
        user = input("Please enter the amount of money you wish you pay for a pokemon, Min is 1 max is 2 ")
        if user == "1":
            charizard = Charizard()
            blatoise = Blastoise()
            print(f"You may pick from the following pokemon {charizard.name} {blatoise.name}")
        elif user == "2":
            ninetails = Ninetails()
            squirtle = Squirtle()
            print(f"You may pick from the following {ninetails.name} {squirtle.name}")
        else:
            print("Incorrect value")