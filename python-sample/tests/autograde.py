import unittest
# Needs xmlrunner: pip install unittest-xml-reporting
import xmlrunner
import sys

class PublicTestsGrader(unittest.TestCase):
    def setUp(self):
        # clears the dictionary containing metadata for each test
        self.meta = { 'expression': '', 'expected': '', 'hint': '' }
    def test_public_01(self):
        self.meta['expression'] = "test_results('public', 1)"
        self.meta['expected'] = str(True)
        self.meta['hint'] = "Be True"
        _out = test_results('public', 1)
        self.meta['output'] = "'" + _out + "'" if isinstance(_out, str) else _out
        self.assertEqual(_out, True)
    def test_public_02(self):
        self.meta['expression'] = "test_results('public', 2)"
        self.meta['expected'] = str(True)
        
        _out = test_results('public', 2)
        self.meta['output'] = "'" + _out + "'" if isinstance(_out, str) else _out
        self.assertEqual(_out, True)

class PrivateTestsGrader(unittest.TestCase):
    def setUp(self):
        # clears the dictionary containing metadata for each test
        self.meta = { 'expression': '', 'expected': '', 'hint': '' }
    def test_private_01(self):
        self.meta['expression'] = "test_results('private', 1)"
        self.meta['expected'] = str(True)
        
        _out = test_results('private', 1)
        self.meta['output'] = "'" + _out + "'" if isinstance(_out, str) else _out
        self.assertEqual(_out, True)
    def test_private_02(self):
        self.meta['expression'] = "test_results('private', 2)"
        self.meta['expected'] = str(True)
        
        _out = test_results('private', 2)
        self.meta['output'] = "'" + _out + "'" if isinstance(_out, str) else _out
        self.assertEqual(_out, True)

class EvaluationTestsGrader(unittest.TestCase):
    def setUp(self):
        # clears the dictionary containing metadata for each test
        self.meta = { 'expression': '', 'expected': '', 'hint': '' }
    def test_evaluation_01(self):
        self.meta['expression'] = "test_results('evaluation', 1)"
        self.meta['expected'] = str(True)
        
        _out = test_results('evaluation', 1)
        self.meta['output'] = "'" + _out + "'" if isinstance(_out, str) else _out
        self.assertEqual(_out, True)
    def test_evaluation_02(self):
        self.meta['expression'] = "test_results('evaluation', 2)"
        self.meta['expected'] = str(True)
        
        _out = test_results('evaluation', 2)
        self.meta['output'] = "'" + _out + "'" if isinstance(_out, str) else _out
        self.assertEqual(_out, True)


# Do not modify beyond this line
if __name__ == '__main__':
    unittest.main(
            testRunner=xmlrunner.XMLTestRunner(open('report.xml', 'wb'), outsuffix = ''),
            failfast=False,
            buffer=False,
            catchbreak=False)
