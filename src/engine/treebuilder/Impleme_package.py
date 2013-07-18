'''
Created on 14-Jul-2013
@author: AppleCart
'''

from . import Impleme_element


class Package(object):
    
    _Elements = None
    _count = 0
    
    def __init__(self ):
        self._Elements = []
        
    def __repr__(self):
        return "<Object Package>"
    
    def __len__(self):
        return len(self._Elements)
    
    def new(self):
        cur = self._count
        new = Impleme_element.Element(elementid = cur)
        self._count += 1
        self._Elements.append(new)
        return self._Elements[len(self._Elements) -1].elementname()
    
    def delete(self , ID ):
        if not isinstance(ID, int):
            return "Type Error"
        
        idsearch = [indx  for indx,  members in enumerate(self._Elements) if members.elementid() == int(ID)]
        if not idsearch :
            return "No such element"
        del self._Elements[idsearch[0]]

        print [(indx , members.elementid()) for indx,  members in enumerate(self._Elements)]
        return "Deleted member " + str(ID)


package = Package()
