class PhoneBook:

    def __init__(self, path: str = 'phone_book.txt'):
        self.path = path
        self.phone_book = []

    def open_file(self):
        with open(self.path, 'r', encoding='UTF-8') as file:
            data = file.readlines()

        for contact in data:
            pb = {}
            new = contact.strip().split(';')
            pb['phone'] = new[0]
            pb['name'] = new[1]
            pb['comment'] = new[2]
            self.phone_book.append(pb)
        print('\nТелефонная книга успешно загружена!\n')

    def save_file(self):
        with open(self.path, 'w', encoding='UTF-8') as file:
            file.write(self)

    def get(self):
        return self.phone_book

    def new_contact(self, contact: dict):
        self.phone_book.append(contact)
        print(f'\nКонтакт {contact.get("name")} добавлен\n')

    def search(self, word: str):
        search_result = []
        for contact in self.phone_book:
            for field in contact.values():
                if word in field:
                    search_result.append(contact)
        return search_result

    def change(self, i: int, new_value: dict):
        self.phone_book[i] = new_value

    def delete(self, i: int):
        contact = self.phone_book.pop(i)
        print(f'Контакт {contact.get("name")} успешно удален!')
