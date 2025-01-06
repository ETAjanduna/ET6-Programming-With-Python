import unittest

from ..sum_of_two_integers import sum_of_two_integers

class TestSumOfTwoIntegers(unittest.TestCase):
    """ """

    def test_minimal_input(self):
        """"""
        self.assertEqual(sum_of_two_integers(0, 0), 0)
