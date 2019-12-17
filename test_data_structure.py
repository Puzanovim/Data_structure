import unittest
from data_structure import Man


class MyTestCase(unittest.TestCase):
    def test_zero_data(self):
        print(f'\n-------Test Zero Data--------')
        new_man = Man()
        new_man.print()
        self.assertEqual(new_man.data(),  'Name         :   \n'
                                          'Home address : \n'
                                          'Phone number : \n'
                                          'Age          : 0')

    def test_only_first_name_data(self):
        print(f'\n-------Test Only Name Data--------')
        new_man = Man(first_name='Edward')
        new_man.print()
        self.assertEqual(new_man.data(),  'Name         : Edward  \n'
                                          'Home address : \n'
                                          'Phone number : \n'
                                          'Age          : 0')

    def test_only_last_name_data(self):
        print(f'\n-------Test Only Last Name Data--------')
        new_man = Man(last_name='George')
        new_man.print()
        self.assertEqual(new_man.data(),  'Name         :  George \n'
                                          'Home address : \n'
                                          'Phone number : \n'
                                          'Age          : 0')

    def test_only_middle_name_data(self):
        print(f'\n-------Test Only Middle Name Data--------')
        new_man = Man(middle_name='Second')
        new_man.print()
        self.assertEqual(new_man.data(),  'Name         :   Second\n'
                                          'Home address : \n'
                                          'Phone number : \n'
                                          'Age          : 0')

    def test_only_home_address_data(self):
        print(f'\n-------Test Only Home Address Data--------')
        new_man = Man(home_address='Starbucks street 5')
        new_man.print()
        self.assertEqual(new_man.data(),  'Name         :   \n'
                                          'Home address : Starbucks street 5\n'
                                          'Phone number : \n'
                                          'Age          : 0')

    def test_only_phone_number_data(self):
        print(f'\n-------Test Only Phone Number Data--------')
        new_man = Man(phone_number='+7 (912) 754-35-07')
        new_man.print()
        self.assertEqual(new_man.data(),  'Name         :   \n'
                                          'Home address : \n'
                                          'Phone number : +7 (912) 754-35-07\n'
                                          'Age          : 0')

    def test_only_age_data(self):
        print(f'\n-------Test Only Age Data--------')
        new_man = Man(age=35)
        new_man.print()
        self.assertEqual(new_man.data(),  'Name         :   \n'
                                          'Home address : \n'
                                          'Phone number : \n'
                                          'Age          : 35')

    def test_full_data(self):
        print(f'\n\n\n-------Test Full Data--------')
        new_man = Man('Edward', 'George', 'Second', 'Starbucks street 5', '+7 (912) 754-35-07', 35)
        new_man.print()
        self.assertEqual(new_man.data(),  'Name         : Edward George Second\n'
                                          'Home address : Starbucks street 5\n'
                                          'Phone number : +7 (912) 754-35-07\n'
                                          'Age          : 35')

    def test_change_zero_data(self):
        print(f'\n-------Test Change Zero Data--------')
        new_man = Man('Edward', 'George', 'Second', 'Starbucks street 5', '+7 (912) 754-35-07', 35)
        new_man.change()
        new_man.print()
        self.assertEqual(new_man.data(),  'Name         : Edward George Second\n'
                                          'Home address : Starbucks street 5\n'
                                          'Phone number : +7 (912) 754-35-07\n'
                                          'Age          : 35')

    def test_change_only_first_name_data(self):
        print(f'\n-------Test Change Only Name Data--------')
        new_man = Man('Edward', 'George', 'Second', 'Starbucks street 5', '+7 (912) 754-35-07', 35)
        new_man.change(first_name='Ivan')
        new_man.print()
        self.assertEqual(new_man.data(),  'Name         : Ivan George Second\n'
                                          'Home address : Starbucks street 5\n'
                                          'Phone number : +7 (912) 754-35-07\n'
                                          'Age          : 35')

    def test_change_only_last_name_data(self):
        print(f'\n-------Test Change Only Last Name Data--------')
        new_man = Man('Edward', 'George', 'Second', 'Starbucks street 5', '+7 (912) 754-35-07', 35)
        new_man.change(last_name='Ivanov')
        new_man.print()
        self.assertEqual(new_man.data(), 'Name         : Edward Ivanov Second\n'
                                         'Home address : Starbucks street 5\n'
                                         'Phone number : +7 (912) 754-35-07\n'
                                         'Age          : 35')

    def test_change_only_middle_name_data(self):
        print(f'\n-------Test Change Only Middle Name Data--------')
        new_man = Man('Edward', 'George', 'Second', 'Starbucks street 5', '+7 (912) 754-35-07', 35)
        new_man.change(middle_name='Ivanovich')
        new_man.print()
        self.assertEqual(new_man.data(), 'Name         : Edward George Ivanovich\n'
                                         'Home address : Starbucks street 5\n'
                                         'Phone number : +7 (912) 754-35-07\n'
                                         'Age          : 35')

    def test_change_only_home_address_data(self):
        print(f'\n-------Test Change Only Home Address Data--------')
        new_man = Man('Edward', 'George', 'Second', 'Starbucks street 5', '+7 (912) 754-35-07', 35)
        new_man.change(home_address='Kominterna street 2')
        new_man.print()
        self.assertEqual(new_man.data(),  'Name         : Edward George Second\n'
                                          'Home address : Kominterna street 2\n'
                                          'Phone number : +7 (912) 754-35-07\n'
                                          'Age          : 35')

    def test_change_only_phone_number_data(self):
        print(f'\n-------Test Change Only Phone Number Data--------')
        new_man = Man('Edward', 'George', 'Second', 'Starbucks street 5', '+7 (912) 754-35-07', 35)
        new_man.change(phone_number='8 (800) 555-35-35')
        new_man.print()
        self.assertEqual(new_man.data(),  'Name         : Edward George Second\n'
                                          'Home address : Starbucks street 5\n'
                                          'Phone number : 8 (800) 555-35-35\n'
                                          'Age          : 35')

    def test_change_only_age_data(self):
        print(f'\n-------Test Change Only Age Data--------')
        new_man = Man('Edward', 'George', 'Second', 'Starbucks street 5', '+7 (912) 754-35-07', 35)
        new_man.change(age=85)
        new_man.print()
        self.assertEqual(new_man.data(),  'Name         : Edward George Second\n'
                                          'Home address : Starbucks street 5\n'
                                          'Phone number : +7 (912) 754-35-07\n'
                                          'Age          : 85')

    def test_change_full_data(self):
        print(f'\n-------Test Change Full Data--------')
        new_man = Man('Edward', 'George', 'Second', 'Starbucks street 5', '+7 (912) 754-35-07', 35)
        new_man = Man('Ivan', 'Ivanov', 'Ivanovich', 'Kominterna street 5', '8 (800) 555-35-35', 85)
        new_man.print()
        self.assertEqual(new_man.data(),  'Name         : Ivan Ivanov Ivanovich\n'
                                          'Home address : Kominterna street 5\n'
                                          'Phone number : 8 (800) 555-35-35\n'
                                          'Age          : 85')


if __name__ == '__main__':
    unittest.main()

