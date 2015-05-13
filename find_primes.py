__author__ = 'vsejpal'

class Primes:
    '''
        In theory this algorithm is O (n log log n), however I have a strong feeling it is O (n log n)
        because, we iterate the number list once (n) and for each item  'p' we start at its 'p-square' and mark off items in steps of 'p'
        thus with as we advance through the list, we cut are 'items to be marked off' nearly by half, just like binary search
    '''
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


