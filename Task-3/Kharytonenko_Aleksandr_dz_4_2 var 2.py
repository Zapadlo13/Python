try:
    from translate import Translator
except:
    print('Не установлен модуль "translate"  для коректной работы!')
    exit(0)


def num_translate(word):
    translator = Translator(to_lang='ru')
    translation = translator.translate(word)
    if translation == None:
        return 'None Перевод не найден!'
    else:
        return translation


def num_translate_adv(word):
    translator = Translator(to_lang='ru')
    translation = translator.translate(word)

    if translation == None:
        return 'None Перевод не найден!'
    else:
        result = translation.lower()
        return result.title() if word[0] == word[0].upper() else result


print('Задание 1')
print(num_translate(input('Введите числительное от 0 до 10 на английском языке: ')))
print('Задание 2*')
print(num_translate_adv(input('Введите числительное от 0 до 10 на английском языке: ')))
