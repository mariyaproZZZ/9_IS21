[![Python CI](https://github.com/mariyaproZZZ/9_IS21/actions/workflows/ci.yml/badge.svg)](https://github.com/mariyaproZZZ/9_IS21/actions/workflows/ci.yml)
# 🔐 Генератор и оценщик паролей (Вариант 9)

Программный комплекс для генерации надежных паролей, анализа их стойкости и безопасного шифрования.

---

## 👥 Состав команды

| Роль | Разработчик | Модуль |
| :--- | :--- | :--- |
| **Backend / Logic** | Костылева Екатерина | Модуль B (Оценка сложности) |
| **Backend / Security** | Зозуля Мария | Модули A и C (Генерация и Шифрование) |

---

## 🛠 Описание модулей

* **Модуль A** (`9_modul_a.py`): Генератор случайных паролей с настройкой длины.
* **Модуль B** (`9_modul_b.py`): Анализатор сложности (проверка на символы, регистр и длину).
* **Модуль C** (`9_modul_c.py`): Шифрование и запись паролей в защищенное хранилище.

---

## 🚀 Инструкция по запуску

### 1. Клонирование репозитория
git clone [https://github.com/mariyaproZZZ/9_IS21.git](https://github.com/mariyaproZZZ/9_IS21.git)

cd 9_IS21

---


## 2. Запуск компонентов

* python 9_modul_a.py   # Генерация
* python 9_modul_b.py   # Проверка сложности
* python 9_modul_c.py   # Сохранение

---

## 🧪 Разработка и тесты
Установка окружения

* pip install pytest flake8 black
---

## Качество кода и форматирование
Black (автоформатирование):

* black 9_modul_a.py 9_modul_b.py 9_modul_c.py

---

## Flake8 (проверка стиля):

* flake8 9_modul_a.py 9_modul_b.py 9_modul_c.py

---

## Запуск Unit-тестов

* pytest tests/ -v

---

## 📊 Статус тестов
Все модули успешно прошли проверку:

tests/test_password_modules.py::test_generate_password_default_length PASSED
tests/test_password_modules.py::test_generate_password_custom_length  PASSED
tests/test_password_modules.py::test_generate_password_too_short      PASSED
tests/test_password_modules.py::test_check_strength_weak              PASSED
tests/test_password_modules.py::test_check_strength_medium            PASSED
tests/test_password_modules.py::test_check_strength_strong            PASSED
tests/test_password_modules.py::test_encrypt_decrypt                  PASSED

✅ 7 passed in 0.03s
