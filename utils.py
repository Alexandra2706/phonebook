import re
import os

from prettytable import PrettyTable

LOCAL_PATH = os.path.dirname(os.path.abspath(__file__))
PATTERN = re.compile(r'\d+')
PATTERN_FILENAME = re.compile(r'\w+')


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


def get_records(filename: str) -> None:
    data = read_from_file(filename)
    print_records(data)


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


def delete_record(filename: str) -> None:
    surname = input('Введите фамилию: ')
    pattern = re.compile(re.escape(surname))
    with open(filename, 'r+', encoding='utf-8') as file:
        records = file.readlines()
        file.seek(0)
        for record in records:
            result = pattern.search(record)
            if result is None:
                file.write(record)
            else:
                print(record.rstrip('\n'))
                answer = input('Удалить запись (y/n)? ')
                print('Запись удалена') if answer == 'y' else file.write(record)
            file.truncate()


def get_number_record(msg: str) -> int:
    while True:
        try:
            record_number = int(input(msg))
            return record_number
        except ValueError:
            print('Ошибка ввода. Попробуйте еще раз')


def get_filename(msg: str) -> str:
    filename = input(msg)
    while True:
        try:
            if PATTERN_FILENAME.match(filename):
                return filename + '.txt'
            else:
                raise ValueError
        except ValueError:
            print('Ошибка ввода. Попробуйте еще раз')


def patch_record(filename: str) -> None:
    records = read_from_file(filename)
    print_records(records)
    index = get_number_record('Введите номер редактируемой записи: ')
    old_record = records[index-1]
    new_record = ' '.join(create_record()) + '\n'
    with open(filename, 'r', encoding='utf-8') as file:
        lines = [new_record if line.rstrip(
        ) == old_record else line for line in file]
    with open(filename, 'w', encoding='utf-8') as file:
        file.writelines(lines)
    print('запись изменена')


def copy_record(filename: str) -> None:
    records = read_from_file(filename)
    print_records(records)
    index = get_number_record('Введите номер копируемой записи: ')
    print(records[index-1])
    new_filename = LOCAL_PATH + '\\tables\\' + \
        get_filename('Введите имя файла без расширения: ')
    with open(new_filename, 'w', encoding='utf-8') as file:
        file.writelines(records[index-1] + '\n')
    print('запись скопирована')


def find_actions(filename: str) -> None:
    print('Rритерии поиска: \n'
          '1 - поиск по фамилии \n'
          '2 - поиск по имени \n'
          '3 - поиск по номеру телефона \n'
          '0 - возвращение в главное меню \n'
          )
    while True:
        cmd = input('Выберите критерии поиска / выход - 0 >>> ')
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
