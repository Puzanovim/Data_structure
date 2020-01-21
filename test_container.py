import unittest
from container import Notebook
from data_structure import Man


class MyTestInit(unittest.TestCase):
    new_notebook = Notebook()

    def test_empty_init(self):
        new_notebook = Notebook()
        self.assertEqual(new_notebook.people, list())

    def test_init(self):
        new_notebook = Notebook('Igor', 'Puzanov', home_address='Izhevsk', phone_number='55-00-55', age=20)
        self.assertEqual(new_notebook.people[0].data(),
                         Man('Igor', 'Puzanov', home_address='Izhevsk', phone_number='55-00-55', age=20).data())

    def test_delete(self):
        print('-----------\n')
        new_notebook = Notebook()
        new_notebook.add('Igor', 'Puzanov', home_address='Izhevsk', phone_number='55-00-55', age=20)
        new_notebook.add('Igor', 'Puzanov', home_address='Izhevsk', phone_number='55-00-55', age=19)
        new_notebook.add('Igor', 'Puzanov', 'Mixail', home_address='Izhevsk', phone_number='55-00-55', age=18)
        new_notebook.add('Igor', 'Puzanov', 'Alex', home_address='Izhevsk', phone_number='55-00-55', age=17)
        print(new_notebook.length())
        for man in new_notebook.people:
            print(man)
        new_notebook.delete(2)
        print(new_notebook.length())
        for man in new_notebook.people:
            print(man)

    def test_change(self):
        print('-----------\n')
        new_notebook = Notebook()
        new_notebook.add('Igor', 'Puzanov', home_address='Izhevsk', phone_number='55-00-55', age=20)
        new_notebook.add('Igor', 'Puzanov', home_address='Izhevsk', phone_number='55-00-55', age=19)
        new_notebook.add('Igor', 'Puzanov', 'Mixail', home_address='Izhevsk', phone_number='55-00-55', age=18)
        print(new_notebook.length())
        for man in new_notebook.people:
            print(man)
        new_notebook.change(1, middle_name='Alex')
        for man in new_notebook.people:
            print(man)
        new_notebook.change(first_name='Alo')
        for man in new_notebook.people:
            print(man)
        print('\n\n\n')
        print(new_notebook.find("Igor Puzanov Mixail"))

    def test_add(self):
        new_notebook = Notebook()
        new_notebook.add('Igor', 'Puzanov', home_address='Izhevsk', phone_number='55-00-55', age=20)
        self.assertEqual(new_notebook.people[0].data(),
                         Man('Igor', 'Puzanov', home_address='Izhevsk', phone_number='55-00-55', age=20).data())

    def test_odd(self):
        new_notebook = Notebook()
        new_man = Man('Igor', 'Puzanov', home_address='Izhevsk', phone_number='55-00-55', age=20)
        new_notebook.odd(new_man)
        new_notebook.odd('hello')
        print(new_notebook.length())
        self.assertEqual(new_notebook.people[0].data(),
                         Man('Igor', 'Puzanov', home_address='Izhevsk', phone_number='55-00-55', age=20).data())
        self.assertEqual(new_notebook.length(), 1)

    def test_record_and_read(self):
        new_notebook = Notebook()
        new_notebook.add('Igor', 'Puzanov', home_address='Izhevsk', phone_number='55-00-55', age=20)
        new_notebook.record()
        new_notebook.read()
        self.assertEqual(new_notebook.length(), 2)


if __name__ == '__main__':
    unittest.main()
