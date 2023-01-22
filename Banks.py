M = int(input("Введите сумму желаемого взноса: "))

per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
tkb = per_cent['ТКБ'] * 0.01 * M
skb = per_cent['СКБ'] * 0.01 * M
vtb = per_cent['ВТБ'] * 0.01 * M
sber = per_cent['СБЕР'] * 0.01 * M
deposit = [tkb, skb, vtb, sber]
deposit_max = int(max(deposit))

print("Максимальная сумма которую вы можете забрать - ", deposit_max, "₽")
