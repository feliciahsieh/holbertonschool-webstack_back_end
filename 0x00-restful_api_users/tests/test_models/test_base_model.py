#!/usr/bin/python3
"""
test_base_model.py - unit tests BaseModel class
"""

import datetime
import models
import pep8 as pycodestyle
import unittest
from unittest import mock
import uuid
BaseModel = models.base_model.BaseModel
module_doc = models.base_model.__doc__


class test_BaseModelDocs(unittest.TestCase):
    """
    Test BaseModelDocs class - uses unittest
    """

    @classmethod
    def setUpClass(self):
        """
        setupClass() - setup for docstring tests
        """
        self.base_funcs = inspect.getmembers(BaseModel, inspect.isfunction)

    def test_pycodestyle_conformance(self):
        """
        test_pycodestyle_conformance() - test code with pycodestyle linter
        """
        for path in ['models/base_model.py',
                     'tests/test_models/test_base_model.py']:
            with self.subTest(path=path):
                errors = pycodestyle.Checker(path).check_all()
                self.assertEqual(errors, 0)

    def test_module_docstring(self):
        """
        Test for existence of module docstring
        """
        self.assertIsNot(module_doc, None,
                         "base_model.py needs a docstring")
        self.assertTrue(len(module_doc) > 1,
                        "base_model.py needs a docstring")

    def test_class_docstring(self):
        """
        Test for BaseModel class docstring
        """
        self.assertIsNot(BaseModel.__doc__, None,
                         "BaseModel class needs a docstring")
        self.assertTrue(len(BaseModel.__doc__) >= 1,
                        "BaseModel class needs a docstring")

    def test_func_docstrings(self):
        """
        Test for presence of docstrings in BaseModel methods
        """
        for func in self.base_funcs:
            with self.subTest(function=func):
                self.assertIsNot(
                    func[1].__doc__,
                    None,
                    "{:s} method needs a docstring".format(func[0])
                )
                self.assertTrue(
                    len(func[1].__doc__) > 1,
                    "{:s} method needs a docstring".format(func[0])
                )


class TestBaseModel(unittest.TestCase):
    """
    """

    def test_id(self):
        """
        test_id() - does id exists
        """
        bm1 = BaseModel()
        bm2 = BaseModel()
        for bm in [bm1, bm2]:
            uuid = bm.id
            with self.subTest(uuid=uuid):
                self.assertIs(type(uuid), str)
                self.assertRegex(uuid,
                                 '^[0-9a-f]{8}-[0-9a-f]{4}'
                                 '-[0-9a-f]{4}-[0-9a-f]{4}'
                                 '-[0-9a-f]{12}$')
        self.assertNotEqual(bm1.id, bm2.id)

    def test_created_at(self):
        """
        test_created_at() - does created_at exists
        """
        d = datetime.datetime.now()
        self.assertEqual(type(self.created_at), type(d))

    def test_updated_at(self):
        """
        test_updated_at() - does updated_at exists
        """
        d = datetime.datetime.now()
        self.assertEqual(type(self.updated_at), type(d))

    def test_id_unique(self):
        """
        test_id_unique() - is id unique
        """
        n = uuid.uuid4()
        self.assertEqual(self.id, n)
