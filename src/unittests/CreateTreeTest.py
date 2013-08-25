'''
Created on 14-Jul-2013
@author: AppleCart
'''

import unittest
from engine.treebuilder.Impleme_package import package
from engine.treebuilder import utilities



class Test(unittest.TestCase):


    def test_MakeTree(self):        
        self.assertEqual(str(package) , "<Object Package>" , "Success")
        
    def test_NewElement(self):        
        self.assertEqual(len(package) , 0 , "Success")        
        self.assertEqual(package.new() , "" , "Success")
        self.assertEqual(len(package) , 1 , "Success")
        
    def test_UtilsRandomnum(self):
        seqln = 5
        rseq = [ utilities.randseq(seqln) for dummy_i in range(10000) ]             
        tseq = utilities.randseq(seqln)
        msg = "Random word '" + str(tseq) + "' repeated."
        self.assertNotEqual(tseq in rseq , True , msg)
        
    def test_hashtest(self):
        seqln = 5
        rseq = [ utilities.genhash(utilities.randseq(seqln) , seqln) for dummy_i in range(10000) ]
        tseq = utilities.genhash(utilities.randseq(seqln) , seqln)
        msg = "Random word '" + str(tseq) + "' repeated."
        self.assertNotEqual(tseq in rseq , True , msg)
        
    def test_ispushworking(self):
        print "OK"
        

        

if __name__ == "__main__":
    unittest.main()
