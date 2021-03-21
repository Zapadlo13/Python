import random


def get_jokes(unique_values, count):
    result = []
    if unique_values == 'Y':
        random.shuffle(nouns)
        random.shuffle(adverbs)
        random.shuffle(adjectives)

    for i in range(count):
        if unique_values == 'Y':
            if i <= len(nouns) - 1:
                result.append(nouns[i] + ' ' + adverbs[i] + ' ' + adjectives[i])
            else:
                print('Уникальные шутки закончились!')
                break
        else:
            result.append(
                str(random.choice(nouns)) + ' ' + str(random.choice(adverbs)) + ' ' + str(random.choice(adjectives)))

    return result


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

unique_values = input('Введиет Y для запрета повторов слов в шутках:')
jokes = get_jokes(unique_values, int(input('Введиет кол-во шуток:')))

print(jokes)
