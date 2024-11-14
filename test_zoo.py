import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(5), 50)
       
    def test_1(self):
        self.assertEqual(self.zoo.get_ticket_price(19), 100)

    def test2(self):
        self.assertEqual(self.zoo.get_ticket_price(21), 150)

    def test3(self):
        self.assertEqual(self.zoo.get_ticket_price(20), 100)    

    def test4(self):
        self.assertEqual(self.zoo.get_ticket_price(-1), 'invalid')
    
    def test5(self):
        self.assertEqual(self.zoo.get_ticket_price(61), 100)

    def test6(self):
        self.assertEqual(self.zoo.get_ticket_price(0), 50)

    def test7(self):
        self.assertEqual(self.zoo.get_ticket_price(-8), 'invalid')

    def test8(self):
        self.assertEqual(self.zoo.get_ticket_price(0), 50)

    def test9(self):
        self.assertEqual(self.zoo.get_ticket_price(12), 50)
        
    def test10(self):
        self.assertEqual(self.zoo.get_ticket_price(14), 100)

    def test11(self):
        self.assertEqual(self.zoo.get_ticket_price(18), 100)

    def test12(self):
        self.assertEqual(self.zoo.get_ticket_price(25), 150)

    def test13(self):
        self.assertEqual(self.zoo.get_ticket_price(60), 150)

    def test14(self):
        self.assertEqual(self.zoo.get_ticket_price(68), 100)

    def test15(self):
        self.assertEqual(self.zoo.get_ticket_price(99), 100)

    def test16(self):
        self.assertEqual(self.zoo.get_ticket_price(91), 100)

if __name__ == '__main__':
    unittest.main()