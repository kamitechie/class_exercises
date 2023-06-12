import unittest
from deck_main import Card, Deck


class TestDeckMain(unittest.TestCase):

    def test_show_card(self):
        self.test_param_card = Card('Hearts', 5)
        self.assertEqual(self.test_param_card.show_card(), 'Hearts5')


if __name__ == '__main__':
    unittest.main()
