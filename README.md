# Генератор и оценщик паролей (Вариант 9)

## Состав команды
- Костылева Екатерина (модуль B)
- Зозуля Мария (модули A и C)

## Описание
Проект состоит из трёх модулей:
- **Модуль A** (`9_modul_a.py`): генератор случайных паролей
- **Модуль B** (`9_modul_b.py`): оценка сложности паролей
- **Модуль C** (`9_modul_c.py`): шифрование и сохранение паролей

## Инструкция по запуску
1. Клонировать репозиторий:

   git clone https://github.com/mariyaproZZZ/9_IS21.git
   
Запустить нужный модуль:
python 9_modul_a.py   # генерация пароля
python 9_modul_b.py   # проверка сложности
python 9_modul_c.py   # сохранение пароля

Разработка. Установка зависимостей
pip install pytest flake8 black

Запуск тестов
py -m pytest tests/ -v

Проверка стиля кода (flake8)
py -m flake8 9_modul_a.py 9_modul_b.py 9_modul_c.py

Форматирование кода (black)
py -m black 9_modul_a.py 9_modul_b.py 9_modul_c.py

Результаты тестов
tests/test_password_modules.py::test_generate_password_default_length PASSED
tests/test_password_modules.py::test_generate_password_custom_length PASSED
tests/test_password_modules.py::test_generate_password_too_short PASSED
tests/test_password_modules.py::test_check_strength_weak PASSED
tests/test_password_modules.py::test_check_strength_medium PASSED
tests/test_password_modules.py::test_check_strength_strong PASSED
tests/test_password_modules.py::test_encrypt_decrypt PASSED

7 passed in 0.03s
