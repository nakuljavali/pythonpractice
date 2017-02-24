import unittest
from merge import mergesort

class TestSorts(unittest.TestCase):
        def test_merge1(self):
            ret = mergesort([8,5,1,2,4])
            self.assertEqual(ret, [1,2,4,5,8])

        def test_merge2(self):
            ret = mergesort([0,10,1,1])
            self.assertEqual(ret, [0,1,1,10])

if __name__ == '__main__':
    unittest.main()
