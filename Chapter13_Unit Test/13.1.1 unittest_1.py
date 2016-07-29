import unittest
class TestAddition(unittest.TestCase):
    def setUp(self):
        print("Setting up the test")

    def tearDown(self):
        print("Tearing down the test")

    def test_twoPlusTwo(self):
        total = 2+2
        self.assertEqual(4,total)

    def test_onePlusTwo(self):
        total = 1+2
        self.assertEqual(3,total)

if __name__ == '__main__':
    unittest.main()

# Output
# Testing started at 下午5:34 ...
# Setting up the test
# Tearing down the test
# Setting up the test
# Tearing down the test