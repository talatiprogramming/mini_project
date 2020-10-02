import unittest

def user_input():
    # Input() asks user to print something to the terminal
    # which is then returned as a string
    return input()
    

class SumanTest(unittest.TestCase):
    def test_user_input(self):
        # Arrange
        # This is what I expect to come out of input() when I type
        # 'banana' into the terminal
        expected_input = "banana"

        #Act
        # This is what actually happens when I call user_input()
        actual = user_input()

        #Assert
        assert expected_input == actual
    

if __name__ == '__main__':
    unittest.main() 