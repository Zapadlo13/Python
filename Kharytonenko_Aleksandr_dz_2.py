list_a = []
for i in range(1, 1000):
    if i % 2 == 1:
        list_a.append(i ** 3)

# Задание А
sum_num = 0

for i in list_a:
    num = i
    sum_el = 0
    while True:
        sum_el = sum_el + num % 10
        if num // 10 == 0:
            break
        else:
            num = num // 10
    if sum_el % 7 == 0:
        sum_num = sum_num + i

print('Задание 2 пункт а:' + str(sum_num))
# Задание C
for i, val in enumerate(list_a):
    list_a[i] = val + 17
# Задание B
sum_num = 0
for i in list_a:
    num = i
    sum_el = 0
    while True:
        sum_el = sum_el + num % 10
        if num // 10 == 0:
            break
        else:
            num = num // 10
    if sum_el % 7 == 0:
        sum_num = sum_num + i

print('Задание 2 пункт b:' + str(sum_num))
