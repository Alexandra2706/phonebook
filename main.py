import os

from utils import delete_record, find_actions, patch_record, print_records, read_from_file, write_to_file

LOCAL_FILENAME = '\\tables\phone.txt'
LOCAL_PATH = os.path.dirname(os.path.abspath(__file__)) + LOCAL_FILENAME


def actions(filename: str) -> None:
    print('Выбереите действие: ')
    print('1 - вывести список абонентов')
    print('2 - добавить абонента в телефонный справочник')
    print('3 - изменить данные абонента')
    print('4 - найти абонента')
    print('5 - удалить данные абонента')
    print('0 - выход из программы')
    print()
    while True:
        cmd = input('Введите пункт меню >>> ')
        if cmd == '1':
            data = read_from_file(filename)
            print_records(data)
        elif cmd == '2':
            write_to_file(filename)
        elif cmd == '3':
            patch_record(filename)
        elif cmd == '4':
            find_actions(filename)
        elif cmd == '5':
            delete_record(filename)
        elif cmd == '0':
            exit(0)
        else:
            print("Вы ввели не правильное значение")


if __name__ == '__main__':
    filename = LOCAL_PATH
    actions(filename)
