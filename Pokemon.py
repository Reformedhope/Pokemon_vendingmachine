

class Pokemon:
    def __init__(self,name):
        self.name = name
        self.cost = "1"

class Lowpokemon:
    def __init__(self,name):
        self.name = name
        self.cost = "2"







class Charizard(Pokemon):
    def __init__(self):
        super().__init__("charizard")


class Blastoise(Pokemon):
    def __init__(self):
        super().__init__("Blastoise")

        



class Squirtle (Lowpokemon):
    def __init__(self):
        super().__init__("squirtle")



class Ninetails(Lowpokemon):
    def __init__(self):
        super().__init__("Ninetails")



    
        

    

