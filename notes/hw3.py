#################################################
# Hw3
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
# Hw3 problems
#################################################

### TESTING PROBLEM ###

def testPigLatin(pigLatin):
    return 42

### DEBUGGING PROBLEMS ###
### NOTE: remove the triple-quotes before you start debugging. ###

"""def hasLetterC(s):
    s = s.lower()
    for i in range(len(s)):
        if s[i] = 'c':
            return True
    return False"""

"""def findShortFruits(fruits):
    count = 0
    for fruit in fruits.split("-"):
        if len(friut) < 6 and len(fruit) > 0:
            count += 1
    return count"""

"""def hasConsecutiveDigits(n):
    if n < 0:
        return hasConsecutiveDigits(-n)
    while n > 0:
        nextN = n / 10
        if n % 10 == nextN % 10:
            return True
        n = nextN
    return False"""

### STYLE PROBLEM ###

def is_undulating(n):
    if n < 100:
        return False
    a = n % 10
    b = (n // 10) % 10
    n = n // 100
    blah = True
    while n > 0:
        digit = n % 10
        if blah:
          if digit != a:
              return False
        if (not blah):
            if digit != b:
                return False
        blah = not blah
        n = n // 10
    return a - b != 0

def nthUndulatingNumber(n):
    f= 0
    g =0
    while f<= n :
        g+=1
        if is_undulating(g):
            f += 1
    return g

### ALGORITHMIC THINKING PROBLEM ###

def nthPradishNumber(n):
    return 42

def longestSubpalindrome(s):
    return 42

##### Bonus #####

def getEvalSteps(expr):
    return 42

#################################################
# Hw3 Test Functions
#################################################

def pigLatin1(s):
    if s == "":
        return ""
    result = ""
    for word in s.split():
        index = 0
        for i in range(len(word)):
            if word[i] in 'aeio':
                index = i
                break
        if index == 0:
            newWord = word + "yay"
        else:
            newWord = word[index:] + word[:index] + "ay"
        result += newWord + " "
    return result[:-1]

def pigLatin2(sent):
  res = ""
  for s in sent.split(" "):
    if(s[0] in "aeiou"):
      res += s + "yay "
    else:
      i = 0
      while(s[i] not in "aeiou"):
        i += 1
      res += s[i:] + s[0:i]
      res += "ay "
  return res[:-1]

def findFirstVowel(word):
    vowels = "aeiou"
    for i in range(len(word)):
        c = word[i]
        if c in vowels:
            break
    return i
def pigLatin3(sentence):
    vowels = "aeiou"
    result = ""
    for word in sentence.split(" "):
        if word[0] not in vowels:
            i = findFirstVowel(word)
            result += word[i:] + word[:i] + "ay" + " "
        else:
            result += word + "yay" + " "
    return result

def findVowel(word):
    vowels = "aeiou"
    for i in range(len(word)): 
        if word[i] in vowels:
            return i
def pigLatin4(s):
    result = ""
    vowels = "aeiou"
    for word in s.split():
        if word.isalpha() and word == word.lower():
            if word[0] in vowels: 
                toAdd = word + "yay"
            else: 
                consonantIndex = findVowel(word)
                toAdd = word[consonantIndex:] + word[:consonantIndex] + "ay"
            result += toAdd + " "
    return result.strip()

def pigLatin5(s):
    result=""
    for word in s.split():
        result += (word+"yay ")
    return result.strip()

def testTestPigLatin():
    print("Testing testPigLatin()...")

    successCount = 0
    try:
        testPigLatin(pigLatin1)
        print("pigLatin1: passed")
        successCount += 1
    except:
        print("pigLatin1: failed")

    try:
        testPigLatin(pigLatin2)
        print("pigLatin2: passed")
        successCount += 1
    except:
        print("pigLatin2: failed")

    try:
        testPigLatin(pigLatin3)
        print("pigLatin3: passed")
        successCount += 1
    except:
        print("pigLatin3: failed")

    try:
        testPigLatin(pigLatin4)
        print("pigLatin4: passed")
        successCount += 1
    except:
        print("pigLatin4: failed")

    try:
        testPigLatin(pigLatin5)
        print("pigLatin5: passed")
        successCount += 1
    except:
        print("pigLatin5: failed")

    # Only one pigLatin function should pass the test cases, and it should
    # be the correct one!
    assert(successCount == 1)
    print("Passed!")

def testHasLetterC():
    print("Testing hasLetterC()...", end="")
    assert(hasLetterC("cookie") == True)
    assert(hasLetterC("banana") == False)
    assert(hasLetterC("ace") == True)
    assert(hasLetterC("attorney") == False)
    print("Passed!")

def testFindShortFruits():
    print("Testing findShortFruits()...", end="")
    assert(findShortFruits("apple-banana-kiwi-pumpkin") == 2)
    assert(findShortFruits("") == 0)
    assert(findShortFruits("cucumber-grapefruit-pineapple") == 0)
    assert(findShortFruits("fig-lemon-lime") == 3)
    assert(findShortFruits("berry") == 1)
    print("Passed!")

def testHasConsecutiveDigits():
    print("Testing hasConsecutiveDigits()...", end="")
    assert(hasConsecutiveDigits(0) == False)
    assert(hasConsecutiveDigits(123456789) == False)
    assert(hasConsecutiveDigits(1212) == False)
    assert(hasConsecutiveDigits(1212111212) == True)
    assert(hasConsecutiveDigits(33) == True)
    print("Passed!")

def testNthPradishNumber():
    print("Testing nthPradishNumber()...", end="")
    assert(nthPradishNumber(0) == 11)
    assert(nthPradishNumber(1) == 1102)
    assert(nthPradishNumber(2) == 1111)
    assert(nthPradishNumber(3) == 1120)
    assert(nthPradishNumber(4) == 2002)
    assert(nthPradishNumber(5) == 2011)
    assert(nthPradishNumber(6) == 2020)
    assert(nthPradishNumber(7) == 102003)
    print("Passed!")

def testLongestSubpalindrome():
    print("Testing longestSubpalindrome()...", end="")
    assert(longestSubpalindrome("ab-4-be!!!") == "b-4-b")
    assert(longestSubpalindrome("abcbce") == "cbc")
    assert(longestSubpalindrome("aba") == "aba")
    assert(longestSubpalindrome("m") == "m")
    assert(longestSubpalindrome("when he said madamimadam i laughed") == \
                                " madamimadam ")
    print("Passed!")

def testBonusGetEvalSteps():
    print("Testing getEvalSteps()...", end="")
    assert(getEvalSteps("0") == "0 = 0")
    assert(getEvalSteps("2") == "2 = 2")
    assert(getEvalSteps("3+2") == "3+2 = 5")
    assert(getEvalSteps("3-2") == "3-2 = 1")
    assert(getEvalSteps("3**2") == "3**2 = 9")
    assert(getEvalSteps("31%16") == "31%16 = 15")
    assert(getEvalSteps("31*16") == "31*16 = 496")
    assert(getEvalSteps("32//16") == "32//16 = 2")
    assert(getEvalSteps("2+3*4") == "2+3*4 = 2+12\n      = 14")
    assert(getEvalSteps("2*3+4") == "2*3+4 = 6+4\n      = 10")
    assert(getEvalSteps("2+3*4-8**3%3") == """\
2+3*4-8**3%3 = 2+3*4-512%3
             = 2+12-512%3
             = 2+12-2
             = 14-2
             = 12""")
    assert(getEvalSteps("2+3**4%2**4+15//3-8") == """\
2+3**4%2**4+15//3-8 = 2+81%2**4+15//3-8
                    = 2+81%16+15//3-8
                    = 2+1+15//3-8
                    = 2+1+5-8
                    = 3+5-8
                    = 8-8
                    = 0""")
    print("Passed!")

#################################################
# Hw3 Main
#################################################

def testAll():
    testTestPigLatin()
    testHasLetterC()
    testFindShortFruits()
    testHasConsecutiveDigits()
    testNthPradishNumber()
    testLongestSubpalindrome()
    testBonusGetEvalSteps()

def main():
    cs112_s18_week3_linter.lint() # check style rules
    testAll()

if __name__ == '__main__':
    main()
