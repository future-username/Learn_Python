## Простая регистрация пользователя (без БД и API)

```python
def normalize_login(login: str) -> str:
    return login.strip().lower()


def check_password(password: str) -> bool:
    return len(password) >= 6


def main() -> None:
    login = input("Логин: ")
    password = input("Пароль: ")
    confirm = input("Подтверждение пароля: ")

    login = normalize_login(login)

    if not login:
        print("Логин пуст")
        return

    if not check_password(password):
        print("Пароль слишком короткий")
        return

    if password != confirm:
        print("Пароли не совпадают")
        return

    print("Вход успешный")


if __name__ == "__main__":
    main()
```

```mermaid
sequenceDiagram
    actor User
    participant Main
    participant Normalize as "normalize_login(login)"
    participant Check as "check_password(password)"

    User ->> Main: ввод login, password, confirm
    Main ->> Normalize: нормализация логина
    Normalize -->> Main: login

    alt login пуст
        Main -->> User: "Логин пуст"
        Main -->> Main: выход
    else login есть
        Main -->> Main: продолжить
    end

    Main ->> Check: проверка пароля
    Check -->> Main: bool

    alt пароль некорректный
        Main -->> User: "Пароль слишком короткий"
        Main -->> Main: выход
    else пароль корректный
        Main -->> Main: продолжить
    end

    alt password != confirm
        Main -->> User: "Пароли не совпадают"
        Main -->> Main: выход
    else пароли совпадают
        Main -->> User: "Вход успешный"
    end
```
