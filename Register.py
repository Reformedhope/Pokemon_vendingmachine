from Coin import Coin
from Penny import Penny
from Quarter import Quarter
from Nickel import Nickel

# Register.drawer is a container (dictionary) of smaller containers (lists) of coins
# When creating a Register object (instantiate) we add 5 new Penny objects to the 'pennies' container

class Register (): 
  def __init__(self):
    self.drawer = {
      'pennies': [],
      'nickels': [],
      'dimes': [],
      'quarters': [],
    }

    while len(self.drawer['pennies']) < 5:
      new_penny = Penny()
      self.drawer['pennies'].append(new_penny)
              
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