# -*- coding: utf-8 -*-

"""
FILE : trace 

DESCRIPTION:   
                                                                                       
FUNCTION LIST:  
  1. class definition of Trace

REVISION:  
  
Ver  | yyyymmdd | Who    | Description of changes
1.00 | 20181105 | wxhao  | Create.

"""

import re
from req import srsDict

class STrace:

    # User ID diretory
    usrDict = None
    # Trace from SRS to User
    srsTrUsr = None
    # Trace from user to SRS
    usrTrSrs = None

    def __init__(self, f):
        self.usrDict = {}
        self.srsTrUsr = {}
        self.usrTrSrs = {}
        self.usrObj = f
    
    def hasThisFun(self):
        print("HAS THIS FUN")

    def getUsrDict(self):
        #for line in self.usrObj:
        for para in self.usrObj.paragraphs:
            line = para.text
            line = line.strip()
            matchFlag = re.match(r'USER_', line)
            if matchFlag:
                key = line

                # test if same ID is found
                if key in self.usrDict:
                    print("ERROR: Same USER ID: %s"   %(key))
                    assert key not in self.usrDict

                self.usrDict[key] = []
        
    def doTrace(self):
        for key in srsDict:
            # Trace from SRS to user
            usrList = srsDict[key].trace
            self.srsTrUsr[key] = usrList

            # Trace from user to SRS
            for ele in usrList:
                if ele not in self.usrDict:
                    if ele != 'DERIVED' and ele != 'Derived':
                        print("ERR: USER ITEM NOT FOUND IN RW DOC: %s"  %(ele))
                else:
                    if ele in self.usrTrSrs:
                        tmpList = self.usrTrSrs[ele]
                    else:
                        tmpList = []
                    tmpList.append(key)
                    self.usrTrSrs[ele] = tmpList

    def debug(self):

        covCnt = 0
        
        print("\n***********************************************************\n")
               
        for key in sorted(self.usrTrSrs.keys()):
            srsList = self.usrTrSrs[key]
            for it in srsList:
                print (key, "        ", it)

        print("\n***********************************************************\n")

        for key in sorted(self.srsTrUsr.keys()):
            ursList = self.srsTrUsr[key]
            for it in ursList:
                print (key, "        ", it)

        print("\n***********************************************************\n")

        for key in sorted(self.usrDict.keys()):
            if key in self.usrTrSrs:
                strHas = 'Y'
                covCnt = covCnt + 1
            else:
                strHas = 'N'
            print(key + "    " + strHas)

        print("\n***********************************************************\n")

        print("Coverage is: %.2f%%"  % (covCnt / len(self.usrDict) * 100))

        print("\n***********************************************************\n")                


















