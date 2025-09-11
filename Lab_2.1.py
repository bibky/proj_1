#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Задание 2.1: Таблица умножения. Создайте программу, которая выводит таблицу умножения от 1 до 10
multiplication_table = []
for i in range(1, 11):
    row = []
    for j in range(1, 11):
        row.append(i*j)
    multiplication_table.append(row)
print(multiplication_table)  

