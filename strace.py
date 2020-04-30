# -*- coding: utf-8 -*-

"""
FILE : strace 

DESCRIPTION:   
                                                                                       
FUNCTION LIST:  
  1. class definition of STrace

REVISION:  
  
Ver  | yyyymmdd | Who    | Description of changes
1.00 | 20181105 | wxhao  | Create.
1.00 | 20200429 | wxhao  | Add trace of Srs and Sdd.

"""

import re
from req import srsDict

import configparser

# for debug
import csv 

class STrace:

    # User ID diretory
    usrDict = None
    # Trace from SRS to User
    srsTrUsr = None
    # Trace from user to SRS
    usrTrSrs = None

    # SDD id and trace list
    sddDict = None
    srsTrSdd = None
    sddTrSrs = None

    cf = None

    def __init__(self, f):
        self.inFileObj = f
        
        self.usrDict = {}
        self.srsTrUsr = {}
        self.usrTrSrs = {}

        self.sddDict = {}
        self.sddTrSrs = {}
        self.srsTrSdd = {}

        # read config file
        self.cf = configparser.ConfigParser()
        self.cf.read("smg.conf",encoding="utf-8-sig")

    def getUsrDict(self):
        #for line in self.inFileObj:
        for para in self.inFileObj.paragraphs:
            line = para.text
            line = line.strip()
            # search user ID
            matchFlag = re.match(self.cf.get("usrFile", "usrIdLineRgl"), line)
            if matchFlag:
                key = line

                # test if same ID is found
                if key in self.usrDict:
                    print("ERR: Same USER ID: %s"   %(key))
                    # to continue to run? todo
                    assert key not in self.usrDict

                self.usrDict[key] = []
        
    def doTraceSrs2Usr(self):
        for key in srsDict:
            # Trace from SRS to user
            usrList = srsDict[key].trace
            self.srsTrUsr[key] = usrList

            # error report for NULL traceability
            if '' in usrList:
                print("ERR: NULL TRACE.  ", key)
                continue

            # Trace from user to SRS
            # for ele in usrList:
            #     if ele not in self.usrDict:
            #         if ele != 'DERIVED' and ele != 'Derived':
            #             print("ERR: USER ITEM NOT FOUND IN RW DOC: %s"  %(ele))
            #     else:
            #         if ele in self.usrTrSrs:
            #             tmpList = self.usrTrSrs[ele]
            #         else:
            #             tmpList = []
            #         tmpList.append(key)
            #         self.usrTrSrs[ele] = tmpList

            for ele in usrList:
                tmpList = []
                # if ele not in self.usrDict:
                #     if ele != 'DERIVED' and ele != 'Derived':
                #         print("ERR: USER ITEM NOT FOUND IN RW DOC: %s"  %(ele))
                # else:
                #     if ele in self.usrTrSrs:
                #         tmpList = self.usrTrSrs[ele]
                if ele in self.usrTrSrs:
                    tmpList = self.usrTrSrs[ele]
                else:
                    if ele not in self.usrDict:
                        if ele != 'DERIVED' and ele != 'Derived':
                            print("ERR: USER ITEM NOT FOUND IN RW DOC: %s"  %(ele))
                        
                tmpList.append(key)
                self.usrTrSrs[ele] = tmpList


    def getSddTraceList(self):
        #for line in self.inFileObj:
        for para in self.inFileObj.paragraphs:
            line = para.text

            # for debug, to delete, todo
            #print(line)

            line = line.strip()

            # match sdd ID for sddDict
            matchFlag = re.match(self.cf.get("sddFile", "sddIdLineRgl"), line)
            if matchFlag:
                pos = line.find(self.cf.get("sddFile", "sddIdRgl"))
                
                if pos == -1:
                    print("ERR: NOT FOUND ID REGULATION.  %s"   %(line))
                    continue
                else:
                    line = line[pos:].strip()
                    key = line

                # test if same ID is found
                if key in self.sddDict:
                    print("ERR: Same SDD ID: %s"   %(key))
                    # to continue to run? todo
                    assert key not in self.sddDict

                # for debug, to delete, todo
                if key == 'F':
                    ccc = 200


                self.sddDict[key] = []

            # match Tracebility for trace list
            matchFlag = re.match(self.cf.get("sddFile", "sddTrSrsRgl"), line)
            if matchFlag:
                pos = re.search('[：:]', line).start()
                line = line[pos + 1 :]
                line = line.strip()
                line = re.split('[,，]', line)

                # delete front and end space of every element
                strip_line = [ele.strip() for ele in line]
                
                # self.sddTrSrs[key] = []
                
                # if '' in strip_line:
                #     print("ERR: NULL TRACE.  ", key)
                # else:
                #     self.sddTrSrs[key] = strip_line
                self.sddTrSrs[key] = strip_line

        
    def doTraceSdd2Srs(self):
        for key in self.sddDict:
            # Trace from Sdd to Srs
            srsList = self.sddTrSrs[key]
            self.sddTrSrs[key] = srsList

            # error report for NULL traceability
            if '' in srsList:
                print("ERR: NULL TRACE.  ", key)
                continue
            
            # Trace from Srs to Sdd
            for ele in srsList:
                # if ele not in srsDict:
                #     if ele != 'DERIVED' and ele != 'Derived':
                #         print("ERR: SRS ITEM NOT FOUND IN SRS DOC: %s"  %(ele))
                # else:
                #     if ele in self.srsTrSdd:
                #         tmpList = self.srsTrSdd[ele]
                #     else:
                #         tmpList = []
                #     tmpList.append(key)
                #     self.srsTrSdd[ele] = tmpList

                tmpList = []
                if ele in self.srsTrSdd:
                    tmpList = self.srsTrSdd[ele]
                else:
                    if ele not in srsDict:
                        if ele != 'DERIVED' and ele != 'Derived':
                            print("ERR: SRS ITEM NOT FOUND IN SRS DOC: %s"  %(ele))                        
                
                tmpList.append(key)
                self.srsTrSdd[ele] = tmpList


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

        # generate output file of U2R
        # must add newline, or there will be many null line in csv
        f = open('../output/straceU2R.csv','w', newline="")


        # todo for: a bytes-like object is required, not 'str'
        '''
        csvWriter = csv.writer(f)
        for k,v in self.usrTrSrs.items():
            csvWriter.writerow([k,v])
        f.close()
        '''   
        csvWriter = csv.writer(f)
        for k in self.usrTrSrs:
            if self.usrTrSrs[k]:
                for ele in self.usrTrSrs[k]:
                    csvWriter.writerow([k,ele])
        f.close()

        # generate output file of R2U
        f = open('../output/straceR2U.csv','w', newline="")

        csvWriter = csv.writer(f)
        for k in self.srsTrUsr:
            if self.srsTrUsr[k]:
                for ele in self.srsTrUsr[k]:
                    csvWriter.writerow([k,ele])

        f.close()

    def sddTrOutput(self):
        # todo
        covCnt = 0
        
        print("\n***********************************************************\n")
               
        for key in sorted(self.srsTrSdd.keys()):
            sddList = self.srsTrSdd[key]
            for it in sddList:
                print (key, "        ", it)

        print("\n***********************************************************\n")

        for key in sorted(self.sddTrSrs.keys()):
            ursList = self.sddTrSrs[key]
            for it in ursList:
                print (key, "        ", it)

        print("\n***********************************************************\n")

        for key in sorted(srsDict.keys()):
            if key in self.srsTrSdd:
                strHas = 'Y'
                covCnt = covCnt + 1
            else:
                strHas = 'N'
            print(key + "    " + strHas)

        print("\n***********************************************************\n")

        print("Coverage is: %.2f%%"  % (covCnt / len(srsDict) * 100))

        print("\n***********************************************************\n")    

        # generate output file of R2D
        # must add newline, or there will be many null line in csv
        f = open('../output/straceR2D.csv','w', newline="")

        # todo for: a bytes-like object is required, not 'str'
        '''
        csvWriter = csv.writer(f)
        for k,v in self.usrTrSrs.items():
            csvWriter.writerow([k,v])
        f.close()
        '''   
        csvWriter = csv.writer(f)
        for k in self.srsTrSdd:
            if self.srsTrSdd[k]:
                for ele in self.srsTrSdd[k]:
                    csvWriter.writerow([k,ele])
        f.close()

        # generate output file of D2R
        f = open('../output/straceD2R.csv','w', newline="")

        csvWriter = csv.writer(f)
        for k in self.sddTrSrs:
            if self.sddTrSrs[k]:
                for ele in self.sddTrSrs[k]:
                    csvWriter.writerow([k,ele])

        f.close()
    
    def tClear(self):

        srsDict.clear()

        self.usrDict.clear()
        self.srsTrUsr.clear()
        self.usrTrSrs.clear()

        self.sddDict.clear()
        self.sddTrSrs.clear()
        self.srsTrSdd.clear()



















