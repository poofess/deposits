per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

money = int(input("Введите сумму, которую вы планируете положить под проценты: "))

deposit = [money * percent / 100 for percent in per_cent.values()]

print("Накопленные средства за год вклада в каждом из банков:", deposit)

max_deposit = max(deposit)
print("Максимальная накопленная сумма за год:", max_deposit)

max_index = deposit.index(max_deposit)
max_bank = list(per_cent.keys())[max_index]

print(f"Максимальная сумма, которую вы можете заработать — {max_deposit} в банке {max_bank}")