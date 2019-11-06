import main 
import unittest

class MyTestCase(unittest.TestCase):

        def setUp(self):
            main.app.testing = True
            self.app = main.app.test_client()

        def test_subint(self):
            rv =  self.app.get('/sub?A=3&B=7')
            self.assertMultiLineEqual('-4', rv.data)
        def test_subfloat(self):
            rv =  self.app.get('/sub?A=3.3&B=7.3')
            self.assertMultiLineEqual('-4.0', rv.data)
        def test_subfrac(self):
            rv =  self.app.get('/sub?A=5/3&B=3/3')
            self.assertMultiLineEqual('0.666666666667', rv.data)
        def test_subneg(self):
            rv =  self.app.get('/sub?A=4.3&B=-2.1')
            self.assertMultiLineEqual('6.4', rv.data)

      
        
if __name__ == '__main__':
    unittest.main()      
