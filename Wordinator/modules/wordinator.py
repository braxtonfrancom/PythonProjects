# Braxton Francom
# CS1400 - LW2
# Assignment 10

class Wordinator:
    def __init__(self, word):
        self.__word = word

    def getWord(self):
        return self.__word

    def __str__(self):
        return self.__word

    def __lt__(self, other):   #first word
        if self.__word.lower() >= other.getWord().lower():
            return False
        elif other.getWord().lower() > self.__word.lower():
            return True

    def __add__(self, other):    #big word
        return (self.__word + other.getWord()).capitalize()

    def __mul__(self, factor):
        return (self.__word * factor).upper()

    def __truediv__(self, other):
        length = len(self.__word)
        newWord = ""
        for i in range(len(self.__word)):
            newWord += (self.__word[i] + other.getWord()[i])

        if len(self.__word) > len(other.getWord()):
            newWord += self.__word[len(other.getWord()):]
        elif len(other.getWord()) > len(self.__word):
            newWord += other.getWord()[len(self.__word):]
        return newWord.capitalize()

    def __mod__(self, other):
        words = [self.__word,other.getWord()]
        result = []
        for word in words:
            trimLength = ((len(word) + 2) // 4)
            result.append(word[trimLength:len(word)-trimLength])
        return result[0],result[1]


    def __sub__(self, other):
        newStr = []
        words = [self.__word, other.getWord()]

        for word in words:
            temp = ''
            for char in word:
                if char.isupper():
                    value = ord(char)
                    value += 32
                    temp += chr(value)
                elif char.islower():
                    value = ord(char)
                    value -= 32
                    temp += chr(value)
            newStr.append(temp)
        return newStr[0], newStr[1]


    def backWordSlice(self):
        return self.__word[::-1]

    def backWordManual(self):
        string1 = ""
        length = len(self.__word)
        for i in range(len(self.__word)-1,-1,-1):
            string1 += self.__word[i]
        return string1
