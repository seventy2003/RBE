# -*- coding: utf-8 -*-

"""
FILE : pState 

DESCRIPTION: 
  State transition of SRS attribute parsing.
  NOTE: THIS FILE IS GENERATED BY PROGRAM, DO NOT MODIFY THIS FILE.
                                                                                       
FUNCTION LIST:  
  1. State transition of SRS attribute parsing.

REVISION:  
  
Ver  | yyyymmdd | Who    | Description of changes
1.00 | #GENDAY# | RBE    | #GENDAY# #GENTIME# create by tmlGen. 

"""


class PState:
    
    def lineParse(self, Parse):
        pass


class StateInit(PState):

    def __init__(self):
        pass

#lineParse#

"""
    def lineParse(self, pars):

        if (pars.matchId()):
            pars.setState(StateId())
            pars.parseLine()
"""

#Id#
          
#Disc#             

#Input#

#Output#

#Handle#

#Perfm#   

#Verify#

#Trace#

#Interface#

#Abcdefg#

#None#

"""
class StateNone(PState):

    def lineParse(self, pars):

        if (pars.matchId()):
            pars.setState(StateId())
            pars.parseLine()
        elif (pars.matchInput()):
            pars.setState(StateExcp())
            pars.parseLine()            
        # more state to add, todo
        #else:
            #pars.setState(StateNone())
            #pars.parseLine()
"""


class StateExcp(PState):

    def lineParse(self, pars):
        pars.procExcp()
