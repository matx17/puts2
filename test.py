import main 
import unittest

class MyTestCase(unittest.TestCase):

        def setUp(self):
            main.app.testing = True
            self.app = main.app.test_client()

        def test_list_sumint(self):
            response = self.app.get('/add?A=3&B=7')
            self.assertMultiLineEqual( '10' , response.data)
        def test_addfloat(self):
            rv =  self.app.get('/add?A=3.3&B=7.3')
            self.assertMultiLineEqual('10.6', rv.data)
        def test_addfrac(self):
            rv =  self.app.get('/add?A=5/3&B=3/3')
            self.assertMultiLineEqual('2.66666666667', rv.data)
        def test_addneg(self):
            rv =  self.app.get('/add?A=4.3&B=-2.1')
            self.assertMultiLineEqual('2.2', rv.data)

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

