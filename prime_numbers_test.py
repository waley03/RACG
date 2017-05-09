import unittest
from prime_numbers import prime_numbers
class Test_Prime_Numbers(unittest.TestCase):

    def test_prime_numbers(self):
        """Testing if prime numbers are correctly generated."""
        
        self.assertEqual(prime_numbers(20), [2, 3, 5, 7, 11, 13, 17, 19])
    def test_zero(self):
        """Testing if zero is correctly determined not to be prime."""

        self.assertEqual(prime_numbers(0), "Zero or One cannot be prime numbers.")
    def test_one(self):
        """"Testing if one is correctly determined not to be prime."""

        self.assertEqual(prime_numbers(1), "Zero or One cannot be prime numbers.")
    def test_invalid_type_string(self):
        """Testing if error returned if input not integer."""

        self.assertEqual(prime_numbers("String"), "Only integers are allowed.")
    def test_only_positive(self):
        """Testing if error returned if negative integers input."""

        self.assertEqual(prime_numbers(-1), "Not possible to generate prime numbers for integers less than 2.")
