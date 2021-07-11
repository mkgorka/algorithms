import math
import time

def count_Kprimes(k, start, nd):
    start_time = time.time()

    num_lst = [i for i in range(2, nd + 1)]
    element_lst = []
    k_primes = []
    factors = []

    for n in num_lst:
        n = 2
        while n < math.sqrt(nd):
            for nr in range(n, nd + 1):
                if n * nr in num_lst:
                    num_lst.remove(n * nr)
            n += 1

    for element in range(start, nd + 1):
        if element not in num_lst:
            element_lst.append(element)
    element_lst.remove(0)
    element_lst.remove(1)

    for elem in element_lst:
        initial_elem = elem
        for p in num_lst:
            while elem % p == 0:
                factors.append(p)

                elem = elem // p
        k_counter = len(factors)
        factors.clear()
        if k_counter <= k:
            k_primes.append(initial_elem)

    return k_primes
  
