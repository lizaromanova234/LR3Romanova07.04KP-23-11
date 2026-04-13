#ЛР3 Общее задание

#1 задание делала с Рубеном
# import os
# Sec_Romanova_1= os.environ['Sec_Romanova_1']
# print (Sec_Romanova_1)

# import os
# Sec_Romanova_2= os.environ['Sec_Romanova_2']
# print (Sec_Romanova_2)

# import os
# Sec_Romanova_3= os.environ['Sec_Romanova_3']
# print (Sec_Romanova_3)

#2 задание (Вариант 2) Работала с Глуховой Анной
#линейный способ
# from sympy import *
# k, T, C, L = symbols('k T C L')
# C_ost = 50000
# Am_lst =[]
# C_ost_lst=[]
# for i in range(9):
#   Am = (C-L)/T #что это означает? - это формула амортизации
#   C_ost -= Am.subs({C:50000, T:9, L:0})
#   Am_lst.append(round(Am.subs({C: 50000, T:9, L:0}),2))
#   C_ost_lst.append(round(C_ost, 2))
# print('Am_lst:', Am_lst)
# print('C_ost_lst:', C_ost_lst)

# #способ уменьшаемого остатка
# Aj=0
# C_ost = 50000
# Am_lst_2=[]
# C_ost_lst_2=[] #Что это?
# for i in range(9):
#   Am = k*1/T*(C - Aj)
#   C_ost -= Am.subs({C:50000, T:9, k:2})
#   Am_lst_2.append(round(Am.subs({C:50000, T:9, k:2}), 2))
#   Aj += Am
#   C_ost_lst_2.append(round(C_ost,2))
# print('Am_lst_2:', Am_lst_2) #Что это? - вывод списка амортизации
# print('C_ost_lst_2:', C_ost_lst_2)

# #Контейнер табличного вывода
# import pandas as pd
# Y = range(1, 10) #Что это? - последовательность целых чисел от 1 до 9
# table1 = list(zip(Y, C_ost_lst, Am_lst))
# table2 = list(zip(Y, C_ost_lst_2, Am_lst_2))
# tfame = pd.DataFrame(table1, columns = ['Y', 'C_ost_lst', 'Am_lst'])
# tfame2 = pd.DataFrame(table2, columns = ['Y', 'C_ost_lst_2', 'Am_lst_2'])
# print(tfame)
# print(tfame2)

# #визуализация

# import numpy as np
# import matplotlib.pyplot as plt
# plt.plot(tfame['Y'], tfame['C_ost_lst'], label='Am')
# plt.savefig('chart7.png') #Что это? - сохранение графика 7 в файл
# plt.figure()
# plt.plot(tfame2['Y'], tfame2['C_ost_lst_2'], label='Am2')
# plt.savefig('chart8.png')
# plt.figure() #Что это? - создание нового окна для графика

# plt.figure()
# vals = Am_lst #Что это? - Присваивание переменной vals значения переменной Am_lst
# labels = [str(x) for x in range(1,10)]
# explode = (0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1)
# fig, ax = plt.subplots()
# ax.pie(vals, labels=labels, autopct='%1.1f%%', shadow=True, explode=explode, wedgeprops={'lw':1, 'ls':'--', 'edgecolor':"k"}, rotatelabels=True)
# ax.axis("equal")
# plt.savefig('chart9.png')
# plt.figure() #что это? - создание нового окна для графика

# plt.figure()
# vals = Am_lst_2
# labels = [str(x) for x in range(1,10)]
# explode = (0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1)
# fig, ax = plt.subplots()
# ax.pie(vals, labels=labels, autopct='%1.1f%%', shadow=True, explode=explode, wedgeprops={'lw':1, 'ls':'--', 'edgecolor':"k"}, rotatelabels=True)
# ax.axis("equal")
# plt.savefig('chart10.png')
# plt.clf() #Что это? - очистка текущего графика
# plt.figure()


# table1 = list(zip(Y, Am_lst))
# table2 = list(zip(Y, Am_lst_2))
# tframe = pd.DataFrame(table1, columns=['Y', 'Am_lst'])
# tframe2 = pd.DataFrame(table2, columns=['Y', 'Am_lst_2'])
# plt.bar(tfame['Y'], tfame['Am_lst'])
# plt.savefig('chart11.jpeg')
# plt.figure()
# plt.bar(tfame2['Y'], tfame2['Am_lst_2']) #Что это? - построение столбчатой диаграммы
# plt.savefig('chart12.jpeg')
# plt.figure()

#Проверила Глухова Анна, все супер!!! 100/100!
#Были изменены переменные и добавлены комментарии 
#Анна Глухова отвечала на вопросы
#Оценка ответов на вопросы 5/5, проверила Романова Елизавета.
#Задание номер 5 выполнено


#№7
# изменение со 2 на 6 вариант (15000/8)
# линейный способ
# from sympy import *
# k, T, C, L = symbols('k T C L')
# C_ost = 15000
# Am_lst =[]
# C_ost_lst=[]
# for i in range(8):
#   Am = (C-L)/T #что это означает? - это формула амортизации
#   C_ost -= Am.subs({C:15000, T:8, L:0})
#   Am_lst.append(round(Am.subs({C: 15000, T:8, L:0}),2))
#   C_ost_lst.append(round(C_ost, 2))
# print('Am_lst:', Am_lst)
# print('C_ost_lst:', C_ost_lst)

