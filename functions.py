def show_data() -> None:
    """Выводит информацию из справочника"""
    with open ('D:\\Учебная\\Знакомство с Python\\sem_8_practice\\book.txt', 'r', encoding = 'utf-8') as book:
        print(book.read())


def add_data() -> None:
    """Добавляет информацию в справочник."""
    fio = input('Введите ФИО: ')
    phone_number = input('Введите номер телефона: ')
    with open('D:\\Учебная\\Знакомство с Python\\sem_8_practice\\book.txt', 'a', encoding = 'utf-8') as book:
        book.write(f'\n{fio} | {phone_number}')


def find_data() -> None:
    """Печатает результат поиска по справочнику."""
    with open('D:\\Учебная\\Знакомство с Python\\sem_8_practice\\book.txt', 'r', encoding = 'utf-8') as file:
        data = file.read()
    contact_to_find = input('Что хотите найти: ')
    result = search(data, contact_to_find)
    print(result)


def search(book: str, info: str) -> list[str]:
    """Находит в списке записи по определенному критерию поиска"""
    book = book.split('\n')
    return list(filter(lambda contact: info.lower() in contact.lower(), book))                  
