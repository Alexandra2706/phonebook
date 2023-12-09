import os

from utils import copy_record, delete_record, get_records, find_actions, patch_record, write_to_file

LOCAL_FILENAME = '\\tables\phone.txt'
LOCAL_PATH = os.path.dirname(os.path.abspath(__file__)) + LOCAL_FILENAME


def actions(filename: str) -> None:
    print('Выбереите действие: ')
    print('1 - вывести список абонентов')
    print('2 - добавить абонента в телефонный справочник')
    print('3 - изменить данные абонента')
    print('4 - найти абонента')
    print('5 - удалить данные абонента')
    print('6 - скопирвать строку в файл')
    print('0 - выход из программы')
    print()
    while True:
        cmd = input('Введите пункт меню >>> ')
        if cmd == '1':
            get_records(filename)
        elif cmd == '2':
            write_to_file(filename)
        elif cmd == '3':
            patch_record(filename)
        elif cmd == '4':
            find_actions(filename)
        elif cmd == '5':
            delete_record(filename)
        elif cmd == '6':
            copy_record(filename)
        elif cmd == '0':
            exit(0)
        else:
            print("Вы ввели не правильное значение")


if __name__ == '__main__':
    filename = LOCAL_PATH
    actions(filename)