# #способ уменьшаемого остатка
# Aj=0
# C_ost = 15000
# Am_lst_2=[]
# C_ost_lst_2=[] #Что это?
# for i in range(8):
#   Am = k*1/T*(C - Aj)
#   C_ost -= Am.subs({C:15000, T:8, k:2})
#   Am_lst_2.append(round(Am.subs({C:15000, T:8, k:2}), 2))
#   Aj += Am
#   C_ost_lst_2.append(round(C_ost,2))
# print('Am_lst_2:', Am_lst_2) #Что это? - вывод списка амортизации
# print('C_ost_lst_2:', C_ost_lst_2)

# #Контейнер табличного вывода
# import pandas as pd
# Y = range(1, 9) #Что это? - последовательность целых чисел от 1 до 9
# table1 = list(zip(Y, C_ost_lst, Am_lst))
# table2 = list(zip(Y, C_ost_lst_2, Am_lst_2))
# tfame = pd.DataFrame(table1, columns = ['Y', 'C_ost_lst', 'Am_lst'])
# tfame2 = pd.DataFrame(table2, columns = ['Y', 'C_ost_lst_2', 'Am_lst_2'])
# print(tfame)
# print(tfame2)

# #визуализация

# import numpy as np
# import matplotlib.pyplot as plt
# plt.plot(tfame['Y'], tfame['C_ost_lst'], label='Am')
# plt.savefig('chart7.png') #Что это? - сохранение графика 7 в файл
# plt.figure()
# plt.plot(tfame2['Y'], tfame2['C_ost_lst_2'], label='Am2')
# plt.savefig('chart8.png')
# plt.figure() #Что это? - создание нового окна для графика

# plt.figure()
# vals = Am_lst #Что это? - Присваивание переменной vals значения переменной Am_lst
# labels = [str(x) for x in range(1,9)]
# explode = (0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1)
# fig, ax = plt.subplots()
# ax.pie(vals, labels=labels, autopct='%1.1f%%', shadow=True, explode=explode, wedgeprops={'lw':1, 'ls':'--', 'edgecolor':"k"}, rotatelabels=True)
# ax.axis("equal")
# plt.savefig('chart9.png')
# plt.figure() #что это? - создание нового окна для графика

# plt.figure()
# vals = Am_lst_2
# labels = [str(x) for x in range(1,9)]
# explode = (0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1)
# fig, ax = plt.subplots()
# ax.pie(vals, labels=labels, autopct='%1.1f%%', shadow=True, explode=explode, wedgeprops={'lw':1, 'ls':'--', 'edgecolor':"k"}, rotatelabels=True)
# ax.axis("equal")
# plt.savefig('chart10.png')
# plt.clf() #Что это? - очистка текущего графика
# plt.figure()


# table1 = list(zip(Y, Am_lst))
# table2 = list(zip(Y, Am_lst_2))
# tframe = pd.DataFrame(table1, columns=['Y', 'Am_lst'])
# tframe2 = pd.DataFrame(table2, columns=['Y', 'Am_lst_2'])
# plt.bar(tfame['Y'], tfame['Am_lst'])
# plt.savefig('chart11.jpeg')
# plt.figure()
# plt.bar(tfame2['Y'], tfame2['Am_lst_2']) #Что это? - построение столбчатой диаграммы
# plt.savefig('chart12.jpeg')
# plt.figure()



#Индивидуальное задание лр 3
#1 Для определенных в ТЗ компонентов интеграции создать в реплике необходимое количество секретных ключей.
# КОНТЕЙНЕР ЗАЩИТЫ ОТ СКРЫТНОГО ВКЛЮЧЕНИЯ В БОТ-СЕТЬ
# Вариант 12 

import os
import pandas as pd
import matplotlib.pyplot as plt

# ============================================================
# ПОЛУЧЕНИЕ СЕКРЕТНЫХ КЛЮЧЕЙ ИЗ REPlIT SECRETS
# ============================================================

REPUTATION_API_KEY = os.environ.get("REPUTATION_API_KEY", "КЛЮЧ НЕ НАЙДЕН")
DOMAIN_REPUTATION_API_KEY = os.environ.get("DOMAIN_REPUTATION_API_KEY", "КЛЮЧ НЕ НАЙДЕН")
PROMETHEUS_TOKEN = os.environ.get("PROMETHEUS_TOKEN", "КЛЮЧ НЕ НАЙДЕН")
ELK_API_KEY = os.environ.get("ELK_API_KEY", "КЛЮЧ НЕ НАЙДЕН")

print("\n" + "="*60)
print("ЗАГРУЖЕННЫЕ СЕКРЕТНЫЕ КЛЮЧИ:")
print("="*60)
print(f"REPUTATION_API_KEY: {REPUTATION_API_KEY}")
print(f"DOMAIN_REPUTATION_API_KEY: {DOMAIN_REPUTATION_API_KEY}")
print(f"PROMETHEUS_TOKEN: {PROMETHEUS_TOKEN}")
print(f"ELK_API_KEY: {ELK_API_KEY}")
print("="*60)

