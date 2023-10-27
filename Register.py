from Coin import Coin
from Penny import Penny
from Quarter import Quarter
from Nickel import Nickel
from Dime import Dime
# Register.drawer is a container (dictionary) of smaller containers (lists) of coins
# When creating a Register object (instantiate) we add 5 new Penny objects to the 'pennies' container


class Register (): 
  # On Register Create
  def __init__(self):
    # Create a container to hold all of our coins
    self.drawer = {
      # penny bucket
      'pennies': [],
      # nickel bucket
      'nickels': [],
      # ...
      'dimes': [],
      # ...
      'quarters': [],
    }

    # When creating the register, we want 5 pennies in our register/drawer
    while len(self.drawer['pennies']) < 20:
      # create a new penny
      new_penny = Penny()
      # add the penny to the drawer (in the penny bucket)
      self.drawer['pennies'].append(new_penny)
      
    # I want 20 pennies, 30 nickels, 40 dimes, and 50 quarters in my drawer
    while len(self.drawer['nickels']) < 30:
      new_nickel = Nickel()
      self.drawer['nickels'].append(new_nickel)

    while len(self.drawer['dimes']) < 40:
      new_dime = Dime()
      self.drawer['dimes'].append(new_dime)
    

    while len(self.drawer['quarters']) < 50:
      new_quarter = Quarter()
      self.drawer['quarter'].append(new_quarter)



      









    # {
    #     'pennies': [
    #       <Penny.Penny object at 0x0000023514B5E250>,
    #       <Penny.Penny object at 0x0000023514B5E350>,
    #       <Penny.Penny object at 0x0000023514B5E310>,
    #       <Penny.Penny object at 0x0000023514B5E290>,
    #       <Penny.Penny object at 0x0000023514B729990>
    #     ],
    #     'nickels': [],
    #     'dimes': [],
    #     'quarters': []
    # }