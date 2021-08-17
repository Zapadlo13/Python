def my_gen(items1, items2):
    k = len(items1) - len(items2)
    if k > 0:
        for _ in range(k):
            items2.append(None)
    for tutor, klass in zip(items1, items2):
        yield (tutor, klass)

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

my_gener = my_gen(tutors, klasses)
print(type(my_gener),*my_gener)
