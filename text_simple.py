import unittest

import simple1

class TestSimple(unittest.TestCase):
    def test_one_word(self):
        text = 'python'
        result = simple1.cap_text(text)
        self.assertEqual(result,'Python')

    def test_multiple_words(self):
        text = 'monty python'
        result = simple1.cap_text(text)
        self.assertEqual(result,'Monty Python')

if __name__ == '__main__':
    unittest.main()