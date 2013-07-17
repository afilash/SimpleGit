'''
Created on 14-Jul-2013
@author: AppleCart
'''

from engine.treebuilder.elm import Element

class ElementPackage():
    
    _Elements = None
    _count = 0
    
    def __init__(self ):
        self._Elements = []
    
    def Elements(self):
        return self._Elements
    
    def New(self):
        cur = self._count
        new = Element(elementid = cur)
        self._count += 1
        self._Elements.append(new)
        return self._Elements[len(self._Elements) -1]
    
    def Delete(self , ID ):
        
#        idsearch = [ members.elementid() for members in self._Elements]
#        if ID not in idsearch  :
#            return "No such element"

        try:
            int(ID)
        except:
            return "Type Error"
        
        print [(indx , members.elementid()) for indx,  members in enumerate(self._Elements)]
        idsearch = [indx  for indx,  members in enumerate(self._Elements) if members.elementid() == int(ID)]
        if not idsearch :
            return "No such element"
        del self._Elements[idsearch[0]]

        print [(indx , members.elementid()) for indx,  members in enumerate(self._Elements)]
        return "Deleted member " + str(ID)
        
