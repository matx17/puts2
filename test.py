import main 
import unittest

class MyTestCase(unittest.TestCase):

        def setUp(self):
            main.app.testing = True
            self.app = main.app.test_client()

        def test_mulint(self):
            rv =  self.app.get('/mul?A=3&B=7')
            self.assertMultiLineEqual('21', rv.data)
        def test_mulfloat(self):
            rv =  self.app.get('/mul?A=3.3&B=7.3')
            self.assertMultiLineEqual('24.09', rv.data)
        def test_mulfrac(self):
            rv =  self.app.get('/mul?A=5/3&B=3/3')
            self.assertMultiLineEqual('1.66666666667', rv.data)
        def test_mulneg(self):
            rv =  self.app.get('/mul?A=4.3&B=-2.1')
            self.assertMultiLineEqual('-9.03', rv.data)
      
        
if __name__ == '__main__':
    unittest.main()        


