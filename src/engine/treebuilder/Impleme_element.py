'''
Created on 14-Jul-2013
@author: AppleCart
'''


class Element(object):
    '''
    classdocs:
    Contains Constructors for creating METADATA elements and variables
    '''
    
    #===========================================================================
    #            INITIALIZATION
    #===========================================================================
    def __init__(self , elementid=0, elementname = "" , enabled = False , actionlist  = [] ):
        '''
        Constructor:
        METADATA elements
        '''
        self._elementid = elementid
        self._elementname = elementname
        self._enabled = enabled
        self._actionlist = actionlist        
        
        
    #===========================================================================
    #        Getter and Setter : elementid
    #===========================================================================
    def setelementid(self, elementid):
        self._elementid = elementid
        
    def elementid(self):
        return self._elementid   
               
    #===========================================================================
    #        Getter and Setter : elementname
    #===========================================================================
    def setelementname(self, elementname):
        self._elementname = elementname
        
    def elementname(self):
        return self._elementname
    
    #===========================================================================
    #        Getter and Setter : enabled
    #===========================================================================
    def setenabled(self, enabled):
        self._enabled = enabled
        
    def enabled(self):
        return self._enabled   
             
    #===========================================================================
    #        Getter and Setter : actionlist
    #===========================================================================
    def setactionlist(self, actionlist):
        self._elementid = actionlist
        
    def actionlist(self):
        return self._actionlist
             