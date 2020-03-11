# -*- coding: utf-8 -*-

"""
FILE : inform 

DESCRIPTION:   
                                                                                       
FUNCTION LIST:  
  1. module of information of error and warning

REVISION:  
  
Ver  | yyyymmdd | Who    | Description of changes
1.00 | 20200311 | wxhao  | Create.

"""

class Inform:
    errList = None
    warnList = None

    def __init__(self):

        self.errList = []
        self.warnList = []

    def resetInform(self):
        self.errList = []
        self.warnList = []
    
    def appendErr(self, infm):
        self.errList.append(infm)

    def appendWarn(self, infm):
        self.warnList.append(infm)


