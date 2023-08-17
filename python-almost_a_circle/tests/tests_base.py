#!/usr/bin/python3
"""
This is the testfile

for the module base.py

in the models/ directory
"""


import unittest
from models.base import Base
import json

# test_object1 = Base()
# test_object2 = Base()
# test_object3 = Base(89)


class TestBase(unittest.TestCase):
    """
    This is the unittest class

    for the base.py class

    in the models directory
    """
    def test_base_with_or_without_args(self):
        """
        This test for the instance

        of the Base class without

        arguement to see if the id are

        given consecutively after initialization
        """
        self.base1 = Base()
        self.base2 = Base()
        self.base3 = Base(89)
        self.assertEqual(self.base1.id, 1)
        self.assertEqual(self.base2.id, 2)
        self.assertEqual(self.base3.id, 89)

    def test_base_to_json_strings(self):
        self.base4 = Base.to_json_string(None)
        self.base5 = Base.to_json_string([])
        self.base6 = Base.to_json_string([ { 'id': 12 }])
        self.assertListEqual(json.loads(self.base4), [])
        self.assertListEqual(json.loads(self.base5), [])
        self.assertListEqual(json.loads(self.base6), [ { 'id': 12 }])

    def test_base_from_json_strings(self):
        self.base7 = Base.from_json_string(None)
        self.base8 = Base.from_json_string("[]")
        self.base9 = Base.from_json_string('[{ "id": 89 }]')
        self.base10 = Base.from_json_string('[{ "id": 89 }]')
        self.assertEqual(json.dumps(self.base7), "[]")
        self.assertEqual(json.dumps(self.base8), "[]")
        self.assertEqual(json.dumps(self.base9), '[{"id": 89}]')
        self.assertEqual(json.dumps(self.base10), '[{"id": 89}]')
