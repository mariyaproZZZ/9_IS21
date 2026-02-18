import random
import string

def generate_password(length=12):
    """Генерирует пароль заданной длины."""
    if length < 4:
        print("Рекомендуемая длина пароля - не менее 4 символов.")
        length = 4
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

if __name__ == "__main__":
    pwd = generate_password(10)
    print(f"Сгенерированный пароль: {pwd}")