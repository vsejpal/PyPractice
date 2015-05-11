__author__ = 'vsejpal'

class Primes:
    def find_primes_before(self, num):
        bool_list = [True] * (num+1)
        primes = []

        # Mark both 0 and 1 as not prime
        bool_list[0] = bool_list [1] = False

        # 2 is the smallest possible prime number
        prime = 2
        while (prime <= num):
            if (bool_list[prime]):
                primes.append(prime)
                multiple = prime * prime
                while (multiple <= num):
                    bool_list[multiple] = False
                    multiple += prime
            prime += 1
        return primes

print Primes().find_primes_before(100)
