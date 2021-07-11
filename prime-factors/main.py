def prime_factors(n):
    result = ""
    res_arr = []
    factors = []
    multi_list = []
    prime_el = 2
    primes = [prime_el]

    while prime_el < n:
        prime_el += 1
        for p in primes:
            if p * p > prime_el:
                primes.append(prime_el)
                break
            if prime_el % p == 0:
                break  
    if n > 1:
        for i in primes:
            while n%i == 0:
                n = n/i
                factors.append(i)

    for val in factors:
        if factors.count(val) == 1:
            result = "(%i)" % val
            if result not in res_arr:
                res_arr.append(result)

        elif factors.count(val) > 1:
            count = factors.count(val)
            result = "(%i**%i)" % (val, count)
            if result not in res_arr:
                res_arr.append(result)

    return "".join(res_arr)
