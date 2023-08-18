#!/usr/bin/python3
"""
testing rectangle
"""
import sys
import unittest
import json
from models.rectangle import Rectangle
from io import StringIO
#from models.square import Square

class TestRectangle(unittest.TestCase):
    """
    doc
    """
    def test_rectangle(self):
        """
        doc
        """
        r1 = Rectangle(1,2)
        r2 = Rectangle(1,2,3)
        r3 = Rectangle(1,2,3,4)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r2.x, 3)
        self.assertEqual(r3.y, 4)

    def test_rectangle_args(self):
        """
        doc
        """
        self.assertRaises(TypeError, Rectangle, "1" ,2)
        self.assertRaises(TypeError, Rectangle, 1, "2")
        self.assertRaises(TypeError, Rectangle, 1, 2, 3, "4")
        self.assertRaises(TypeError, Rectangle, 1, 2, "3")
        self.assertRaises(ValueError, Rectangle, 1, 2, 3, -6,)
        self.assertRaises(ValueError, Rectangle, 1,2,-3,4)
        self.assertRaises(ValueError, Rectangle, 1,-2,3,4)
        self.assertRaises(ValueError,Rectangle, -1,2,3,4)
        self.assertEqual(Rectangle(1,2,3,4,5).id, 5)
        self.assertRaises(ValueError, Rectangle, 0, 1)
        self.assertRaises(ValueError, Rectangle,1, 0)

    def test_methods(self):
        """
        doc
        """
        r2 = Rectangle(2,3, id=24)
        self.assertEqual(r2.area(), 6)
        self.assertEqual(r2.__str__(), "[Rectangle] (24) 0/0 - 2/3")

    def test_methods_update(self):
        """
        doc
        """
        r = Rectangle(10,12, id=12)
        r.update(1)
        self.assertNotEqual(r.id, 12)
        r.update(1,2)
        self.assertNotEqual(r.width, 10)
        r.update(1,2,3)
        self.assertNotEqual(r.height, 12)
        r.update(1,2,3,4)
        self.assertNotEqual(r.x, 0)
        r.update(1,2,3,4,5)
        self.assertNotEqual(r.y, 0)
        #passing now a dict to update
        self.assertNotEqual(r.id, r.update(**{"id": 89}))
        self.assertNotEqual(r.width, r.update(**{"id": 89, "width": 3}))
        self.assertNotEqual(r.height, r.update(**{"id": 89, "width": 4, "height": 21}))
        self.assertNotEqual(r.x, r.update(**{"id": 89, "width": 4, "height": 21, "x": 3}))
        self.assertNotEqual(r.y, r.update(**{"id": 89, "width": 4, "height": 21, "x": 3, "y": 6}))

    def test_to_dict(self):
        """
        doc
        """
        r = Rectangle(1, 2, id=12)
        self.assertEqual(r.to_dictionary(), {"id": 12, "x": 0, "y": 0, "width": 1, "height": 2})


    def test_create(self):
        """
        doc
        """
        r = Rectangle.create(**{"id": 23})
        self.assertEqual(r.id, 23)
        r = Rectangle.create(**{"id": 23, "width": 2})
        self.assertEqual(r.width, 2)
        r = Rectangle.create(**{"id": 23, "width": 2, "height": 3})
        self.assertEqual(r.height, 3)
        r = Rectangle.create(**{"id":23, "width": 2, "height": 3, "x": 2})
        self.assertEqual(r.x, 2)
        r = Rectangle.create(**{"id":23, "width": 2, "height": 3, "x": 2, "y": 4})
        self.assertEqual(r.y, 4)

    def test_save_to_file(self):
        """
        doc
        """
        r = Rectangle(1,2, id=23)
        Rectangle.save_to_file(None)
        with open("Rectangle.json") as f:
            cont = f.read()
            self.assertEqual(cont, '[]')
        Rectangle.save_to_file([])
        with open("Rectangle.json")as f:
            content = f.read()
            self.assertEqual(content, '[]')
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            content = f.read()
            self.assertEqual(content, '[{"width": 1, "height": 2, "x": 0, "y": 0, "id": 23}]')

    def test_load_from_file(self):
        """
        doc
        """
        Rectangle.save_to_file([])
        my_list = Rectangle.load_from_file()
        self.assertEqual(my_list, [])

    def test_load_from_file2(self):
        """
        doc
        """
        r = Rectangle(1, 2)
        Rectangle.save_to_file([r])
        my_list = Rectangle.load_from_file()
        self.assertEqual(type(my_list[0]), type(Rectangle.create(**r.to_dictionary())))

    def test_display(self):
        """
        doc
        """
        # testing display with x,y = (0,0)
        r = Rectangle(2,3)
        r1 = Rectangle(2,3,2)
        r2 = Rectangle(2,3,2,2)
        inst = StringIO()
        sys.stdout = inst
        r.display()
        to_check = inst.getvalue().strip()
        sys.stdout = sys.__stdout__
        expected = "##\n##\n##"
        self.assertEqual(to_check, expected)
        #testing display with cordinates (2, 0)
        inst2 = StringIO()
        sys.stdout = inst2
        r1.display()
        to_check = inst2.getvalue().strip()
        sys.stdout = sys.__stdout__
        expected = "##\n  ##\n  ##"
        self.assertEqual(to_check, expected)
        # testing display with cordinates (2,2)
        sys.stdout = inst
        r2.display()
        to_check = inst.getvalue().strip()
        sys.stdout = sys.__stdout__
        expected = "##\n##\n##\n\n\n  ##\n  ##\n  ##"
        self.assertEqual(to_check, expected)
