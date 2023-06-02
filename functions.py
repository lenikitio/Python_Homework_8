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


def search(book: str, info: str) -> list[str] | str:
    """Находит в списке записи по определенному критерию поиска"""
    result = [contact for contact in book if info.lower() in contact.lower()]
    if not result:
        return 'Ничего не нашёл'    
    elif len(result) == 1:
        return result[0]
    elif len(result) > 1:
        print()
        print('\n' .join(result))
        correct_info = input('Введите данные для уточнения контакта: ')
        return search(result, correct_info)              
