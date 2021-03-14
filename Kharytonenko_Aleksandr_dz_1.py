duration = int(input('Введите кол-во секунд:'))

seconds = duration % 60
minutes = duration // 60 % 60
hours = duration // 60 // 60 % 24
days = duration // 60 // 60 // 24

text = ''

if days > 0:
    text = text + ' дн:' + str(days)
if hours > 0 or days > 0:
    text = text + ' час:' + str(hours)
if minutes > 0 or hours > 0 or days > 0:
    text = text + ' мин:' + str(minutes)
if seconds > 0 or minutes > 0 or hours > 0 or days > 0:
    text = text + ' сек:' + str(seconds)

print(text)
