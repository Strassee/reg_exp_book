from pprint import pprint
## Читаем адресную книгу в формате CSV в список contacts_list:
import csv
import re

with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

pattern = re.compile(r"\+*(7|8)\s*\(*(\d{3})\)*\s*-*(\d{3})-*(\d{2})-*(\d{2})\s*\(*(доб.)*\s*(\d+)*\)*")
subst_pattern = r"+7(\2)\3-\4-\5 \6\7" # +7(999)999-99-99 доб.9999

for i in contacts_list:
    lfs = []
    for y in range(0, 3):
        lfs += i[y].split()
    for x in range(0, len(lfs)):
        i[x] = lfs[x]

indexes_del = []
for i in contacts_list:
    for x in range(contacts_list.index(i) + 1, len(contacts_list)):
        if i[0] == contacts_list[x][0] and i[1] == contacts_list[x][1]:
            for y in range (2, 7):
                if i[y] == '':
                    i[y] = contacts_list[x][y]
                else:
                    continue
            indexes_del.append(x)
    i[5] = pattern.sub(subst_pattern, i[5])
indexes_del.sort(reverse=True)
for x in indexes_del:
    del contacts_list[x]
                    
# pprint(contacts_list)

## 1. Выполните пункты 1-3 задания.
## Ваш код

## 2. Сохраните получившиеся данные в другой файл.
## Код для записи файла в формате CSV:
with open("phonebook.csv", encoding='utf-8', mode="w", newline='') as f:
    datawriter = csv.writer(f, delimiter=',')
  
## Вместо contacts_list подставьте свой список:
    datawriter.writerows(contacts_list)