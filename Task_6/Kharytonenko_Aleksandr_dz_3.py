import sys
import json

result_dict = {}
with open('users.csv', 'r', encoding='utf-8') as f_1, \
        open('hobby.csv', 'r', encoding='utf-8') as f_2:
    for hobbies, user in zip(f_2, f_1):
        result_dict[user.strip()] = hobbies.strip()
    for _ in f_2:
        sys.exit(1)
    for user in f_1:
        result_dict[user.strip()] = None

with open('result.json', 'w', encoding='utf-8') as result_file:
    json.dump(result_dict, result_file, ensure_ascii=False)
with open('result.json', 'r', encoding='utf-8') as f:
    result = json.load(f)
print(result)
