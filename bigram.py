import pandas as pd
import random

f_percent = open('percent.txt', 'w')
f_itog = open('itog.txt', 'w')
n = int(input('Введите количество последовательностей:'))
u = int(input('Введите длину последовательносте:'))
count = 0
s = int(input('Введите количество состояний(от 0 до 10):'))
posled = []
itog = [[0] * s for i in range(s)]
for i in range(u):
    q = ''
    for j in range(n):
        q += (str(random.randint(0, s - 1)))
    posled.append(q)

for i in posled:
    a = i
    for j in range(len(a) - 1):
        itog[int(a[j + 1])][int(a[j])] += 1
        count += 1
    df_itog = pd.DataFrame({i: itog[i] for i in range(s)})
    for i in range(s):
        for j in range(s):
            itog[i][j] = round(itog[i][j] / count, 4)

    df_percent = pd.DataFrame({i: itog[i] for i in range(s)})
    f_itog.write(f'Все биграммы для ряда: {a}')
    f_percent.write(f'Частота встреченных биграмм для ряда: {a}')
    f_itog.write('\n')
    f_percent.write('\n')
    f_itog.write(df_itog.to_string(header=True, index=True))
    f_percent.write(df_percent.to_string(header=True, index=True))
    f_itog.write(2*'\n')
    f_percent.write(2*'\n')
    count = 0
    itog = [[0] * s for i in range(s)]
