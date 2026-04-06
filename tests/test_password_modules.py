import pytest
import sys
import os

# Добавляем родительскую папку в путь
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import importlib

module_a = importlib.import_module("9_modul_a")
module_b = importlib.import_module("9_modul_b")
module_c = importlib.import_module("9_modul_c")


# Тесты для модуля A
def test_generate_password_default_length():
    pwd = module_a.generate_password()
    assert len(pwd) == 12


def test_generate_password_custom_length():
    pwd = module_a.generate_password(20)
    assert len(pwd) == 20


def test_generate_password_too_short():
    pwd = module_a.generate_password(2)
    assert len(pwd) == 4


# Тесты для модуля B
def test_check_strength_weak():
    assert module_b.check_password_strength("123") == "Слабый"
    assert module_b.check_password_strength("qwerty") == "Слабый"


def test_check_strength_medium():
    """Проверка: средний пароль (ровно 2 балла)"""
    # Короткий пароль: разный регистр + спецсимвол
    assert module_b.check_password_strength("Ab!") == "Средний"
    # Короткий пароль: разный регистр + цифры
    assert module_b.check_password_strength("Ab1") == "Средний"
    # Длинный пароль: только строчные буквы + цифры
    assert module_b.check_password_strength("qwerty123") == "Средний"
    # Длинный пароль: только заглавные буквы + цифры
    assert module_b.check_password_strength("QWERTY123") == "Средний"


def test_check_strength_strong():
    assert module_b.check_password_strength("Qwerty123!") == "Сильный"
    assert module_b.check_password_strength("P@ssw0rd") == "Сильный"


# Тесты для модуля C
def test_encrypt_decrypt():
    original = "MySecret"
    encrypted = module_c.simple_encrypt(original)
    decrypted = module_c.simple_decrypt(encrypted)
    assert decrypted == original