def odd_nums(max_num):
    return (i for i in range(max_num) if i % 2)


odd_to_15 = odd_nums(15)

print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
