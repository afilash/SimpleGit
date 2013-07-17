'''
Created on 14-Jul-2013
@author: AppleCart
'''
import sys
import unittest
from engine.treebuilder.epack import ElementPackage 


class Test(unittest.TestCase):


    def testMakeTree(self):
        element_package = ElementPackage()
        print "element_package._count",element_package._count
        element_package.New()
        print "element_package._count",element_package._count
         
        


if __name__ == "__main__":
    unittest.main()