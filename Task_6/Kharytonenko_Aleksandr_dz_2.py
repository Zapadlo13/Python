def get_tuple(ln):
    return (
        line[:line.find(' - - ')], line[line.find('] "') + 3:line.find(' /')], line[line.find(' /'):line.find(' HTTP')])


def top10_spamer(spamers):
    list_spamer = list(spamers.items())
    list_spamer.sort(key=lambda i: i[1], reverse=True)
    min_itesm = min(len(list_spamer), 10)
    print('Топ ' + str(min_itesm) + ' ip по количеству запросов:')
    for i in range(min_itesm):
        print(list_spamer[i])


file_name = 'nginx_logs.txt'
rezult = []
spamers = {}
with open(file_name, 'r', encoding='utf-8') as file_1:
    for line in file_1:
        pars_line = get_tuple(line)
        rezult.append(pars_line)
        if spamers.get(pars_line[0]) == None:
            spamers[pars_line[0]] = 1
        else:
            spamers[pars_line[0]] = spamers[pars_line[0]] + 1

file_name = file_name.split('.')[0]
with open(file_name + '_result.txt', 'w', encoding='utf-8') as file_2:
    print(rezult, file=file_2, sep="\n")

print('Результат обработки был сохранен в ' + file_name + '_result.txt')
top10_spamer(spamers)
