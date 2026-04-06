def simple_encrypt(text):
    """Примитивное 'шифрование' (переворот строки)."""
    return text[::-1]


def simple_decrypt(encrypted_text):
    """Расшифровка (обратный переворот)."""
    return encrypted_text[::-1]


def save_password_to_file(password, filename="passwords.txt"):
    """Сохраняет зашифрованный пароль в файл."""
    encrypted_pwd = simple_encrypt(password)
    try:
        with open(filename, "a", encoding="utf-8") as f:
            f.write(encrypted_pwd + "\n")
        print(f"Пароль (в зашифрованном виде) добавлен в файл {filename}")
    except Exception as e:
        print(f"Ошибка при записи в файл: {e}")


if __name__ == "__main__":
    test_pwd = "MySecretPass"
    save_password_to_file(test_pwd)
