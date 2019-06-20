import unittest

from roman_numerals import RomanNumerals


class EncodeTestCase(unittest.TestCase):

    def setUp(self):
        self.roman_numerals = RomanNumerals()

    def test_zero_returns_empty_string(self):
        self.assertEqual('', self.roman_numerals.encode(0))

    def test_1_returns_I(self):
        self.assertEqual('I', self.roman_numerals.encode(1))

    def test_2_returns_II(self):
        self.assertEqual('II', self.roman_numerals.encode(2))

    def test_3_returns_III(self):
        self.assertEqual('III', self.roman_numerals.encode(3))

    def test_4_returns_IV(self):
        self.assertEqual('IV', self.roman_numerals.encode(4))

    def test_5_returns_V(self):
        self.assertEqual('V', self.roman_numerals.encode(5))

    def test_6_returns_VI(self):
        self.assertEqual('VI', self.roman_numerals.encode(6))

    def test_7_returns_VII(self):
        self.assertEqual('VII', self.roman_numerals.encode(7))
