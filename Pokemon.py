

class Pokemon:
    def __init__(self,name):
        self.name = name
        self.cost = "1"
        self.list_pokemon = ['Charizard', 'squirtle', 'Pikachu']
        self.selected_pokemon = " "
        

    def selected_pokemon(self):
        user_input= int(input(" please select a pokemon"))
        self.picked_pokemon = self.list_pokemon[user_input]
        



