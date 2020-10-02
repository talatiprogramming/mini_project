import unittest
import unittest.mock
from unittest.mock import patch
from tests.tablecopy import print_table
from tests.bunchoffunctions import name_input, drink_input, round_maker
from tests.classescopy import RoundMaker 

class test_name_input(unittest.TestCase):
    @patch("builtins.input")          
    def test_name_input(self, mock_input):
        # Arrange
        mock_input.return_value = "i really love peanuts"
        expected = "I Really Love Peanuts"
        # act
        actual = name_input()

        # Assert
        self.assertEqual(expected, actual)

class TestRoundMaker(unittest.TestCase):
    @patch("tests.bunchoffunctions.name_input")
    @patch("tests.bunchoffunctions.drink_input")
    
    def test_round_maker(self, mock_drink_input, mock_name_input):
        # Arrange
        mock_name_input.return_value = "Larry"
        mock_drink_input.return_value = "coffee"

        expected = ["Larry ordered coffee"]

        # Act
        actual = round_maker()

        # Assert
        self.assertEqual(expected, actual) 

    # @patch("tests.bunchoffunctions.name_input")
    # def test_server_assign(self, mock_name_input):
    #     #Arrange
    #     mock_name_input.return_value = "Gary"
    #     mock_server = Mock(RoundMaker())
    #     expect = ["Gary"]

    #     # Act
    #     actual = RoundMaker("Gary", None, None, [])

    #     # Assert
    #     self.assertEqual(expect, actual)

if __name__ == '__main__':
    unittest.main() 