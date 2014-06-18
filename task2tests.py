import unittest
import TaskTwo as t2

class TestSequenceFunctions(unittest.TestCase):
    def setup(self):
        t2.getAddresses()
    
    def test1(self):
        assert(t2.addresses[0][0] =='Jackson')#test 1 fails - address book not imported from file
        
if __name__ == '__main__':
    unittest.main()