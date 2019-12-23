"""Вивести слова які закінчуються на велику букву"""
text = "dfgdfg vcbbvcH nmmnK wewer"
words = text.split()
i = 0
while i<len(words):
    word = words[i]
    if word[-1].isupper():
        print(word)
    i+=1
