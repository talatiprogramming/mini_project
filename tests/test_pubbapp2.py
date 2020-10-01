import unittest
from unittest.mock import patch
from tablecopy import print_table
from bunchoffunctions import name_input, drink_input, round_maker
from ..v4.cuppa_classes import RoundMaker 

class test_name_input(unittest.TestCase):
    @patch("builtins.input")          
    def test_name_input(self, mock_input):
        # Arrange
        mock_input.return_value = "bob"
        
        # act
        actual = name_input()

        # Assert
        self.assertEqual("Bob", actual)

class TestRoundMaker(unittest.TestCase):
    @patch("bunchoffunctions.name_input")
    @patch("bunchoffunctions.drink_input")
    
    def test_round_maker(self, mock_drink_input, mock_name_input):
        # Arrange
        mock_name_input.return_value = "Larry"
        mock_drink_input.return_value = "coffee"

        expected = ["Larry ordered coffee"]

        # Act
        actual = round_maker()

        # Assert
        self.assertEqual(expected, actual) 


    def test_server_assign(self, mock_name_input):
        #Arrange
        mock_name_input.return_value = "Gary"
        mock_server = Mock(RoundMaker("Gary", None, None, []))
        expect = ["Gary"]

        # Act
        actual = RoundMaker("Gary", None, None, [])

        # Assert
        self.assertEqual(expect, actual)

if __name__ == '__main__':
    unittest.main() 