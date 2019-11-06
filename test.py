import main 
import unittest

class MyTestCase(unittest.TestCase):

        def setUp(self):
            main.app.testing = True
            self.app = main.app.test_client()

        def test_divfloat(self):
            rv =  self.app.get('/div?A=3.3&B=7.3')
            self.assertMultiLineEqual('0.452054794521', rv.data)
        def test_divfrac(self):
            rv =  self.app.get('/div?A=5/3&B=3/3')
            self.assertMultiLineEqual('1.66666666667', rv.data)
        def test_divneg(self):
            rv =  self.app.get('/div?A=4.3&B=-2.1')
            self.assertMultiLineEqual('-2.04761904762', rv.data)
      
        
if __name__ == '__main__':
    unittest.main()
