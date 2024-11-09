from playwright.sync_api import Page, expect
import data
import pytest


@pytest.mark.parametrize("username", ["в", ".", "#"])
def test_username1(page: Page, username):
    page.goto(data.URL)
    page.type('input[type="text"]', username)
    expect(page.get_by_text(f'Введены недопустимые символы: {username}')).to_be_visible()


def test_username2(page: Page):
    page.goto(data.URL)
    page.type('input[type="text"]', "nvjfhydkvbfytrdhfnchydrtgfbnchyfrdtgb")
    expect(page.get_by_text(f'Превышен лимит символов: 32 максимум')).to_be_visible()


@pytest.mark.parametrize("username", ["rimus", "2ghhjhl"])
def test_username3(page: Page, username):
    page.goto(data.URL)
    page.type('input[type="text"]', username)
    page.press('button[type="submit"]', 'Enter')
    expect(page.get_by_text(
        f'Допустимые символы (от 6 до 32): a-z, 0-9, _. Имя должно начинаться с буквы')).to_be_visible()


# def test_username_(page: Page):
#     page.goto(data.URL)
#     username = ''
#     page.type('input[type="text"]', username)
#     page.press('button[type="submit"]', 'Enter')
#     expect(page.get_by_text(f'Поле не заполнено')).to_be_visible()


@pytest.mark.parametrize("email", ["f", "а", "4", "*", "@mail.ru"])
def test_email(page: Page, email):
    page.goto(data.URL)
    page.type('input[name="username"]', email)
    page.press('button[type="submit"]', 'Enter')
    expect(page.get_by_text(f'Формат e-mail: username@test.ru')).to_be_visible()


# def test_email_(page: Page):
#     page.goto(data.URL)
#     email = ''
#     page.type('input[name="username"]', email)
#     page.press('button[type="submit"]', 'Enter')
#     expect(page.get_by_text(f'Поле не заполнено')).to_be_visible()

@pytest.mark.parametrize("password", ["1", "а", "4111234", "*", "mailru"])
def test_password_short(page: Page, password):
    page.goto(data.URL)
    page.type('input[name="new-password"]', password)
    expect(page.get_by_text(f'Сложность пароля: слишком короткий')).to_be_visible()


@pytest.mark.parametrize("password",
                         ["12345678", "а12345678", "12345678*", "А12345678", "mailru12345678", "А_а12345678"])
def test_password_s(page: Page, password):
    page.goto(data.URL)
    page.type('input[name="new-password"]', password)
    expect(page.get_by_text(f'Сложность пароля: низкая')).to_be_visible()


# @pytest.mark.parametrize("code",
#                          ["1", "а", "*", "А", "_", ","])
# def test_code(page: Page, code):
#     page.goto(data.URL)
#     page.type('input[id="input-173"]', code)
#     expect(page.get_by_text(f'Неверный формат ссылки')).to_be_visible()

