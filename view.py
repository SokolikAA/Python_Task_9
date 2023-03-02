

def menu():
    print('=====================================\n'
          '|          Телефонная книга         |\n'
          '=====================================\n'
          '|            Главное меню           |\n'
          '=====================================\n'
          '1: Открыть файл\n'
          '2: Сохранить файл\n'
          '3: Показать контакты\n'
          '4: Добавить контакт\n'
          '5: Найти контакт\n'
          '6: Изменить контакт\n'
          '7: Удалить контакт\n'
          '8: Выход\n')
    while True:
        choice = input('Введите номер меню: ')
        if choice.isdigit() and (0 < int(choice) < 9):
            return int(choice)


def show_contact(phone_book: list):
    print()
    if phone_book:
        for i, contact in enumerate(phone_book, 1):
            print(f'{i}. {contact.get("phone"):<15}'
                  f'{contact.get("name"):<20}'
                  f'{contact.get("comment"):<20}')
        print()
    else:
        print('\nТелефонная книга не открыта или пуста\n')


def new_contact():
    print()
    phone = input('Введите номер телефона контакта: ')
    name = input('Введите имя и фамилию контакта: ')
    comment = input('Введите коментарий: ')
    print()
    return {'phone': phone, 'name': name, 'comment': comment}


def change_contact(book: list):
    show_contact(book)
    choice = int(input('Выберите контакт, который хотите изменить: '))
    phone = input('Введите новый номер или Enter если оставить без изменений: ')
    name = input('Введите новое имя или Enter если оставить без изменений: ')
    comment = input('Введите новый коментарий или Enter если оставить без изменений: ')
    return choice - 1, {'phone': phone if phone else book[choice - 1].get('phone'),
                        'name': name if name else book[choice - 1].get('name'),
                        'comment': comment if comment else book[choice - 1].get('comment')}


def input_request(text: str):
    return input(f'Введите {text}: ')

def select_to_delete(book: list):
    show_contact(book)
    return int(input('Введите номер контакта, который хотите удалить: ')) - 1

def goodbye():
    print('Досвидания!')
