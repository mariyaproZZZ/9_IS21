import string

def check_password_strength(password):
    """Оценивает сложность пароля по шкале Слабый/Средний/Сильный."""
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)
    length = len(password)

    score = 0
    if length >= 8:
        score += 1
    if has_upper and has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_special:
        score += 1

    if score <= 1:
        return "Слабый"
    elif score == 2:
        return "Средний"
    else:
        return "Сильный"

def test_password(password):
    """Тестирует один пароль и выводит результат."""
    strength = check_password_strength(password)
    print(f"Пароль '{password}' -> {strength} (оценка: {strength})")

if __name__ == "__main__":
    print("=== ТЕСТИРОВАНИЕ ОЦЕНЩИКА ПАРОЛЕЙ ===\n")
    
    # Тестовые пароли разной сложности
    test_passwords = [
        "123",              # Слабый (короткий, только цифры)
        "qwerty",           # Слабый (только строчные)
        "QWERTY",           # Слабый (только заглавные)
        "Qwerty123",        # Средний (есть буквы+цифры, нет спецсимволов)
        "Qwerty!",          # Средний (буквы+спецсимвол, короткий)
        "Qwerty123!",       # Сильный (всё есть, длина 9)
        "P@ssw0rd",         # Сильный (всё есть, длина 8)
        "SuperStrongP@ssw0rd123"  # Сильный (длинный, всё есть)
    ]
    
    for pwd in test_passwords:
        test_password(pwd)
    
    print("\n=== Пример использования ===")
    user_pwd = input("Введите пароль для проверки: ")
    result = check_password_strength(user_pwd)
    print(f"Сложность вашего пароля: {result}")