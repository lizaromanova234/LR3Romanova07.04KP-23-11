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

# КОНТЕЙНЕР ЗАЩИТЫ ОТ СКРЫТНОГО ВКЛЮЧЕНИЯ В БОТ-СЕТЬ
# Вариант 12

import os
import pandas as pd
import matplotlib.pyplot as plt

# 1. ПОЛУЧЕНИЕ СЕКРЕТНЫХ КЛЮЧЕЙ

C2_BLACKLIST_API_KEY = os.environ.get("C2_BLACKLIST_API_KEY", "КЛЮЧ НЕ НАЙДЕН")
THREAT_INTELLIGENCE_KEY = os.environ.get("THREAT_INTELLIGENCE_KEY", "КЛЮЧ НЕ НАЙДЕН")
MONITORING_TOKEN = os.environ.get("MONITORING_TOKEN", "КЛЮЧ НЕ НАЙДЕН")


print("ЗАГРУЖЕННЫЕ СЕКРЕТНЫЕ КЛЮЧИ:")
print(f"C2_BLACKLIST_API_KEY: {C2_BLACKLIST_API_KEY[:10] if C2_BLACKLIST_API_KEY != 'КЛЮЧ НЕ НАЙДЕН' else 'КЛЮЧ НЕ НАЙДЕН'}...")
print(f"THREAT_INTELLIGENCE_KEY: {THREAT_INTELLIGENCE_KEY[:10] if THREAT_INTELLIGENCE_KEY != 'КЛЮЧ НЕ НАЙДЕН' else 'КЛЮЧ НЕ НАЙДЕН'}...")
print(f"MONITORING_TOKEN: {MONITORING_TOKEN[:10] if MONITORING_TOKEN != 'КЛЮЧ НЕ НАЙДЕН' else 'КЛЮЧ НЕ НАЙДЕН'}...")

# 2. ИСХОДНЫЕ ДАННЫЕ 

# Список IP-адресов (10 разных адресов)
ip_addresses = [
    "185.130.5.253",   # C&C сервер
    "8.8.8.8",         # DNS Google (безопасный)
    "94.23.15.12",     # C&C сервер
    "1.1.1.1",         # DNS Cloudflare (безопасный)
    "193.42.4.1",      # C&C сервер
    "176.9.75.45",     # C&C сервер
    "8.8.4.4",         # DNS Google (безопасный)
    "89.45.87.12",     # C&C сервер
    "5.188.86.45",     # C&C сервер
    "208.67.222.222"   # DNS OpenDNS (безопасный)
]

# ЧЁРНЫЙ СПИСОК C&C серверов
if C2_BLACKLIST_API_KEY != "КЛЮЧ НЕ НАЙДЕН":
    C2_SERVERS = ["185.130.5.253", "94.23.15.12", "193.42.4.1", 
                  "176.9.75.45", "89.45.87.12", "5.188.86.45",
                  "45.155.205.233", "103.25.14.78"]  
    print("\n[+] Используется расширенный список C&C серверов (API ключ активен)")
else:
    C2_SERVERS = ["185.130.5.253", "94.23.15.12", "193.42.4.1"]
    print("\n[-] Используется базовый список C&C серверов")

n = len(ip_addresses)

# ФАКТОРЫ РИСКА
connections_count = [250, 45, 180, 30, 500, 15, 75, 320, 150, 60]   #количество соединений
suspicious_port =   [1,   0,  1,   0,  1,   0,  0,  1,   1,   0]    #подозрительные порты
unknown_process =   [1,   0,  1,   0,  1,   0,  0,  1,   0,   0]    #подозрительные процессы
high_traffic =      [1,   0,  0,   0,  1,   0,  1,  1,   1,   0]    #высокий трафик
night_activity =    [1,   1,  0,   1,  1,   0,  1,  0,   1,   1]    #ночная активность


# 3. ОПРЕДЕЛЕНИЕ C&C СЕРВЕРОВ

c2_server = []
for i in range(n):
    if ip_addresses[i] in C2_SERVERS:
        c2_server.append(1)
        if THREAT_INTELLIGENCE_KEY != "КЛЮЧ НЕ НАЙДЕН":
            print(f"   [!] IP {ip_addresses[i]} обнаружен в базе C&C серверов")
    else:
        c2_server.append(0)


# 4. РАСЧЁТ УГРОЗЫ

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

# 5. ТАБЛИЦА РЕЗУЛЬТАТОВ

data = list(zip(range(1, n+1), ip_addresses, connections_count, 
                suspicious_port, unknown_process, high_traffic, 
                c2_server, night_activity, threat_level, decision))

