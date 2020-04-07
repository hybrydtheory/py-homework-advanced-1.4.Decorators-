def parse_dict(my_dict):
    my_string = ''
    for key, val in my_dict.items():
        my_string += f'\t{key}: {val}\n'
    return my_string


def parse_favour(favour):
    if favour:
        return 'да'
    return 'нет'


class Contact:
    def __init__(self, first_name, last_name, phone_number, favourites=False, **kwargs):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.favourites = favourites
        self.other_info = parse_dict(kwargs)
        self.items = [self.first_name, self.last_name, self.phone_number]

    def __str__(self):
        return f'''Имя: {self.first_name}\nФамилия: {self.last_name}
                \rТелефон: {self.phone_number}\nВ избранных: {parse_favour(self.favourites)}\n{self.other_info}'''

    def __lt__(self, other):
        return self.first_name < other.first_name

    def __contains__(self, item):
        return item in self.items


# Task_1_4_(1_2)

from time import strftime, localtime


def param_logger(file_patch):
    def logger(method):
        def wrapper(self, *args, **kwargs):
            res = method(self, *args, **kwargs)
            write_string = f'{strftime(f"%y-%m-%d %H.%M.%S", localtime())} {method.__name__} {args} {kwargs} {res}\n'
            with open(file_patch, 'a', encoding='utf8') as file:
                file.write(write_string)
            return res

        return wrapper

    return logger


file_patch = 'log.txt'


# Task_1_4_3
class PhoneBook:
    @param_logger(file_patch)
    def __init__(self, book_name, contact_list=[]):
        self.book_name = book_name
        self.contact_list = contact_list

    @param_logger(file_patch)
    def add_contact(self, *args, **kwargs):
        self.contact_list.append(Contact(*args, **kwargs))
        self.contact_list.sort()

    @param_logger(file_patch)
    def view_contacts(self):
        for contact in self.contact_list:
            print(contact)

    @param_logger(file_patch)
    def view_favourite(self):
        for contact in self.contact_list:
            if contact.favourites:
                print(contact)

    @param_logger(file_patch)
    def search_contact(self, search_string):
        for contact in self.contact_list:
            if search_string in contact:
                print(contact)

    @param_logger(file_patch)
    def delete_contact(self, phone_number):
        for contact in self.contact_list:
            if phone_number in contact:
                self.contact_list.remove(contact)


# Task_1_3_3

def smart_delimeter(in_string, step, symbol):
    out_string = ''
    for substr in range(int(len(in_string) / step) + 1):
        if (_slice := in_string[step * substr: step * (substr + 1)]):
            out_string += _slice + symbol
    return out_string[0: -1]


def adv_print(*args, **kwargs):
    output_string = kwargs.pop('start', '') + str(*args) + kwargs.pop('end', '')
    if (max_line := kwargs.pop('max_line', False)):
        output_string = smart_delimeter(output_string, max_line, '\n')
    if kwargs.pop('in_file', False):
        with open('output', 'w', encoding='utf8') as f:
            f.write(output_string)
    print(output_string, **kwargs)


if __name__ == '__main__':
    print('===Добавляем контакты===\n')
    book = PhoneBook('Телефонная книга')
    book.add_contact('Jhon', 'Smith', '+71234567809', telegram='@jhony', email='jhony@smith.com')
    book.add_contact('John', 'Lennon', '+79234856583', telegram='@lennon', email='lennon@google.com', favourites=True)
    book.add_contact('Paul', 'McCartney', '+79140945983', telegram='@mccartney', email='mccartney@mail.ru')
    book.add_contact('George', 'Harrison', '+79152358345', telegram='@george', email='george@yandex.ru',
                     favourites=True)
    book.add_contact('Ringo', 'Starr', '+79184445326', telegram='@ringo', email='ringo@yandex.ru')
    print('===Все контакты===\n')
    book.view_contacts()
    print('===Избранные===\n')
    book.view_favourite()
    print('===Поиск===\n')
    book.search_contact('+71234567809')
    print('===Удаление===\n')
    book.delete_contact('+71234567809')
    book.view_contacts()

    adv_print('Тестовая строка', end='Конец', start='Начало', max_line=6, in_file=True)