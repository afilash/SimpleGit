'''
Created on 14-Jul-2013

@author: AppleCart
'''
from treebuilder.Impleme_package import package

def CreateElementPack():
    print [  package.new() for dummy_i in range(4)]
    print len(package)



if __name__ == '__main__':
    CreateElementPack()