df = pd.DataFrame(data, columns=[
    "ID", "IP адрес", "Соединений", "Подозр. порт",
    "Подозр. процесс", "Высокий трафик", "C&C сервер",
    "Ночная активность", "Уровень угрозы", "Решение"
])

print("\n" + "-"*140)
print("РЕЗУЛЬТАТЫ АНАЛИЗА СЕТЕВОЙ АКТИВНОСТИ")
print("Защита от скрытного включения в бот-сеть (Вариант 12)")
print(df.to_string(index=False))
print("\n" + "-"*140)
print("СТАТИСТИКА РЕШЕНИЙ:")
stats = df["Решение"].value_counts()
print(f"   ALLOW (разрешено):  {stats.get('ALLOW', 0)} соединений")
print(f"   BLOCK (заблокировано): {stats.get('BLOCK', 0)} соединений")

# 6. ОТПРАВКА МЕТРИК 

if MONITORING_TOKEN != "КЛЮЧ НЕ НАЙДЕН":
    blocked_count = len(df[df["Решение"] == "BLOCK"])
    allowed_count = len(df[df["Решение"] == "ALLOW"])
    print(f"\n[+] Отправка метрик в Prometheus (токен: {MONITORING_TOKEN[:8]}...):")
    print(f"   - bot_activity_blocked_total: {blocked_count}")
    print(f"   - bot_activity_allowed_total: {allowed_count}")
    print(f"   - threat_level_max: {max(threat_level)}")
    print(f"   - threat_level_avg: {sum(threat_level)/len(threat_level):.1f}")
else:
    print("\n[-] MONITORING_TOKEN отсутствует, метрики не отправлены")


# 7. ВИЗУАЛИЗАЦИЯ

plt.style.use('ggplot')

# График 1: Количество соединений
plt.figure(figsize=(14, 6))
colors_line = ['red' if c2_server[i]==1 else 'blue' for i in range(n)]
plt.bar(ip_addresses, connections_count, color=colors_line, alpha=0.7)
plt.title("Количество сетевых соединений по IP-адресам (красный = C&C сервер)", fontsize=14)
plt.xlabel("IP-адрес", fontsize=12)
plt.ylabel("Количество соединений", fontsize=12)
plt.xticks(rotation=45, ha="right")
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig("chart_connections.png")
plt.close()

# График 2: Уровень угрозы
plt.figure(figsize=(14, 6))
plt.bar(ip_addresses, threat_level, color='orange', edgecolor='black')
plt.title("Уровень угрозы по IP-адресам", fontsize=14)
plt.xlabel("IP-адрес", fontsize=12)
plt.ylabel("Уровень угрозы (баллы)", fontsize=12)
plt.xticks(rotation=45, ha="right")
plt.axhline(y=3, color='red', linestyle='--', label='Порог блокировки (3 балла)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig("chart_threat.png")
plt.close()

# График 3: Круговая диаграмма решений
plt.figure(figsize=(8, 8))
decision_counts = df["Решение"].value_counts()
labels = ["Разрешить (ALLOW)", "Заблокировать (BLOCK)"]
sizes = [decision_counts.get("ALLOW", 0), decision_counts.get("BLOCK", 0)]
colors_pie = ['#66b3ff', '#ff6666']
explode = (0.05, 0.1)
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90,
        shadow=True, explode=explode, colors=colors_pie)
plt.title("Распределение решений контейнера безопасности", fontsize=14)
plt.savefig("chart_pie.png")
plt.close()

# График 4: Факторы риска (суммарно)
plt.figure(figsize=(10, 6))
risk_factors = df[["Подозр. порт", "Подозр. процесс", "Высокий трафик", 
                   "C&C сервер", "Ночная активность"]].sum()
risk_factors.plot(kind='bar', color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'])
plt.title("Суммарные срабатывания факторов риска", fontsize=14)
plt.ylabel("Количество случаев (из 10 IP)", fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.5)
for i, v in enumerate(risk_factors):
    plt.text(i, v + 0.5, str(v), ha='center', fontsize=10)
plt.tight_layout()
plt.savefig("chart_risk_factors.png")
plt.close()

print("\n" + "-"*40)
print("СОЗДАННЫЕ ГРАФИКИ:")
print("  - chart_connections.png")
print("  - chart_threat.png")
print("  - chart_pie.png")
print("  - chart_risk_factors.png")
print("\nРАБОТА КОНТЕЙНЕРОВ ЗАВЕРШЕНА")