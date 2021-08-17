def thesaurus(*args):
    names = {}

    for el in args:
        if names.get(el[0]) == None:
            names[el[0]] = [el]
        else:
            el_dict = names[el[0]]
            el_dict.append(el)
            names[el[0]] = el_dict
    print(names)


def sort_dict(names):
    list_keys = list(names.keys())
    list_keys.sort()
    names_sort = {}
    for i in list_keys:
        names_sort[i] = (names[i])

    return names_sort


def thesaurus_adv(*args):
    names = {}

    for el in args:
        lst = el.split()
        if names.get(lst[1][0]) == None:
            names[lst[1][0]] = {lst[0][0]: [el]}
        else:
            el_dict = names[lst[1][0]]
            if el_dict.get(lst[0][0]) == None:
                el_dict[lst[0][0]] = {lst[0][0]: [el]}
            else:
                el_dict_2 = el_dict[lst[0][0]]
                el_dict_2.append(el)
                el_dict[lst[0][0]] = el_dict_2

    names_sort = sort_dict(names)
    print(names_sort)


print('Задание 3')
thesaurus("Иван", "Мария", "Петр", "Илья")
print('Задание 4*')
thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
