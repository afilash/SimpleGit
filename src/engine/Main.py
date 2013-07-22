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
    print "checking for preservation added on cba9582437515e1b8e2fec8b25f9b3248a55d837"
    print "checking for preservation added on 3a7d6c8a31aedafb830daa2914bb0cbb90c0e392"



if __name__ == '__main__':
    CreateElementPack()