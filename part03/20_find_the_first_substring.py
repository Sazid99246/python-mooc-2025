word = input("Please type in a word: ")
char = input("Please type in a character: ")

char_index = word.find(char)
if char_index != -1 and char_index + 2 < len(word):
    print(word[char_index:char_index + 3])
