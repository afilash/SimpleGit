'''
Created on 14-Jul-2013
@author: AppleCart
'''


class Element():
    '''
    classdocs:
    Contains Constructors for creating METADATA elements and variables
    '''
    
    #===========================================================================
    #            INIT
    #===========================================================================
    def __init__(self , elementid=0, pointer = 0 , color = None , indcolor = False , colorlist  = [] , action = "" , revert = []):
        '''
        Constructor:
        METADATA elements
        '''
        self._elementid = elementid
        self._pointer = pointer
        self._color = color
        self._indcolor = indcolor
        self._colorlist = colorlist
        self._action = action
        self._revert = revert
        
        
        
    #===========================================================================
    #        Getter and Setter : elementid
    #===========================================================================
    def setelementid(self, elementid):
        self._elementid = elementid
        
    def elementid(self):
        return self._elementid   
               
    #===========================================================================
    #        Getter and Setter : pointer
    #===========================================================================
    def setpointer(self, pointer):
        self._pointer = pointer
        
    def pointer(self):
        return self._pointer
             
    #===========================================================================
    #        Getter and Setter : color
    #===========================================================================
    def setcolor(self, color):
        self._color = color
        
    def color(self):
        return self._color   
             
    #===========================================================================
    #        Getter and Setter : indcolor
    #===========================================================================
    def setindcolor(self, indcolor):
        self._indcolor = indcolor
        
    def indcolor(self):
        return self._indcolor   
             
    #===========================================================================
    #        Getter and Setter : colorlist
    #===========================================================================
    def setcolorlist(self, colorlist):
        self._elementid = colorlist
        
    def colorlist(self):
        return self._colorlist
             
    #===========================================================================
    #        Getter and Setter : action
    #===========================================================================
    def setaction(self, action):
        self._elementid = action
        
    def action(self):
        return self._action
             
    #===========================================================================
    #        Getter and Setter : revert
    #===========================================================================
    def setrevert(self, revert):
        self._elementid = revert
        
    def revert(self):
        return self._revert 
        