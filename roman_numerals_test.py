import unittest

from roman_numerals import RomanNumerals


class EncodeTestCase(unittest.TestCase):

    def setUp(self):
        self.roman_numerals = RomanNumerals()

    def test_0_returns_empty_string(self):
        self.assertEqual('', self.roman_numerals.encode(0))

    def test_1_through_3(self):
        self.assertEqual('I', self.roman_numerals.encode(1))
        self.assertEqual('II', self.roman_numerals.encode(2))
        self.assertEqual('III', self.roman_numerals.encode(3))

    def test_4_returns_IV(self):
        self.assertEqual('IV', self.roman_numerals.encode(4))

    def test_5_returns_V(self):
        self.assertEqual('V', self.roman_numerals.encode(5))

    def test_6_through_8(self):
        self.assertEqual('VI', self.roman_numerals.encode(6))
        self.assertEqual('VII', self.roman_numerals.encode(7))
        self.assertEqual('VIII', self.roman_numerals.encode(8))

    def test_9_returns_IX(self):
        self.assertEqual('IX', self.roman_numerals.encode(9))

    def test_10_returns_X(self):
        self.assertEqual('X', self.roman_numerals.encode(10))

    def test_11_through_13(self):
        self.assertEqual('XI', self.roman_numerals.encode(11))
        self.assertEqual('XII', self.roman_numerals.encode(12))
        self.assertEqual('XIII', self.roman_numerals.encode(13))
    #
    # def test_14_returns_XIV(self):
    #     self.assertEqual('XIV', self.roman_numerals.encode(14))
