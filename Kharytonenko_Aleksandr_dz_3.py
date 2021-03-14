for i in range(1, 21):
    end =  ''
    num = i % 10

    if (i >= 5 and i <= 20) or (num >= 5) or (num == 0):
        end = 'ов'
    elif num > 1 and num < 5:
        end = 'а'
    print(str(i) + ' процент' + end)
