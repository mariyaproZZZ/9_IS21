import string

def check_password_strength(password):
    """Оценивает сложность пароля."""
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

if __name__ == "__main__":
    test_pwd = "ExamplePwd123!"
    strength = check_password_strength(test_pwd)
    print(f"Пароль '{test_pwd}' - {strength}")