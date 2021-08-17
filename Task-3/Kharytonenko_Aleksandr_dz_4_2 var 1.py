def getEnglishDictionary():
    english_dictionary = {
        'zero': 'ноль',
        'one': 'одни',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять'}

    return english_dictionary


def num_translate(word):
    english_dictionary = getEnglishDictionary()

    if english_dictionary.get(word) == None:
        return 'None Перевод не найден!'
    else:
        return english_dictionary[word]


def num_translate_adv(word):
    english_dictionary = getEnglishDictionary()

    if english_dictionary.get(word.lower()) == None:
        return 'None Перевод не найден!'
    else:
        result = english_dictionary[word.lower()]
        return result.title() if word[0] == word[0].upper() else result


print('Задание 1')
print(num_translate(input('Введите числительное от 0 до 10 на английском языке: ')))
print('Задание 2*')
print(num_translate_adv(input('Введите числительное от 0 до 10 на английском языке: ')))
