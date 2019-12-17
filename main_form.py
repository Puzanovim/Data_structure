from container import Notebook


def draw(name_form, function_one, function_two):
    print(f'************************')
    print(f'*   {name_form}    *')
    print(f'*                      *')
    print(f'*  {function_one.short_name} - {function_one.name}   *')
    print(f'*  {function_two.short_name} - {function_two.name}   *')
    print(f'************************')


print('--Notebook--')
print('--C-Create--')
print('---A-Add----')
print('--D-Delete--')
print('--R-Change--')
print('--F-Find----')
print('--P-Print---')
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
        print('введите Имя | если данного параметра нет - введите пробел')
        first_name = input()
        print('введите Отчество | если данного параметра нет - введите пробел')
        middle_name = input()
        print('введите домашний адрес | если данного параметра нет - введите пробел')
        home_address = input()
        print('введите номер телефона | если данного параметра нет - введите пробел')
        phone_number = input()
        print('введите возраст | если данного параметра нет - введите пробел')
        age = input()
        notebook.add(first_name=first_name, last_name=last_name, middle_name=middle_name,
                     home_address=home_address, phone_number=phone_number, age=age)
        print('--запись создана--')
        print('чтобы посмотреть все записи нажмите P')
        #print('введите ФИО, домашний адрес, номер телефона или возраст новой записи')
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
            print(man)
            print('--------------------')
    elif answer == 'E':
        print('GOOD BYE')
        break


# answer = input()
# if answer == 'Y':
#     notebook = 0
