
import unittest
import random

import sys
import os

from binary_search import BinarySearch

class TestBS(unittest.TestCase):

    def test_bs1(self):
        print ("test 1")
        arry_len = 300
        arry = [random.randint(0, arry_len*2) for _ in range(0,arry_len)]
        arry.sort() #nlogn	
        bs = BinarySearch(arry)
        f = bs.find(79)
        print ('found it',f)
        self.assertTrue(True)

    def test_bs2(self):
        print ("test 2")	
        arry = [7,12,13,16,22,52,55,56,60,61,62,66,73,78,91,99,100,101]	
        bs = BinarySearch(arry)
        f = bs.find(16)
        print ('found it',f)
        self.assertTrue(f)


    def test3(self):
        arry_len = 3000000
        arry = [random.randint(0, arry_len*2) for _ in range(0,arry_len)]
        arry.sort() #nlogn	
        bs = BinarySearch(arry)
        f = bs.find(arry[91])
        print ('found it',f)


    def test4(self):
        arry = []
        arry.sort() #nlogn	
        bs = BinarySearch(arry)
        f = bs.find(10)
        print ('found it',f)
        self.assertTrue(f)