#################################################
# Colab3
#################################################

import cs112_s18_week3_linter
import math
import string

#################################################
# Helper functions
#################################################

def almostEqual(d1, d2, epsilon=10**-7):
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

import decimal
def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

#################################################
# Colab3 problems
########################

### TESTING PROBLEM ###

def testIsEquidigital(isEquidigital):
    return 42

### DEBUGGING PROBLEMS ###
### NOTE: remove the triple-quotes before you start debugging. ###

"""def countEvenDigits(n):
    if n < 0:
        return countEvenDigits(-n)
    elif n == 0:
        return 1
    count = 0
    while n > 0:
        digit = n % 10
        if digit % 2 == 0
            count += 1
        n = n // 10
    return count"""

"""def hasDoubleLetters(s):
    for i in range(len(s)):
        if s[i] == s[i+1]:
            return True
    return False"""

"""import string
def largestNumber(s):
    biggest = None
    for word in s.split():
        allNumbers = True
        for i in range(len(word)):
            if word[i] not in string.digits:
                allNumbers = False
        if allNumbers:
            n = int(word)
            if biggest == None or n > biggest:
                n = biggest
    return biggest"""

### STYLE PROBLEM ###

def areAnagrams(s1, s2):
    if len(s1) != len(s2):
        return False
        print("bad case")
    if len(s1) == len(s2):
        for str in s1:
            one = 1
            count_matches_1 = 0
            count_matches_2 = 0
            for i in range(len(s1)):
                if s1[i] == str:
                    count_matches_1 += one
            for i in range(len(s2)):
                if s2[i] == str:
                    count_matches_2 += one
            if count_matches_1 != count_matches_2:
                return False
        return True

### ALGORITHMIC THINKING ###

def nthKaprekarNumber(n):
    return 42

def mostFrequentLetters(s):
    return 42

#################################################
# Colab3 Test Functions
#########################################################################

def isPrime(n):
    if (n < 2):
        return False
    for factor in range(2,n):
        if (n % factor == 0):
            return False
    return True

def isEquidigital1(n):
    if n < 2:
        return False
    digitsInN = len(str(n))
    digitsInFactors = 0
    for factor in range(2, n):
        if n % factor == 0 and isPrime(factor):
            digitsInFactors += len(str(factor))
    return digitsInN == digitsInFactors


def digitCount2(n):
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count

def isEquidigital2(n):
    numDigits = digitCount2(n)
    primeFactorDigitCount = 0
    for potentialFactor in range(2,n+1):
        if n % potentialFactor == 0:
            if isPrime(potentialFactor):
                primeFactorDigitCount += digitCount2(potentialFactor)
    return numDigits == primeFactorDigitCount


def digitCount3(n):
    return len(str(n))

def isEquidigital3(n):
    if n < 3:   return False
    numDigits = digitCount3(n)
    primeDigits = 0

    for factor in range(2, n):
        if n % factor == 0 and isPrime(factor):
            primeDigits += digitCount3(factor)
    if isPrime(n):
        primeDigits += digitCount3(n)

    return primeDigits - numDigits <= 1


def digitCount4(n):
    n = abs(n)
    count = 1
    while(n > 9):
        count += 1
        n //= 10
    return count

def isEquidigital4(n):
    factorDigits = 0
    for factor in range(2, n + 1):
        if(n%factor == 0 and isPrime(factor)):
            factorDigits += digitCount4(factor)
    return factorDigits == digitCount4(n)

def testTestIsEquidigital():
    print("Testing testIsEquidigital()...")

    successCount = 0
    try:
        testIsEquidigital(isEquidigital1)
        print("isEquidigital1: passed")
        successCount += 1
    except:
        print("isEquidigital1: failed")

    try:
        testIsEquidigital(isEquidigital2)
        print("isEquidigital2: passed")
        successCount += 1
    except:
        print("isEquidigital2: failed")

    try:
        testIsEquidigital(isEquidigital3)
        print("isEquidigital3: passed")
        successCount += 1
    except:
        print("isEquidigital3: failed")

    try:
        testIsEquidigital(isEquidigital4)
        print("isEquidigital4: passed")
        successCount += 1
    except:
        print("isEquidigital4: failed")

    # Only one isEquidigital function should pass the test cases, and it should
    # be the correct one!
    assert(successCount == 1)
    print("Passed!")

def testCountEvenDigits():
    print("Testing countEvenDigits...", end="")
    assert(countEvenDigits(23456) == 3)
    assert(countEvenDigits(8) == 1)
    assert(countEvenDigits(1) == 0)
    print("Passed!")

def testHasDoubleLetters():
    print("Testing hasDoubleLetters...", end="")
    assert(hasDoubleLetters("three") == True)
    assert(hasDoubleLetters("once") == False)
    assert(hasDoubleLetters("llama") == True)
    assert(hasDoubleLetters("") == False)
    print("Passed!")

def testLargestNumber():
    print("Testing largestNumber...", end="")
    assert(largestNumber("I saw 3 dogs, 17 cats, and 14 cows!") == 17)
    assert(largestNumber("One person ate two hot dogs!") == None)
    assert(largestNumber("I only want 1") == 1)
    assert(largestNumber("123456789 is the highest I can count") == 123456789)
    print("Passed!")

def testNthKaprekarNumber():
    print('Testing nthKaprekarNumber()...', end='')
    assert(nthKaprekarNumber(0) == 1)
    assert(nthKaprekarNumber(1) == 9)
    assert(nthKaprekarNumber(2) == 45)
    assert(nthKaprekarNumber(3) == 55)
    assert(nthKaprekarNumber(4) == 99)
    assert(nthKaprekarNumber(5) == 297)
    assert(nthKaprekarNumber(6) == 703)
    assert(nthKaprekarNumber(7) == 999)
    print('Passed.')

def testMostFrequentLetters():
    print("Testing mostFrequentLetters()...", end="")
    
    s = "We attack at Dawn"
    result = "atwcdekn"
    assert(mostFrequentLetters(s) == result)
    
    s = "Note that digits, punctuation, and whitespace are not letters!"
    result = "teanioscdhpruglw"
    assert(mostFrequentLetters(s) == result)
    
    s = ""
    result = ""
    assert(mostFrequentLetters(s) == result)
    
    print("Passed!")

#################################################
# Colab3 Main
################################################

def testAll():
    testTestIsEquidigital()
    testCountEvenDigits()
    testHasDoubleLetters()
    testLargestNumber()
    testNthKaprekarNumber()
    testMostFrequentLetters()

def main():
    cs112_s18_week3_linter.lint() # check style rules
    testAll()

if __name__ == '__main__':
    main()
