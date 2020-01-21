from data_structure import Man
import json


class Notebook:

    def __init__(self, first_name='', last_name='', middle_name='', home_address='', phone_number='', age=0):
        """Создает лист, в котором будут храниться записи,
        если же передаются какие-нибудь ещё значения - создается первая запись"""
        self.people = []
        if first_name != '' or last_name != '' or middle_name != '' or \
                home_address != '' or phone_number != '' or age != 0:
            self.add(first_name, last_name, middle_name, home_address, phone_number, age)

    def add(self, first_name='', last_name='', middle_name='', home_address='', phone_number='', age=0):
        """Добавляет нового человека в Записную книжку"""
        self.people.append(Man(first_name, last_name, middle_name, home_address, phone_number, age))

    def odd(self, obj):
        if isinstance(obj, Man):
            self.add(obj.first_name, obj.last_name, obj.middle_name, obj.home_address, obj.phone_number, obj.age)

    def delete(self, index):
        """Удаляет человека под индексом index, если же индекс не указан, то последнего записанного человека"""
        self.people.pop(index)

    def length(self):
        """Возвращается количество записей в Записной книжке"""
        return len(self.people)

    def change(self, index=0,
               first_name='', last_name='', middle_name='', home_address='', phone_number='', age=0):
        """Меняет значения человека под индексом index, если же индекс не указан,
        то изменения применяются к первому человеку в записной книжке"""
        man = self.people[index]
        man.change(first_name, last_name, middle_name, home_address, phone_number, age)

    def find(self, name):
        """Ищет человека по имени и возвращает его индекс"""
        for man in self.people:
            if man.last_name == name:
                return self.people.index(man), man.data()
        return 'Такого человека нет :('

    def record(self):
        notebook = dict()
        for man in self.people:
            notebook[self.people.index(man)] = [man.first_name, man.last_name, man.middle_name, man.home_address, man.phone_number, man.age]
        data_json = json.dumps(notebook)
        file_json = open('data_json', 'w')
        file_json.write(data_json)
        file_json.close()

    def read(self):
        file_json = open('data_json', 'r')
        data_json = file_json.read()
        file_json.close()
        data = json.loads(data_json)
        for man in data:
            self.add(data[man][0], data[man][1], data[man][2], data[man][3], data[man][4], data[man][5])
