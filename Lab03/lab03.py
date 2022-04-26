def integerDivision(n, k):
    if n == 0:
        return 0
    elif n < k:
        return 0
    else:
        n = n-k
        return 1 + integerDivision(n, k)

def collectEvenInts(listOfInt):
    collected_list = []
    
    if not listOfInt:
        return collected_list

    if listOfInt[0] % 2 == 0:
        collected_list.append(listOfInt[0])
        listOfInt.pop(0)
        
        return collected_list + collectEvenInts(listOfInt)

    listOfInt.pop(0)
    
    return collectEvenInts(listOfInt)


def countVowels(someString):
    counter = 0
    
    if not someString:
        return counter

    charToCheck = someString[0]
    if charToCheck == 'a' or charToCheck == 'e' or charToCheck == 'i' or charToCheck == 'o' or charToCheck == 'u' \
        or charToCheck == 'A' or charToCheck == 'E' or charToCheck == 'I' or charToCheck == 'O' or charToCheck == 'U':
            counter += 1
            someString = someString[1:]
            return counter + countVowels(someString)
    
    someString = someString[1:]
    return countVowels(someString)

def reverseString(s):
    if not s:
        return ''
    else:
        first_char = s[0]
        return reverseString(s[1:]) + first_char

def removeSubString(s, sub):
    new_string = ""
    if not s:
        return new_string
    if len(s) < len(sub):
        return new_string
    check_string = s[0:len(sub)]
    if check_string == sub:
        s = s[len(sub):]
        return removeSubString(s, sub)  
    new_string = s[0]
    s = s[1:]
    return new_string + removeSubString(s, sub)

