import unittest
from cafeface.app import create_app
from flask import Flask

class TestDemo(unittest.TestCase):

    def test_demo(self):
        self.assertTrue(isinstance(create_app(), Flask))


if __name__ == '__main__':
    unittest.main()