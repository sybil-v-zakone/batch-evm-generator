# Batch EVM Generator
Скрипт генерирует evm-кошельки в заданном количестве и экспортирует их в Excel.


#### Установка зависимостей для Windows:

1. `cd путь\к\проекту`.
2. `python -m venv venv`.
3. `.\venv\Scripts\activate`.
4. `pip install -r requirements.txt`.

#### Установка зависимостей для MacOS / Linux:

Выполняем данные команды в терминале:

1. `cd путь/к/проекту`.
2. `python3 -m venv venv`.
3. MacOS/Linux `source venv/bin/activate`.
4. `pip install -r requirements.txt`.

#### Настройка:
Все настройки софта находятся в файле `config.py`:
- ``WALLET_COUNT`` – количество кошельков для генерации
- ``WALLETS_EXPORT_PATH`` – путь для экспорта в Excel

#### *Запуск:*
Пишем в консоли `python main.py` на Windows или `python3 main.py` на MacOS / Linux