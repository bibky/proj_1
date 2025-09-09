#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Создайте функцию, которая определяет, является ли год високосным. Год високосный, если - Он делится на 4, но не на 100, ИЛИ Он делится на 400
def leap_years(year):
    res = 'Год високосный' if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0) else 'Год обычный'
    return res

leap_years(2024)

