class Man:
    def __init__(self, first_name='', last_name='', middle_name='', home_address='', phone_number='', age=0):
        # TODO
        #  нужно добавить определитель свойства класса:
        #  если число - то возрас, если длинное число - то телефон, если строка с числом - то адрес
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.home_address = home_address
        self.phone_number = phone_number
        self.age = age
        self.name = f'{self.first_name} {self.last_name} {self.middle_name}'

    def print(self):
        print(f'Name         : {self.first_name} {self.last_name} {self.middle_name}\n'
              f'Home address : {self.home_address}\n'
              f'Phone number : {self.phone_number}\n'
              f'Age          : {self.age}')

    def data(self):
        return f'Name         : {self.first_name} {self.last_name} {self.middle_name}\n' \
               f'Home address : {self.home_address}\n' \
               f'Phone number : {self.phone_number}\n' \
               f'Age          : {self.age}'

    def change(self, first_name='', last_name='', middle_name='', home_address='', phone_number='', age=0):
        if first_name != '':
            self.first_name = first_name
        if last_name != '':
            self.last_name = last_name
        if middle_name != '':
            self.middle_name = middle_name
        if home_address != '':
            self.home_address = home_address
        if phone_number != '':
            self.phone_number = phone_number
        if age != 0:
            self.age = age
        self.name = f'{self.first_name} {self.last_name} {self.middle_name}'

    def __str__(self):
        return self.data()
