'''
Created on 14-Jul-2013
@author: AppleCart
'''

import unittest
from engine.treebuilder.Impleme_package import package


class Test(unittest.TestCase):


    def testMakeTree(self):        
        self.assertEqual(str(package) , "<Object Package>" , "Success" )
        
    def testNewElement(self):        
        self.assertEqual(len(package) , 0 , "Success" )        
        self.assertEqual(package.new() , "" , "Success" )
        self.assertEqual(len(package) , 1 , "Success" )
        
        

if __name__ == "__main__":
    unittest.main()