import re

from prettytable import PrettyTable

PATTERN = re.compile(r'\d+')


def read_from_file(filename: str) -> list[str]:
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            lines = [line.rstrip('\n') for line in lines]
            return lines
    except FileNotFoundError:
        print(f"Запрашиваемый файл {filename} не найден")
        return []


def write_to_file(filename: str) -> None:
    record = create_record()
    with open(filename, 'a', encoding='utf-8') as file:
        file.writelines(' '.join(record) + '\n')
        print('Данные записаны')


def create_record() -> tuple[str]:
    surname = input('Введите фамилию: ')
    name = input('Введите имя: ')
    patronymic = input('Введите отчество: ')
    while True:
        try:
            phone_number = input('Введите номер телефона: ')
            if PATTERN.match(phone_number):
                return (surname, name, patronymic, phone_number)
            else:
                raise ValueError
        except ValueError:
            print('Ошибка ввода. Попробуйте еще раз')


def print_records(records: list[str]) -> None:
    mytable = PrettyTable()
    mytable.field_names = ['№ п/п', 'Фамилия',
                           'Имя', 'Отчество', 'Номер телефона']
    mytable.align = 'l'
    counter = 1
    for record in records:
        record = record.split()
        record.insert(0, counter)
        mytable.add_row(record)
        counter += 1
    print(mytable)


def search_record(msg: str, index: int, filename: str) -> list[str]:
    obj = input(msg)
    records = read_from_file(filename)
    result = []
    for record in records:
        contact = record.split()
        if contact[index] == obj:
            result.append(record)
    return result


def print_results(result: list[str]) -> None:
    if not result:
        print('Результаты не найдены')
    else:
        print_records(result)


def delete_record(filename: str):
    surname = input('Введите фамилию: ')
    pattern = re.compile(re.escape(surname))
    with open(filename, 'r+', encoding='utf-8') as file:
        records = file.readlines()
        print(records)
        file.seek(0)
        for record in records:
            result = pattern.search(record)
            if result is None:
                file.write(record)
            else:
                print('Запись удалена')
            file.truncate()


def find_actions(filename: str) -> None:
    print('Выберите критерии поиска: ')
    print('1 - поиск по фамилии')
    print('2 - поиск по имени')
    print('3 - поиск по номеру телефона')
    print('0 - возвращение в главное меню')
    print()
    while True:
        cmd = input('Введите вариант поиска >>> ')
        if cmd == '1':
            result = search_record('введите фамилию: ', int(cmd)-1, filename)
            print_results(result)
        elif cmd == '2':
            result = search_record('введите имя: ', int(cmd)-1, filename)
            print_results(result)
        elif cmd == '3':
            result = search_record(
                'введите номер телефона: ', int(cmd), filename)
            print_results(result)
        elif cmd == '0':
            print('Вы вернулись в главное меню >>>')
            return
        else:
            print("Вы ввели не правильное значение")
