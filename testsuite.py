#**Team Name**: The Amazing Horse Race
#**Team Members**: Linh Pham and Anna Christen
""" This Python script is for you to test your code before submitting it. 

Usage: click "Shell" next to "Console", then type "python3 tests.py" as shown below:
~/Final-Project$ python3 testsuite.py
"""
import unittest
from main import *

class SimpleTest(unittest.TestCase):
  
  def testdatastructure(self):
    """This test makes sure that the function horseracelist() produces the correct set of horses if the player is on race number 2."""
    list=[['7', 'SeaBiscuit', 'Speed', '100', 'Strength', '70', 'Stamina', '70'], ['8', 'Kelso', 'Speed', '65', 'Strength', '99', 'Stamina', '70'], ['9', 'Count Fleet', 'Speed', '70', 'Strength', '80', 'Stamina', '75'], ['10', 'Black Caviar', 'Speed', '75', 'Strength', '50', 'Stamina', '90'], ['11', 'Eclipse', 'Speed', '90', 'Strength', '60', 'Stamina', '50'], ['12', 'American Pharoah', 'Speed', '80', 'Strength', '80', 'Stamina', '80'], ['13', 'Phar Lap', 'Speed', '55', 'Strength', '89', 'Stamina', '90'], ['14', 'Holy Bull', 'Speed', '30', 'Strength', '105', 'Stamina', '70'], ['15', 'Winx', 'Speed', '85', 'Strength', '75', 'Stamina', '80'], ['16', 'War Admiral', 'Speed', '99', 'Strength', '70', 'Stamina', '65'], ['17', 'Ruffian', 'Speed', '88', 'Strength', '78', 'Stamina', '66'], ['18', 'Zenyatta', 'Speed', '75', 'Strength', '88', 'Stamina', '50']]
    self.assertEqual(horseracelist(2),list)

  def testwhowins(self):
    """This test makes sure WhoWins() returns the winner."""
    list = [100,110]
    self.assertEqual(WhoWins(list),'not you')
    
  def testsetuphorseobjects(self):
    """This test makes sure that the function that sets up the horse options for each race is returning a list of objects."""
    self.assertEqual(type(setuphorseobjects(3)), list)












    



if __name__ == '__main__':  
  unittest.main()
