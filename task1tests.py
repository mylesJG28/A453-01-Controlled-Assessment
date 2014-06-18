import unittest
import TaskOne as t1

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        t1.rates = [1,2,3,4]

    def test1(self):
        assert (t1.rates ==[1,2,3,4]) #test 1 fails - test setup does not work.
        
    def test3 (self):
        print(t1.getVal(0,1,10))
        assert (t1.getVal(0,1,10)==20.0)#test2 works - pound to Dollar conversion fails
        assert (t1.getVal(0,2,10)==30.0)#test2 works - pound to Euro conversion fails
        assert (t1.getVal(0,3,10)==40.0)#test2 works - pound to Yen conversion fails

if __name__ == "__main__":
    unittest.main()
