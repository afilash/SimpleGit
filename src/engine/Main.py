'''
Created on 14-Jul-2013

@author: AppleCart
'''
#import sys
from engine.treebuilder.epack import ElementPackage 


def CreateElementPack():
    element_package = ElementPackage()
    print element_package.Elements()
    element_package.New()
    print element_package.Elements()



if __name__ == '__main__':
    CreateElementPack()