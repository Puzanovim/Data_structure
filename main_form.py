from container import Notebook
from age_exception import AgeException

print('--Notebook--')
print('--C-Create--')
print('---A-Add----')
print('--D-Delete--')
print('--R-Change--')
print('--F-Find----')
print('--P-Print---')
print('--Z-Record--')
print('Q-Print JSON')
print('--E-Exit----')
notebooks = []
notebook = Notebook()
count = 0
while True:
    answer = input()
    first_name = ''
    last_name = ''
    middle_name = ''
    home_address = ''
    phone_number = ''
    age = 0
    if answer == 'C':
        notebooks.append(Notebook())
        notebook = notebooks[count]
        print('notebook is created')
    elif answer == 'A':
        print('--создание новой записи--')
        print('введите Фамилию | если данного параметра нет - введите пробел')
        last_name = input()
        while last_name != '-':
            try:
                index = int(last_name)
                print('Фамилией должна быть строка\nУкажите верную фамилию')
                last_name = input()
            except:
                break
        print('введите Имя | если данного параметра нет - введите пробел')
        first_name = input()
        while first_name != '-':
            try:
                index = int(first_name)
                print('Имя должно быть строкой\nУкажите верное имя')
                first_name = input()
            except:
                break
        print('введите Отчество | если данного параметра нет - введите пробел')
        middle_name = input()
        while middle_name != '-':
            try:
                index = int(middle_name)
                print('Отчество должно быть строкой\nУкажите верное отчество')
                middle_name = input()
            except:
                break
        print('введите домашний адрес | если данного параметра нет - введите пробел')
        home_address = input()
        while home_address != '-':
            try:
                index = int(home_address)
                print('Домашний адрес должен быть строкой\nУкажите верный домашний адрес')
                home_address = input()
            except:
                break
        print('введите номер телефона | если данного параметра нет - введите пробел')
        phone_number = input()
        print('введите возраст | если данного параметра нет - введите пробел')
        age = input()
        while age != '-':
            try:
                index = int(age)
                break
            except:
                print('Возрастом должно быть число\nУкажите верный возраст')
                age = input()
        notebook.add(first_name=first_name, last_name=last_name, middle_name=middle_name,
                     home_address=home_address, phone_number=phone_number, age=age)
        print('--запись создана--')
        print('чтобы посмотреть все записи нажмите P')
    elif answer == 'D':
        print('--введите номер записи, которую вы хотите удалить--\n'
              '------иначе - будет удалена последняя запись-------')
        index = input()
        notebook.delete(int(index)-1)
        print(f'--запись под номером {index} удалена')
    elif answer == 'R':
        print('--введите номер записи, которую вы хотите изменить--\n'
              '--------иначе - будет изменина первая запись--------')
        ind = input()
        try:
            index = int(ind)
        except:
            index = 0
        print('---------какой параметр вы хотите изменить?---------')
        print('Имя: нажмите F')
        print('Фамилия: нажмите L')
        print('Отчество: нажмите M')
        print('Домашний адрес: нажмите H')
        print('Номер телефона: нажмите N')
        print('Возраст: нажмите A')
        value = input()
        for symbol in value:
            if value == 'F':
                print('введите имя')
                first_name = input()
            elif value == 'L':
                print('введите фамилию')
                last_name = input()
            elif value == 'M':
                print('введите отчество')
                middle_name = input()
            elif value == 'H':
                print('введите домашний адрес')
                home_address = input()
            elif value == 'N':
                print('введите номер телефона')
                phone_number = input()
            elif value == 'A':
                print('введите возраст')
                age = input()
        notebook.change(index=int(index)-1, first_name=first_name, last_name=last_name, middle_name=middle_name,
                     home_address=home_address, phone_number=phone_number, age=age)
        print('--запись изменина--')
    elif answer == 'F':
        print('--введите фамилию человека, которого хотите найти--')
        name = input()
        values = notebook.find(name)
        if values == 'Такого человека нет :(':
            print(values)
        else:
            print(f'Индекс записи {values[0]}')
            print('Информация о человеке:')
            print(values[1])
    elif answer == 'P':
        if notebook.length() == 0:
            print('К сожалению, пока что нет ни одной записи :(')
        for man in notebook.people:
            print('--------------------')
            print('Номер записи: ', notebook.people.index(man)+1)
            print(man)
            print('--------------------')
    elif answer == 'Z':
        notebook.record()
        print('Notebook is record')
    elif answer == 'Q':
        print(notebook.read())
        print('Notebook is read')
        print('чтобы посмотреть все записи нажмите P')
    elif answer == 'E':
        print('GOOD BYE')
        break

