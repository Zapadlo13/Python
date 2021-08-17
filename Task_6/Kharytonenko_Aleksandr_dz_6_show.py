import sys


def read_sale(argv):
    program, *args = argv
    result = str()
    with open('sales_save.txt', 'r', encoding='utf-8') as f:
        list_line = f.read().splitlines()
        if len(args) == 0:
            args.append(1)
            args.append(len(list_line))
        elif len(args) == 1:
            args.append(len(list_line))
        start = int(args[0])
        stop = int(args[1])
        if start == 0 or start > len(list_line) or stop < start or stop > len(list_line):
            return result
        for el in list_line[start - 1: stop]:
            result += f'{el}\n'
        return result.strip('\n')


if __name__ == '__main__':
    print(read_sale(sys.argv))