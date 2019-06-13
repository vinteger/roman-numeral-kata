import unittest

from roman_numerals import RomanNumerals


class EncodeTestCase(unittest.TestCase):

    def setUp(self):
        self.roman_numerals = RomanNumerals()

    def test_zero_returns_empty_string(self):
        self.assertEqual(self.roman_numerals.encode(0), '')

    def test_1_returns_I(self):
        self.assertEqual(self.roman_numerals.encode(1), 'I')

    def test_2_returns_II(self):
        self.assertEqual(self.roman_numerals.encode(2), 'II')

    def test_3_returns_III(self):
        self.assertEqual(self.roman_numerals.encode(3), 'III')
