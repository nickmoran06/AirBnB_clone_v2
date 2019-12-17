#!/usr/bin/python3
"""test for BaseModel"""
import unittest
import os
from models.base_model import BaseModel
import pep8


class TestBaseModel(unittest.TestCase):
    """this will test the base model class"""

    @classmethod
    def setUpClass(cls):
        """setup for the test"""
        cls.base = BaseModel()
        cls.base.name = "Kev"
        cls.base.num = 20

    @classmethod
    def teardown(cls):
        """at the end of the test this will tear it down"""
        del cls.base

    def tearDown(self):
        """teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_BaseModel(self):
        """Testing for pep8"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/base_model.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_checking_for_docstring_BaseModel(self):
        """checking for docstrings"""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_method_BaseModel(self):
        """chekcing if Basemodel have methods"""
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_init_BaseModel(self):
        """test if the base is an type BaseModel"""
        self.assertTrue(isinstance(self.base, BaseModel))

    def test_save_BaesModel(self):
        """test if the save works"""
        self.base.save()
        self.assertNotEqual(self.base.created_at, self.base.updated_at)

    def test_to_dict_BaseModel(self):
        """test if dictionary works"""
        base_dict = self.base.to_dict()
        self.assertEqual(self.base.__class__.__name__, 'BaseModel')
        self.assertIsInstance(base_dict['created_at'], str)
        self.assertIsInstance(base_dict['updated_at'], str)

    # Functionality
    def test_AtributtesClass(self):
        self.assertNotEqual(datetime.now(), self.inst.created_at)
        self.assertNotEqual(datetime.now(), self.inst.updated_at)
        self.assertNotEqual(self.inst.created_at, self.inst.updated_at)

    def test_save(self):
        Instance = BaseModel()
        Instance.save()

    # Documentation
    def test_ModuleDocstring(self):
        """Testing the documentation of the module"""
        self.assertIsNotNone(BaseModel.__doc__)

    def test_MethodsDocstring(self):
        """Testing the documentation of the different methods"""
        for doc in dir(BaseModel):
            self.assertIsNotNone(doc.__doc__)

    # Existence and types
    def test_IsInstance(self):
        """Testing the existence of the instance"""
        In = BaseModel()
        DIn = self.inst.to_dict()
        self.assertIsInstance(self.inst, BaseModel)
        self.assertEqual(DIn['__class__'], "BaseModel")
        self.assertEqual(DIn['created_at'],
                         self.inst.created_at.isoformat())
        self.assertEqual(DIn['updated_at'],
                         self.inst.updated_at.isoformat())
        self.assertEqual(DIn['id'], self.inst.id)
        In.save()

    def test_Types(self):
        """Test the types of the atributes"""
        self.assertEqual(str, type(self.inst.id))
        self.assertIs(str, type(self.inst.id))
        self.assertIs(datetime, type(self.inst.created_at))
        self.assertIs(datetime, type(self.inst.updated_at))
        self.assertFalse(self.inst.updated_at == datetime.utcnow())

    def test_File(self):
        """The existence of the json file"""
        self.inst.save()
        self.assertTrue(os.path.isfile("file.json"))

    def test_Methods(self):
        """Testing the existence of the different methods"""
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "__str__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_ClassDict(self):
        """Testing the dictionary of the class"""
        ClassDict = self.inst.to_dict()
        self.assertEqual(type(ClassDict), dict)
        self.assertIsInstance(ClassDict["created_at"], str)
        self.assertIsInstance(ClassDict["updated_at"], str)


if __name__ == "__main__":
    unittest.main()
