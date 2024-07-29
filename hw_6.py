from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        if len(value) > 0:
            super().__init__(value)


class Phone(Field):
    def __init__(self, value: str):
        if len(value) == 10 and value.isdigit():
            super().__init__(value)
        else:
            raise ValueError


class Record:
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        for ph in self.phones:
            if ph.value == phone:
                self.phones.remove(ph)

    def edit_phone(self, old_phone, new_phone):
        for ph in self.phones:
            if ph.value == old_phone:
                if len(new_phone) == 10 and new_phone.isdigit():
                    ph.value = new_phone
                    break
        else:
            raise ValueError

    def find_phone(self, phone):
        for ph in self.phones:
            if ph.value == phone:
                return self.phones[phone]

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, note):
        self.data[note.name.value] = note

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        del self.data[name]

    def __str__(self):
        return f"Contacts book: name: {'; '.join(p for p in self.data)}"


# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("9999999999")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі

print(book)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "5555555555")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

# Видалення запису Jane
book.delete("Jane")