# ============================================================
# ОСНОВНАЯ ЧАСТЬ ПРОГРАММЫ
# ============================================================

# Данные
ip_addresses = [
    "185.130.5.253", "8.8.8.8", "94.23.15.12", "1.1.1.1",
    "193.42.4.1", "176.9.75.45", "8.8.4.4", "89.45.87.12",
    "5.188.86.45", "208.67.222.222"
]

C2_SERVERS = ["185.130.5.253", "94.23.15.12", "193.42.4.1", 
              "176.9.75.45", "89.45.87.12", "5.188.86.45"]

n = len(ip_addresses)

# Фиксированные данные
connections_count = [200, 50, 250, 10, 100, 5, 70, 180, 60, 30] #изменение
suspicious_port =   [0,   1,  0,   1,  0,   1,  1,  0,   1,  1] #изменение
unknown_process =   [1,   0,  1,   0,  1,   0,  0,  1,   0,  0]
high_traffic =      [1,   0,  1,   0,  1,   0,  0,  1,   0,  0]
night_activity =    [0,   1,  0,   1,  0,   1,  1,  0,   1,  1]

# Определяем C&C сервер
c2_server = []
for i in range(n):
    if ip_addresses[i] in C2_SERVERS:
        c2_server.append(1)
    else:
        c2_server.append(0)

# Расчет угрозы и решений
threat_level = []
decision = []

for i in range(n):
    threat = 0
    if connections_count[i] > 100:
        threat += 1
    if suspicious_port[i] == 1:
        threat += 1
    if unknown_process[i] == 1:
        threat += 2
    if high_traffic[i] == 1:
        threat += 1
    if c2_server[i] == 1:
        threat += 3
    if night_activity[i] == 1:
        threat += 1

    threat_level.append(threat)
    decision.append("BLOCK" if threat >= 3 else "ALLOW")

# Таблица результатов
data = list(zip(range(1, n+1), ip_addresses, connections_count, 
                suspicious_port, unknown_process, high_traffic, 
                c2_server, night_activity, threat_level, decision))

df = pd.DataFrame(data, columns=[
    "ID", "IP адрес", "Соединений", "Подозр. порт",
    "Подозр. процесс", "Высокий трафик", "C&C сервер",
    "Ночная активность", "Уровень угрозы", "Решение"
])

print("\nЗАЩИТА ОТ СКРЫТНОГО ВКЛЮЧЕНИЯ В БОТ-СЕТЬ (Вариант 12)")
print(df.to_string(index=False))
print("\nСтатистика решений:")
print(df["Решение"].value_counts())

# ============================================================
# ВИЗУАЛИЗАЦИЯ
# ============================================================

plt.style.use('ggplot')

# График 1: Количество соединений по IP
plt.figure(figsize=(14, 6))
plt.plot(ip_addresses, df["Соединений"], marker='o', color='blue')
plt.title("Количество сетевых соединений по IP-адресам")
plt.xlabel("IP-адрес")
plt.ylabel("Количество соединений")
plt.xticks(rotation=45, ha="right")
plt.grid(True)
plt.tight_layout()
plt.savefig("chart_connections.png")
plt.close()

# График 2: Уровень угрозы по IP
plt.figure(figsize=(14, 6))
plt.plot(ip_addresses, df["Уровень угрозы"], marker='s', color='red')
plt.title("Уровень угрозы скрытного включения в бот-сеть")
plt.xlabel("IP-адрес")
plt.ylabel("Уровень угрозы (баллы)")
plt.xticks(rotation=45, ha="right")
plt.grid(True)
plt.tight_layout()
plt.savefig("chart_threat.png")
plt.close()

# График 3: Круговая диаграмма решений
plt.figure(figsize=(8, 8))
decision_counts = df["Решение"].value_counts()
labels = ["Разрешить", "Заблокировать"]
sizes = [decision_counts.get("ALLOW", 0), decision_counts.get("BLOCK", 0)]
colors = ['#66b3ff', '#ff6666']
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90,
        shadow=True, explode=(0.05, 0.1), colors=colors)
plt.title("Распределение решений контейнера")
plt.savefig("chart_pie.png")
plt.close()

# График 4: Гистограмма факторов риска
plt.figure(figsize=(10, 6))
risk_factors = df[["Подозр. порт", "Подозр. процесс", "Высокий трафик", 
                   "C&C сервер", "Ночная активность"]].sum()
risk_factors.plot(kind='bar', color=['blue', 'red', 'green', 'purple', 'orange'])
plt.title("Суммарные срабатывания факторов риска")
plt.ylabel("Количество случаев")
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.savefig("chart_risk_factors.png")
plt.close()

print("\nСозданные графики:")
print("  - chart_connections.png")
print("  - chart_threat.png")
print("  - chart_pie.png")
print("  - chart_risk_factors.png")
print("\nРАБОТА ЗАВЕРШЕНА")