from lab03 import *

def test_integerDivision1():
    assert integerDivision(27,4) == 6
    assert integerDivision(25,5) == 5
    assert integerDivision(300,1) == 300
def test_integerDivision2():
    assert integerDivision(54,6) == 9
    assert integerDivision(26,12) == 2
    assert integerDivision(5050,50) == 101
def test_collectEvenInts3():
    assert collectEvenInts([1,2,3,4,5]) == [2,4]
    assert collectEvenInts([2,2,3,4,5]) == [2,2,4]
    assert collectEvenInts([8,2,5,4,6]) == [8,2,4,6]
def test_collectEvenInts4():
    assert collectEvenInts([100,100,100,100,100]) == [100,100,100,100,100]
    assert collectEvenInts([2,4,6,8,10]) == [2,4,6,8,10]
    assert collectEvenInts([1,3,5,7,9]) == []
    
def test_countVowels5():
    assert countVowels("This Is A String") == 4
    assert countVowels("America") == 4
    assert countVowels("meta World Piece") == 6
    assert countVowels("AEIOUaeiou") == 10

def test_reverseString6():
    assert reverseString("CMPSC9") == "9CSPMC"
    assert reverseString("RACECAR") == "RACECAR"
    assert reverseString("AMERICA") == "ACIREMA"

def test_removeSubString7():
    assert removeSubString("Lolololol", "lol") == "Loo"
    assert removeSubString("mwahahahaha", "ha") == "mwa"
    assert removeSubString("lmaomao", "mao") == "l"
    
    
    