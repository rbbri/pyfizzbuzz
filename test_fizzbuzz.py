import unittest
import random
from fizzbuzz import Fizzbuzz


class FizzbuzzTDD(unittest.TestCase):

    def test_fizzbuzz_returns_fizz_for_multiples_of_three(self):
        rand = random.randint(1, 100)
        result = Fizzbuzz().play(3 * rand)
        self.assertEqual(result, 'Fizz')

    def test_fizzbuzz_returns_buzz_for_multiples_of_five(self):
        rand = random.randint(1, 100)
        result = Fizzbuzz().play(5 * rand)
        self.assertEqual(result, 'Buzz')

    def test_fizzbuzz_returns_fizzbuzz_for_multiples_of_fifteen(self):
        rand = random.randint(1, 100)
        result = Fizzbuzz().play(15 * rand)
        self.assertEqual(result, 'FizzBuzz')

    def test_fizzbuzz_returns_the_number_otherwise(self):
        result = Fizzbuzz().play(2)
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()
