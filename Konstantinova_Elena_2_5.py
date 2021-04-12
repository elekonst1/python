# Создать вручную список, содержащий цены на товары (10–20 товаров), например:
# [57.8, 46.51, 97, ...]

# Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп (например «5 руб 04 коп»).
# Подумать, как из цены получить рубли и копейки, как добавить нули, если, например, получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).
# Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать, что объект списка после сортировки остался тот же).
# Создать новый список, содержащий те же цены, но отсортированные по убыванию.
# Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?



# A
#Вариант №1 более "красивая реализация"

goods_prices = [23, 761.72, 67.9, 12.7, 78.4, 90.4, 126.96, 21.8, 439.7, 453.82]
new_goods_prices = []
for good in goods_prices:
    rubles = int(good)
    penny = (good - int(good)) * 100
    new_goods_price = f'{rubles} руб {penny:02.0f} коп'
    new_goods_prices.append(new_goods_price)
new_goods_prices = ', '.join(new_goods_prices)
print(new_goods_prices)

#Вариант №2

goods_prices = [23, 761.72, 67.9, 12.7, 78.4, 90.4, 126.96, 21.8, 439.7, 453.82]
new_goods_prices = []
for good in goods_prices:
    rubles = int(good)
    penny = (good - int(good)) * 100
    new_goods_price = f'{rubles} руб {penny:02.0f} коп'
    new_goods_prices.append(new_goods_price)
message = ''
for item in new_goods_prices:
     message += item
     message += ','
     message += ' '
print(message)

# B
#Вывести цены, отсортированные по возрастанию, новый список не создавать
#(доказать, что объект списка после сортировки остался тот же).

goods_prices = [23, 761.72, 67.9, 12.7, 78.4, 90.4, 126.96, 21.8, 439.7, 453.82]
print(id(goods_prices))
goods_prices.sort()
print(id(goods_prices))
new_goods_prices = []
for good in goods_prices:
    rubles = int(good)
    penny = (good - int(good)) * 100
    new_goods_price = f'{rubles} руб {penny:02.0f} коп'
    new_goods_prices.append(new_goods_price)
new_goods_prices = ', '.join(new_goods_prices)
print(new_goods_prices)

#C
#Создать новый список, содержащий те же цены, но отсортированные по убыванию.
# Вариант 1
goods_prices = [23, 761.72, 67.9, 12.7, 78.4, 90.4, 126.96, 21.8, 439.7, 453.82]
print(id(goods_prices))
goods_prices = sorted(goods_prices)
print(id(goods_prices))
goods_prices.reverse()
print(id(goods_prices))
print(goods_prices)
new_goods_prices = []
for good in goods_prices:
    rubles = int(good)
    penny = (good - int(good)) * 100
    new_goods_price = f'{rubles} руб {penny:02.0f} коп'
    new_goods_prices.append(new_goods_price)
new_goods_prices = ', '.join(new_goods_prices)
print(new_goods_prices)

# Вариант 2
goods_prices = [23, 761.72, 67.9, 12.7, 78.4, 90.4, 126.96, 21.8, 439.7, 453.82]
print(id(goods_prices))
goods_prices.sort()
goods_prices = goods_prices[::-1]
print(id(goods_prices))
print(goods_prices)
new_goods_prices = []
for good in goods_prices:
    rubles = int(good)
    penny = (good - int(good)) * 100
    new_goods_price = f'{rubles} руб {penny:02.0f} коп'
    new_goods_prices.append(new_goods_price)
new_goods_prices = ', '.join(new_goods_prices)
print(new_goods_prices)


#Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?
goods_prices = [23, 761.72, 67.9, 12.7, 78.4, 90.4, 126.96, 21.8, 439.7, 453.82]
goods_prices.sort()
print(id(goods_prices))
goods_prices = goods_prices[::-1][:5]
print(id(goods_prices))
print(goods_prices)
for good in goods_prices:
    rubles = int(good)
    penny = (good - int(good)) * 100
    new_goods_price = f'{rubles} руб {penny:02.0f} коп'
    print(new_goods_price)
