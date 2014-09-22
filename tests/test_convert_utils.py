import sys
import os
import unittest

import convert_utils

# Using data from http://romannumerals.babuo.com/roman-numerals-1-5000 for testing
filename = '%s/assets/1_to_3999.txt' % os.path.dirname(os.path.abspath(__file__))


class TestArabicToRoman(unittest.TestCase):
    def test_correct_conversion(self):
        with open(filename, 'r') as f:
            for line in f:
                arabic, roman = line.split(':')
                self.assertEqual(convert_utils.arabic_to_roman(int(arabic)), roman.strip())
                sys.stdout.write('%s is the %s\n' % (arabic, roman.strip()))


class TestRomanToArabic(unittest.TestCase):
    def test_correct_conversion(self):
        with open(filename, 'r') as f:
            for line in f:
                arabic, roman = line.split(':')
                self.assertEqual(convert_utils.roman_to_arabic(roman.strip()), int(arabic))
                sys.stdout.write('%s is the %s\n' % (roman.strip(), arabic))

if __name__ == '__main__':
    unittest.main()
