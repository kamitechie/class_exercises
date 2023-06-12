import unittest
from datetime import date
from main import Dog


class TestMain(unittest.TestCase):

    def setUp(self):
        self.dog_1 = Dog('Saturn', 'medium', 'Alaskan husky', date(2007, 8, 26))
        self.dog_2 = Dog('Haggel', 'big', 'Alaskan husky', date(2014, 4, 12))

    def test_bark(self):
        self.assertEqual(self.dog_1.bark(), 'woof!')
        self.assertEqual(self.dog_2.bark(), 'woof!')

    def test_get_name(self):
        self.assertEqual(self.dog_1.get_name(), 'Saturn')
        self.assertEqual(self.dog_2.get_name(), 'Haggel')

    def test_set_name(self):
        test_param_name = 'Stein'
        self.assertEqual(self.dog_1.set_name(test_param_name), 'Stein')
        self.assertEqual(self.dog_2.set_name(test_param_name), 'Stein')

    def test_dog_years(self):
        self.assertEqual(self.dog_1.dog_years(), 112)
        self.assertEqual(self.dog_2.dog_years(), 63)

    def test_formatted_birth_date(self):
        self.assertEqual(self.dog_1.formatted_birth_date(), '26/08/2007')
        self.assertEqual(self.dog_2.formatted_birth_date(), '12/04/2014')


if __name__ == '__main__':
    unittest.main()
