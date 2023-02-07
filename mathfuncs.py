import math
import numpy as np


def SieveOfPrimes(num):
    '''Returns the list of all the prime numbers smaller or equal to integer num.'''
    prime = [True]*(num+1)
    d = 2
    while (d**2 <= num):
        if prime[d]:
            for i in range(d**2, num+1, d):
                prime[i] = False
        d += 1
    lst_of_primes = []
    for d in range(2, num+1):
        if prime[d]:
            lst_of_primes += [d]
    return lst_of_primes

        


def prime_check(num):
    '''Checks whether integer num is a prime number. Returns Boolean.'''
    if num == 1:
        return False
    L = math.floor(math.sqrt(num))
    R = range(2, max(2, L+1))
    for i in R:
        if num % i == 0:
            return False
    return True


def divisors(num):
    '''Returns list of integer divisors of the integer num.'''
    if num == 1:
        return [1]
    if prime_check(num):
        return [1, num]
    L = math.floor(math.sqrt(num))
    R = range(2, max(2, L+1))
    divs = [1, num]
    for i in R:
        if num % i == 0:
            divs += [i, num//i]
    divs = sorted(list(set(divs)))
    return divs


def divnum(num):
    '''Returns the number of the integer divisors of the integer num.'''
    return len(divisors(num))


def prime_divisors(num):
    '''Returns the list of prime divisors of the integer num.'''
    if num == 1:
        return 1
    if prime_check(num):
        return [[num, 1]]
    L = math.floor(math.sqrt(num))
    R = range(2, max(2, L+1))
    divisors = []
    for i in R:
        if num % i == 0:
            if prime_check(i):
                divisors += [i]
        k = num//i
        if num % k == 0:
            if prime_check(k):
                divisors += [k]
    divisors = sorted(list(set(divisors)))
    divpows = []
    for j in range(len(divisors)):
        k = 0
        while num % (divisors[j]**k) == 0:
            k += 1
        divpows += [[divisors[j],k-1]]
    return divpows


def GCD2(num1, num2):
    '''Returns the greatest common divisor of two integers: num1 and num2.'''
    if num1 == num2:
        return num1
    a = min(num1, num2)
    b = max(num1, num2)
    if prime_check(b):
        return 1
    if b % a == 0:
        return a
    gcd = 1
    for i in range(1, a+1):
        if (a % i == 0) and (b % i == 0):
            gcd = i
    return gcd


def coprimes(num1, num2):
    '''Checks whether integers num1 and num2 are coprimes. Returns Boolean.'''
    return GCD2(num1, num2) == 1 and min(num1, num2) != 1


def LCM2(num1, num2):
    '''Returns the least common multiplyer of two integers: num1 and num2.'''
    return (num1*num2) // GCD2(num1, num2)


def GCD(num_lst):
    '''Returns the greatest common divisor of the integers in the list num_lst.'''
    if len(num_lst) == 1:
        return num_lst[0]
    elif len(num_lst) == 2:
        return GCD2(num_lst[0], num_lst[1])
    else:
        gcd = GCD2(num_lst[0], num_lst[1])
        for i in range(2, len(num_lst)):
            gcd = GCD2(gcd, num_lst[i])
    return gcd


def LCM(num_lst):
    '''Returns the least common multiplyer of the integers in the list num_lst.'''
    if len(num_lst) == 1:
        return num_lst[0]
    elif len(num_lst) == 2:
        return LCM2(num_lst[0], num_lst[1])
    else:
        lcm = LCM2(num_lst[0], num_lst[1])
        for i in range(2, len(num_lst)):
            lcm = LCM2(lcm, num_lst[i])
    return lcm


def perfect(num):
    '''Checks whether the integer num is a perfect number. Returns Boolean.'''
    if num == 1:
        return False
    divs = divisors(num)
    return sum(divs) == 2*num


def powerstring(num):
    '''Returns superscript string from the integer num.'''
    number = str(num)
    keys ='⁰¹²³⁴⁵⁶⁷⁸⁹'
    sup = ''
    for digit in number:
        sup += keys[int(digit)]
    return sup


def primpowstring(pdivs):
    '''Returns string representation of primal decomposition of the integer num.'''
    string = ''
    for div in pdivs:
        power = (powerstring(div[1]))*int(div[1] != 1) + '⋅'
        string += str(div[0]) + power
    string = string[:-1]
    return string


def factorialcheck(n):
    '''Checks if the integer n is a factorial. Returns Boolean.'''
    i = 1
    while n > 1:
        if n % i != 0:
            return False, -1
        else:
            n //= i
            i += 1
    return True, i-1



def numerical_analysis(num):
    '''Performs the numerical analysis of integer num and returns result as
    dictionary.'''
    primality = prime_check(num)
    if primality:
        divs = [1, num]
        primdivs = [[num, 1]]
        pdb, pdp = np.array([num]), np.array([1])
    elif num == 1:
        divs = [1]
        primdivs = [[1,1]]
        pdb, pdp = np.array([1]), np.array([1])
    else:
        divs = divisors(num)
        primdivs = prime_divisors(num)
        pdb, pdp = np.transpose(primdivs)
    smoothness = max(pdb)
    regularity = smoothness == 5
    unusual = smoothness > math.sqrt(num)
    roughness = min(pdb)
    sieve = SieveOfPrimes(smoothness)
    divcount = len(divs)
    sumdivs = sum(divs)
    abundance = sumdivs - 2*num
    primdivcount = len(primdivs)
    powsum = sum(pdp)
    minpow = min(pdp)
    maxpow = max(pdp)
    powgsd = GCD(pdp)
    powsimple = pdp//powgsd
    prfpwb = np.product(pdb**powsimple)
    undivs = []
    pronic_div  = 0
    pronic = False
    for div in divs:
        z = num//div
        if GCD2(div, z) == 1:
            undivs += [div]
        if z-div == 1:
            pronic = True
            pronic_div = div
    del undivs[-1]
    unitarysum = sum(undivs)
    perfect = abundance == 0
    abundant = abundance > 0
    semiprim = powsum == 2
    if num == 1:
        almstprm = 0
    else:
        almstprm = powsum
    sqrfr = maxpow == 1
    prfpw = powgsd > 1
    powerful = minpow > 1
    achilles = powerful and not prfpw
    primorial = (sieve == list(pdb)) and sqrfr
    refactorable = num % divcount == 0
    arithmetic = sumdivs % divcount == 0
    factorial, factorial_base = factorialcheck(num)
    analysis = {}
    analysis['eveness'] = num % 2 == 0
    analysis['primality'] = primality
    analysis['prime_factorization'] = primpowstring(primdivs)
    analysis['prime_divisors'] = list(pdb)
    analysis['prime_divisors_powers'] = list(pdp)
    analysis['number_of_prime_divisors'] = primdivcount
    analysis['divisors'] = str(divs)[1:-1]
    analysis['sumdivs'] = sumdivs
    analysis['numofdivs'] = divcount
    analysis['unipropdivs'] = str(undivs)[1:-1]
    analysis['unidivsum'] = unitarysum
    analysis['unitary_perfect'] = unitarysum == num
    analysis['abundance'] = abundance
    analysis['abundancy_index'] = sumdivs/num
    analysis['perfect'] = perfect
    analysis['semiprime'] = semiprim
    analysis['sqrfree'] = sqrfr
    analysis['powerful'] = powerful
    analysis['perfectpower'] = prfpw
    analysis['baseofperfectpower'] = prfpwb
    analysis['powerofperfectpower'] = powgsd
    analysis['achilles'] = achilles
    analysis['pronic'] = pronic
    analysis['pronic_divisor'] = pronic_div
    analysis['sphenic'] = (powsum == 3) and sqrfr
    analysis['primorial'] = primorial
    analysis['smoothness'] = smoothness
    analysis['roughness'] = roughness
    analysis['regular'] = regularity
    analysis['unusual'] = unusual
    analysis['refactorable'] = refactorable
    analysis['arithmetic'] = arithmetic
    analysis['abundant'] = abundant
    analysis['deficient'] = abundance < 0
    analysis['almstprm'] = almstprm
    analysis['factorial'] = factorial
    if factorial:
        analysis['factorial_base'] = factorial_base
    return analysis