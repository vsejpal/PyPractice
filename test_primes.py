from unittest import TestCase
from find_primes import Primes

__author__ = 'vsejpal@gmail.com'


class TestPrimes(TestCase):
    def test_find_primes_before(self):
        self.assertItemsEqual([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97], Primes().find_primes_before(100))
        self.assertItemsEqual([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97], Primes().find_primes_before(97))
        self.assertItemsEqual([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89], Primes().find_primes_before(96))