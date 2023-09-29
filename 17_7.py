per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
print('Процентные ставки')
print(per_cent)
money=float(input('Введите сумму инвестирования: '))
deposit=[]
deposit.append(money*5.6/100)
deposit.append(money*5.9/100)
deposit.append(money*4.28/100)
deposit.append(money*4.0/100)
print(deposit)
print('Максимальная сумма, которую вы можете заработать — ',max(deposit))