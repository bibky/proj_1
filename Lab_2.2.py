#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Задание 2.2: Поиск простых чисел. Напишите функцию, которая находит все простые числа от 2 до заданного числа n. Используйте цикл for и проверку делимости"
lst = []
def prime_numbers(n):
    for i in range(2, n+1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            lst.append(i)
print(lst)                
prime_numbers(7)

