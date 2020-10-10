import unittest

class MyTest(unittest.TestCase):
    def setUp(self):
        print("----------------1---------------")
    def tearDown(self):
        print("----------------2---------------")

    @classmethod
    def setUpClass(cls):
        print("----------------3---------------")

    @classmethod
    def tearDownClass(cls):
        print("----------------4---------------")

    def test01(self):
        self.assertTrue(100,100)

    def test02(self):
        self.assertEqual(100,200)
