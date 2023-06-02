def show_data() -> None:
    """Выводит информацию из справочника"""
    with open ('D:\\Учебная\\Знакомство с Python\\Python_Homework_8\\book.txt', 'r', encoding = 'utf-8') as book:
        print(book.read())


def add_data() -> None:
    """Добавляет информацию в справочник."""
    fio = input('Введите ФИО: ')
    phone_number = input('Введите номер телефона: ')
    with open('D:\\Учебная\\Знакомство с Python\\Python_Homework_8\\book.txt', 'a', encoding = 'utf-8') as book:
        book.write(f'\n{fio} | {phone_number}')


def find_data() -> None:
    """Печатает результат поиска по справочнику."""
    with open('D:\\Учебная\\Знакомство с Python\\Python_Homework_8\\book.txt', 'r', encoding = 'utf-8') as file:
        data = file.read().split('\n')
    print('\n' .join(data))
    contact_to_find = input('Что хотите найти: ')
    print(search(data, contact_to_find))


def search(book: list[str], info: str) -> list[str] | str:
    """Находит в списке записи по определенному критерию поиска"""
    result = [contact for contact in book if info in contact]
    if not result:
        return 'Ничего не нашёл'    
    elif len(result) == 1:
        return result[0]
    elif len(result) > 1:
        print()
        print('\n' .join(result))
        correct_info = input('Введите данные для уточнения контакта: ')
        return search(result, correct_info)    

def change_data() -> None:
    """Изменение или удаление записей в списке"""     
    with open('D:\\Учебная\\Знакомство с Python\\Python_Homework_8\\book.txt', 'r', encoding = 'utf-8') as file:
        data = file.read().split('\n')
        print('\n' .join(data))
        data_to_search = input('Кого будем менять или удалять: ')
        data_to_search = search(data, data_to_search)
        print(f'Вы выбрали: {data_to_search}')
        mode = input('Удалить - 1, Изменить - 2')
        if mode == '1':
            data.remove(data_to_search)
        elif mode == '2':
            data[data.index(data_to_search)] = choice_contact()
        with open('D:\\Учебная\\Знакомство с Python\\Python_Homework_8\\book.txt', 'w', encoding = 'utf-8') as file:
            file.write('\n' .join(data))

def choice_contact() -> str:
    fio = input('Введите ФИО: ')
    phone_number = input('Введите номер телефона: ')
    return f'{fio} | {phone_number}'