import unittest
import random
from fizzbuzz import Fizzbuzz


class FizzbuzzTDD(unittest.TestCase):

    def test_fizzbuzz_returns_fizz_for_multiples_of_three(self):
        result = Fizzbuzz().play(3)
        self.assertEqual(result, 'Fizz')
        result = Fizzbuzz().play(3 * 8)
        self.assertEqual(result, 'Fizz')

    def test_fizzbuzz_returns_buzz_for_multiples_of_five(self):
        result = Fizzbuzz().play(5)
        self.assertEqual(result, 'Buzz')
        result = Fizzbuzz().play(5 * 5)
        self.assertEqual(result, 'Buzz')

    def test_fizzbuzz_returns_fizzbuzz_for_multiples_of_fifteen(self):
        result = Fizzbuzz().play(15)
        self.assertEqual(result, 'FizzBuzz')
        result = Fizzbuzz().play(15 * 6)
        self.assertEqual(result, 'FizzBuzz')

    def test_fizzbuzz_returns_the_number_otherwise(self):
        result = Fizzbuzz().play(2)
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()
