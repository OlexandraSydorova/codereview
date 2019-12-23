"""Дано текст довільної довжини, може містити літери латинського алфавіту, пробіли та розділові знаки (,.:;!?-);
Результат роботи: список слів (у нижньому регістрі), які зустрічаються в тексті найменшу кількість раз.
Слова, записані через дефіс, вважати двома словами (наприклад, "hand-made").
Слова у різних відмінках, числах та з іншими перетвореннями (наприклад, "page" та "pages") вважаються різними словами.
Регістр слів -- навпаки, не має значення: слова "page" та "Page" вважаються 1 словом.
 Якщо слів, які зустрічаються найменше, декілька -- вивести їх в алфавітному порядку.
Приклад: 'Hello,Hello, my dear!'
Результат: [my,dear]"""
import re
def find_text(prompt):
    text = input(prompt)
    while not bool(re.match(r'[A-Z]*[a-z]*[\s]*[,.:;!?]*',text)):
        text = input(prompt)
    text.split()
    text.split('-')
    index1 = 0
    index2 = 0
    while index1<len(text):
        while index2<len(text[index1]):
            if text[index1][index2].isupper():
                text[index1] = text[index1][:index2]+text[index1][index2].lower()+text[index1][index2+1:]
            index2+=1
        index1+=1

    return text


text = find_text("Введіть рядок ")
print(text)