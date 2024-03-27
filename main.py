def anagram():
    word1 = word1.replace(" ", "").lower()
    word2 = word2.replace(" ", "").lower()
    return sorted(word1) == sorted(word2)


if __name__ == '__main__':
    word1 = input("Enter the first word: ")
    word2 = input("Enter the second word: ")
    if anagram(word1, word2):
        print("True")
    else:
        print("False")