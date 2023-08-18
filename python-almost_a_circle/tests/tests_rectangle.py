#!/usr/bin/python3
"""Test case for Rectangle class"""

import unittest
from models.rectangle import Rectangle
from models.base import Base
from io import StringIO
from unittest.mock import patch
import os 


class TestRectangle(unittest.TestCase):
    """Test class for rectangle"""

    def test_instance(self):
        """Test instance"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(1, 2)
        r2 = Rectangle(1, 2, 3)
        r3 = Rectangle(1, 2, 3, 4)
        r4 = Rectangle(1, 2, 3, 4, 5)

        self.assertEqual(r4.id, 5)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r5 = Rectangle(0, 2)
        
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r6 = Rectangle(1, 0)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r7 = Rectangle(-1, 2)

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r8 = Rectangle(1, -2)

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r9 = Rectangle(1, 2, -3)

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r10 = Rectangle(1, 2, 3, -4)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r11 = Rectangle("1", 2)

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r12 = Rectangle(1, "2")

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r13 = Rectangle(1, 2, "3")

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r14 = Rectangle(1, 2, 3, "4")

    def test_area(self):
        """Test area"""
        a1 = Rectangle(4, 2)
        self.assertEqual(a1.area(), 8)

    def test__str__(self):
        """Test __str__"""
        Base._Base__nb_objects = 0
        s1 = Rectangle(4, 2)
        with patch('sys.stdout', new=StringIO()) as f:
            print(s1)
            self.assertEqual(f.getvalue(), "[Rectangle] (1) 0/0 - 4/2\n")

    def test_display(self):
        """Test for dispaly"""
        d1 = Rectangle(4, 2)
        d2 = Rectangle(4, 2, 3)
        d3 = Rectangle(4, 2, 3, 2)
        with patch('sys.stdout', new=StringIO()) as f:
            d1.display()
            self.assertEqual(f.getvalue(), "####\n####\n")

        with patch('sys.stdout', new=StringIO()) as f:
            d2.display()
            self.assertEqual(f.getvalue(), "   ####\n   ####\n")

        with patch('sys.stdout', new=StringIO()) as f:
            d3.display()
            self.assertEqual(f.getvalue(), "\n\n   ####\n   ####\n")

    def test_dictionary(self):
        """Test for dictionary"""
        Base._Base__nb_objects = 0
        d1 = Rectangle(4, 2)
        self.assertEqual(d1.to_dictionary(),
        {'x': 0, 'y': 0, 'id': 1, 'height': 2, 'width': 4})

    def test_update(self):
        """Test for update"""
        Base._Base__nb_objects = 0
        u1 = Rectangle(4, 2)

        u1.update()
        self.assertEqual(u1.id, 1)

        u1.update(89)
        self.assertEqual(u1.id, 89)

        u1.update(89, 1)
        self.assertEqual(u1.width, 1)
        self.assertEqual(u1.id, 89)

        u1.update(89, 1, 2)
        self.assertEqual(u1.height, 2)
        self.assertEqual(u1.width, 1)
        self.assertEqual(u1.id, 89)

        u1.update(89, 1, 2, 3)
        self.assertEqual(u1.height, 2)
        self.assertEqual(u1.width, 1)
        self.assertEqual(u1.id, 89)
        self.assertEqual(u1.x, 3)

        u1.update(89, 1, 2, 3, 4)
        self.assertEqual(u1.height, 2)
        self.assertEqual(u1.width, 1)
        self.assertEqual(u1.id, 89)
        self.assertEqual(u1.x, 3)
        self.assertEqual(u1.y, 4)

        u1.update(**{'id': 89})
        self.assertEqual(u1.id, 89)

        u1.update(**{'id': 89, 'width': 1})
        self.assertEqual(u1.id, 89)
        self.assertEqual(u1.width, 1)

        u1.update(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(u1.id, 89)
        self.assertEqual(u1.width, 1)
        self.assertEqual(u1.height, 2)

        u1.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(u1.id, 89)
        self.assertEqual(u1.width, 1)
        self.assertEqual(u1.height, 2)
        self.assertEqual(u1.x, 3)


        u1.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(u1.id, 89)
        self.assertEqual(u1.width, 1)
        self.assertEqual(u1.height, 2)
        self.assertEqual(u1.x, 3)
        self.assertEqual(u1.y, 4)


    def test_create(self):
        """test for create function"""
        c1 = Rectangle.create(**{'id': 89})
        self.assertEqual(c1.id, 89)

        c1 = Rectangle.create(**{'id': 89, 'width': 1})
        self.assertEqual(c1.id, 89)
        self.assertEqual(c1.width, 1)

        c1 = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(c1.id, 89)
        self.assertEqual(c1.width, 1)
        self.assertEqual(c1.height, 2)

        c1 = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(c1.id, 89)
        self.assertEqual(c1.width, 1)
        self.assertEqual(c1.height, 2)

        c1 = Rectangle.create(**{'id': 89, 'width': 1, 
        'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(c1.id, 89)
        self.assertEqual(c1.width, 1)
        self.assertEqual(c1.height, 2)
        self.assertEqual(c1.x, 3)

    def test_save_to_file(self):
        """Test for save_to_file"""
        Base._Base__nb_objects = 0

        Rectangle.save_to_file(None)
        self.assertTrue(os.path.isfile("Rectangle.json"))
        with open("Rectangle.json") as f:
            self.assertEqual(f.read(), "[]")

        Rectangle.save_to_file([])
        with open("Rectangle.json") as f:
            self.assertEqual(f.read(), "[]")
            self.assertEqual(type(f.read()), str)

        Rectangle.save_to_file([Rectangle(1, 2)])
        with open("Rectangle.json") as file:
            self.assertEqual(file.read(), '[{"x": 0, "y": 0, "width": 1, "height": 2, "id": 1}]')

    def test_save_file_empty(self):
        """Test for save_to_file with empty list"""
        Rectangle.save_to_file([])
        self.assertTrue(os.path.isfile("Rectangle.json"))
        with open("Rectangle.json") as f:
            self.assertEqual(f.read(), "[]")
            self.assertEqual(type(f.read()), str)

    def test_load_from_file(self):
        """Test for load from file function"""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

        self.assertEqual(Rectangle.load_from_file(), [])
        Rectangle.save_to_file([Rectangle(1, 2)])
        file = Rectangle.load_from_file()
        self.assertEqual(type(file), list)
        self.assertEqual(file[0].width, 1)
        self.assertEqual(file[0].height, 2)

if __name__ == '__main__':
    unittest.main()
