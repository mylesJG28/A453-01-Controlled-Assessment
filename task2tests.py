import unittest
import TaskTwo as t2

class TestSequenceFunctions(unittest.TestCase):
    def setup(self):
        t2.getAddresses()
    
    def test1(self):
        assert(t2.addresses[0][0] =='Jackson')#test 1 fails - address book not imported from file
        
    def test2(self):
        '''
        this test checks that Jackson is put into the list of surnames
        '''
        t2.getSrnames()
        assert('Jackson' in t2.surnames)
        
if __name__ == '__main__':
    unittest.main()