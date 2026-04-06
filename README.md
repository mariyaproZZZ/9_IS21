# 🔐 Генератор и оценщик паролей (Вариант 9)

Программный комплекс для создания надежных паролей, анализа их стойкости и безопасного шифрования данных.

---

## 👥 Состав команды

| Роль | Разработчик | Модуль |
| :--- | :--- | :--- |
| **Backend / Logic** | Костылева Екатерина | Модуль B (Оценка сложности) |
| **Backend / Security** | Зозуля Мария | Модули A и C (Генерация и Шифрование) |

---

## 🛠 Описание модулей

* **Модуль A** (`9_modul_a.py`): Генератор случайных паролей с настраиваемыми параметрами длины и символов.
* **Модуль B** (`9_modul_b.py`): Анализатор сложности, проверяющий пароль на длину, наличие цифр, регистр и спецсимволы.
* **Модуль C** (`9_modul_c.py`): Система шифрования (AES/Fernet) и безопасного сохранения паролей в файл.

---

## 🚀 Инструкция по запуску

### 1. Клонирование репозитория
```bash
git clone [https://github.com/mariyaproZZZ/9_IS21.git](https://github.com/mariyaproZZZ/9_IS21.git)
cd 9_IS21

2. Запуск модулей
Вы можете запустить каждый компонент отдельно в зависимости от задачи:

Bash
python 9_modul_a.py   # Генерация пароля
python 9_modul_b.py   # Проверка сложности
python 9_modul_c.py   # Шифрование и сохранение
🧪 Разработка и качество кода
Установка зависимостей
Для разработки и тестирования необходимо установить дополнительные пакеты:

Bash
pip install pytest flake8 black
Инструменты контроля
Форматирование (Black): Приводит код к единому стандарту.

Bash
black 9_modul_a.py 9_modul_b.py 9_modul_c.py
Linter (Flake8): Проверяет код на наличие стилистических ошибок.

Bash
flake8 9_modul_a.py 9_modul_b.py 9_modul_c.py
Тестирование
Запуск всех Unit-тестов для проверки корректности работы функций:

Bash
pytest tests/ -v
📊 Результаты тестов
Последняя сборка успешно прошла все проверки:

Plaintext
tests/test_password_modules.py::test_generate_password_default_length PASSED [ 14%]
tests/test_password_modules.py::test_generate_password_custom_length  PASSED [ 28%]
tests/test_password_modules.py::test_generate_password_too_short      PASSED [ 42%]
tests/test_password_modules.py::test_check_strength_weak              PASSED [ 57%]
tests/test_password_modules.py::test_check_strength_medium            PASSED [ 71%]
tests/test_password_modules.py::test_check_strength_strong            PASSED [ 85%]
tests/test_password_modules.py::test_encrypt_decrypt                  PASSED [100%]

✅ 7 passed in 0.03s
