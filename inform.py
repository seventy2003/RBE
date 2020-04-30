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

import uuid

from req import srsDict

errDict = {
    "other": "Other Warning.\n"
}

warnDict = {
    "nullItem": "Warning: Null Item.",
    "other": "Warning: Other warning."
}

class Inform:
    
    errList = None
    warnList = None

    def __init__(self):

        self.errList = {}
        self.warnList = {}

    def resetInform(self):
        self.errList = {}
        self.warnList = {}
    
    def appendErrItem(self, idV, infm):
        #self.errList.append(infm)
        self.errList[idV] = errDict[infm]

    def appendWarnItem(self, idV, infm):
        #self.warnList.append(infm)
        self.warnList[idV] = warnDict[infm]
    
    def checkAll(self):

        for key in srsDict:
            if srsDict[key].type == 'FUNC':
                '''
                print(srsDict[key].id, "    ", srsDict[key].dataIn, "    ",
                      srsDict[key].dataOut, "    ", srsDict[key].trace, "    ",
                      srsDict[key].verify)
                '''
                if srsDict[key].dataIn:
                    self.appendWarnItem(srsDict[key].id + " " + "dataIn", "nullItem")

                if srsDict[key].trace:
                    self.appendWarnItem(srsDict[key].id + " " + "trace", "nullItem")

            if srsDict[key].type == 'INTF':
                print(srsDict[key].id, "    ", srsDict[key].trace, "    ",
                      srsDict[key].verify)

        for key in self.warnList:
            print(key, "    ", self.warnList[key])






