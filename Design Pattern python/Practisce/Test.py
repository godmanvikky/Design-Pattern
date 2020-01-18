import unittest
from Employee import Employee
class Test(unittest.TestCase):
    def name(self):
         e=Employee('Vikky',23)
         self.assertEqual(e.getName('Vikky'), 'Vikky')
if __name__ == "__main__":
    unittest.main()