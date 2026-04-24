import unittest
import pandas as pd
import os
import main   # импортируем наш модуль

class TestBotContainer(unittest.TestCase):
    def setUp(self):
        # Этот метод выполняется перед каждым тестом
        # Вызываем calculate() один раз, чтобы получить таблицу и статистику
        self.df, self.stats = main.calculate()

    def test_df_not_empty(self):
        # Проверяем, что DataFrame не пустой
        self.assertFalse(self.df.empty, "DataFrame не должен быть пустым")

    def test_df_shape(self):
        # Проверяем размерность: 10 строк, 10 колонок
        self.assertEqual(self.df.shape, (10, 10), "Должно быть 10 строк и 10 колонок")

    def test_columns_exist(self):
        # Проверяем наличие обязательных колонок
        required_columns = ["ID", "IP адрес", "Соединений", "Подозр. порт",
                            "Подозр. процесс", "Высокий трафик", "C&C сервер",
                            "Ночная активность", "Уровень угрозы", "Решение"]
        for col in required_columns:
            self.assertIn(col, self.df.columns, f"Отсутствует колонка {col}")

    def test_statistics(self):
        # Проверяем, что статистика корректна (6 BLOCK, 4 ALLOW)
        self.assertEqual(self.stats["BLOCK"], 6, "Должно быть 6 блокировок")
        self.assertEqual(self.stats["ALLOW"], 4, "Должно быть 4 разрешения")

    def test_threshold_logic(self):
        # Проверяем, что для каждой строки решение соответствует уровню угрозы
        for idx, row in self.df.iterrows():
            threat = row["Уровень угрозы"]
            decision = row["Решение"]
            if threat >= 3:
                self.assertEqual(decision, "BLOCK", f"Строка {idx}: угроза {threat} должна быть BLOCK")
            else:
                self.assertEqual(decision, "ALLOW", f"Строка {idx}: угроза {threat} должна быть ALLOW")

    def test_c2_server_marking(self):
        # Проверяем, что IP из чёрного списка отмечены как C&C сервер (значение 1)
        # Базовые C&C: 185.130.5.253, 94.23.15.12, 193.42.4.1, 176.9.75.45, 89.45.87.12, 5.188.86.45
        c2_ips = ["185.130.5.253", "94.23.15.12", "193.42.4.1", "176.9.75.45", "89.45.87.12", "5.188.86.45"]
        for ip in c2_ips:
            row = self.df[self.df["IP адрес"] == ip]
            self.assertEqual(row["C&C сервер"].iloc[0], 1, f"IP {ip} должен быть помечен как C&C сервер")

    def test_safe_ips_not_marked(self):
        # Проверяем, что безопасные IP не отмечены как C&C (значение 0)
        safe_ips = ["8.8.8.8", "1.1.1.1", "8.8.4.4", "208.67.222.222"]
        for ip in safe_ips:
            row = self.df[self.df["IP адрес"] == ip]
            self.assertEqual(row["C&C сервер"].iloc[0], 0, f"IP {ip} не должен быть помечен как C&C сервер")

    def test_connections_list_length(self):
        # Проверяем, что все списки имеют длину 10 (целостность данных)
        self.assertEqual(len(main.ip_addresses), 10)
        self.assertEqual(len(main.connections_count), 10)
        self.assertEqual(len(main.suspicious_port), 10)
        self.assertEqual(len(main.unknown_process), 10)
        self.assertEqual(len(main.high_traffic), 10)
        self.assertEqual(len(main.night_activity), 10)

    def test_visualization_files_created(self):
        # Вызываем visualize и проверяем, что создаются 4 PNG-файла
        main.visualize(self.df)
        files = ["chart_connections.png", "chart_threat.png", "chart_pie.png", "chart_risk_factors.png"]
        for f in files:
            self.assertTrue(os.path.exists(f), f"Файл {f} не создан")
        # Очистка (опционально): удалить файлы, чтобы не засорять репозиторий
        for f in files:
            if os.path.exists(f):
                os.remove(f)

    def test_empty_ip_list_handling(self):
        # Сохраняем исходный список IP, временно заменяем на пустой
        original_ips = main.ip_addresses.copy()
        try:
            main.ip_addresses.clear()
            df_empty, stats_empty = main.calculate()
            self.assertTrue(df_empty.empty, "При пустом списке IP DataFrame должен быть пустым")
            self.assertEqual(stats_empty["ALLOW"], 0, "При пустом списке ALLOW должно быть 0")
            self.assertEqual(stats_empty["BLOCK"], 0, "При пустом списке BLOCK должно быть 0")
        finally:
            # Восстанавливаем исходный список IP
            main.ip_addresses.clear()
            main.ip_addresses.extend(original_ips)

if __name__ == "__main__":
    unittest.main()