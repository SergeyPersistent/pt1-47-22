

'''''1. Напишите программу, которая считает общую цену.
Вводится M рублей и N копеек цена,
а также количество S товара Посчитайте общую цену в рублях и копейках за L товаров. 
'''''

rub_input = int(input())
penny_input = int(input())
items = int(input())
rub_output = (rub_input * items)
penny_output = (penny_input * items)
print(rub_output)
print(penny_output)
