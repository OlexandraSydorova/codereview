"""Порахувати  кількість булевих змінних в списку"""
my_list = ['xdfgfd',13,1,True,15,False]
count = 0
for element in my_list:
    if isinstance(element,bool):
        count+=1
print(count)