def write_sale(argv):
    with open('bakery.csv', 'a', encoding='utf-8') as f:
        program, *args = argv
        for el in args:
            f.write(f'{el:>15}\n')
        return 0