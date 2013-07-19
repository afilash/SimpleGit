'''
Created on 14-Jul-2013

@author: AppleCart
'''
from treebuilder.Impleme_package import package

def CreateElementPack():
    print [  package.new() for dummy_i in range(6)]
    print len( package )
    print package.delete(elementId=3)
    print package.delete(elementId=1)
    



if __name__ == '__main__':
    CreateElementPack()