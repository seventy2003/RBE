# -*- coding: utf-8 -*-

"""
FILE : parse 

DESCRIPTION:   
                                                                                       
FUNCTION LIST:  
  1. class definition of Parse

REVISION:  
  
Ver  | yyyymmdd | Who    | Description of changes
1.00 | 20181105 | wxhao  | Create.

"""

import re
import configparser

from req import Req, TotalReq, ValidFuncReq, IntfReq
from req import *
from pState import StateInit
from warnWords import *



class Parse:

    """
      parse state
        1: SRS ID, for invalid func req
        10: SRS ID, contains '_Safe', for safe req
        11: SRS ID, contains '_Perf', for performance req
        12: SRS ID, contains '_Res', for resource req 
        2: input, for valid func req
        3: output, for valid func req    
        4: interface ID, for interface req
        5: Traceability
        100: parse done
    """
    state = 0
    pState = StateInit()
    cf = None

    #funcFact = FuncReqFactory()
    #intfFact = IntfReqFactory()
    reqFact = None
    line = ''
    
    def __init__(self):
        self.storeReq = TotalReq()
        # read config file
        self.cf = configparser.ConfigParser()
        self.cf.read("smg.conf",encoding="utf-8-sig")
    
    def matchId(self):

        #if re.match(r'SRS_', self.line):
        if re.match(self.cf.get("regular", "srsIdLineRgl"), self.line):
            return True
        else:
            return False

    def matchDisc(self):
        if re.match(self.cf.get("regular", "DiscRgl"), self.line):
            return True
        else:
            return False

    def matchInput(self):

        #if re.match(r'输入[：:]', self.line):
        if re.match(self.cf.get("regular", "inDataRgl"), self.line):
            return True
        else:
            return False

    def matchOutput(self):

        #if re.match(r'输出[：:]', self.line):
        if re.match(self.cf.get("regular", "outDataRgl"), self.line):
            return True
        else:
            return False

    def matchVerify(self):

        #if re.match(r'验证方法[：:]', self.line):
        if re.match(self.cf.get("regular", "vefyMtdRgl"), self.line):
            return True
        else:
            return False

    def matchTrace(self):

        #if re.match(r'Traceability[：:]', self.line):
        if re.match(self.cf.get("regular", "tracRgl"), self.line):
            return True
        else:
            return False

    def matchInterface(self):

        #if re.match(r'接口标识[：:]', self.line):
        if re.match(self.cf.get("regular", "infRgl"), self.line):
            return True
        else:
            return False

    def matchHandle(self):

        #if re.match(r'异常处理[：:]', self.line):
        if re.match(self.cf.get("regular", "HandleRgl"), self.line):
            return True
        else:
            return False
    
    def matchPerfm(self):

        #if re.match(r'异常处理[：:]', self.line):
        if re.match(self.cf.get("regular", "PerfmRgl"), self.line):
            return True
        else:
            return False

    def resetState(self):
        self.storeReq.resetReq()

    def endState(self):
        
        """
        requirement store
        """
        # todo, requirement classification
        if self.storeReq.type == 'FUNC':
            self.reqFact = FuncReqFactory()
        elif self.storeReq.type == 'INTF':
            self.reqFact = IntfReqFactory()
        elif self.storeReq.type == 'SAFE':
            self.reqFact = SafeReqFactory()
        elif self.storeReq.type == 'PERF':
            self.reqFact = PerfReqFactory()

        # store storeReq
        #if self.storeReq.type == 'FUNC' or self.storeReq.type == 'INTF':
        if self.storeReq.type != '':
            self.reqFact.create()
            self.reqFact.concreteStore(self.storeReq)
    
    def procId(self):

        #self.storeReq.resetReq(self.line)
        
        # reset storeReq
        pos = self.line.find(self.cf.get("regular", "srsIdRgl"))

        # error report, if ID flag not found in ID line 
        if pos == -1:
            print("ERR: NOT FOUND ID REGULATION.  %s"   %(self.line))
            return

        self.line = self.line[pos:].strip()

        # ID check of valid characters
        patn = r'^[a-zA-Z0-9_]+$'
        res = re.search(patn, self.line)
        if res == None:
            print("WARNNING: INVALID CHARACTERS IN ID.  %s"   %(self.line))

        self.storeReq.id = self.line

        searchRelt = re.search(self.cf.get("nonFuncId", "safReqIdRel"), self.line)
        if searchRelt != None:
            self.storeReq.type = 'SAFE'
        else:
            searchRelt = re.search(self.cf.get("nonFuncId", "prfReqIdRel"), self.line)
            if searchRelt != None:
                self.storeReq.type = 'PERF'
            else:
                self.storeReq.type = 'FUNC'
        # pos = self.line.find('_SAF')
        # if pos != -1:
        #     self.storeReq.type = 'SAFE'
        # else:
        #     pos = self.line.find('_PRF')
        #     if pos != -1:
        #         self.storeReq.type = 'PERF'
        #     else:
        #         self.storeReq.type = 'FUNC'

    def procDisc(self):
        pass

    def procInput(self):

        #pos = line.find('：')
        mm = re.search('[：:]', self.line)
        if mm:
            pos = mm.start()
            line = self.line[pos + 1 :]
            line = line.strip()

            # check NULL attribute
            # if re.match(r'^[\s]+$', line) or line == '':
            #     print("WARNNING: NULL ATTRIBUTE.  %s"   %(self.storeReq.id + " Input"))

            # pos = line.find(' ')
            # if pos != -1:
            #     line = line[:pos]
        else:
            line = self.line.strip()

        pos = line.find(' ')
        if pos != -1:
            line = line[:pos]

        patn = r'^[a-zA-Z0-9_.]+$'
        res = re.search(patn, line)
        
        if line != '' and res != None:        
            self.storeReq.dataIn.append(line)
        elif line == '':
            print("WARNNING: NULL ATTRIBUTE.  %s"   %(self.storeReq.id + " Input"))

        #self.storeReq.type = 'FUNC'

    def procOutput(self):

        mm = re.search('[：:]', self.line)
        if mm:
            pos = mm.start()
            line = self.line[pos + 1 :]
            line = line.strip()

            # check NULL attribute
            # if re.match(r'^[\s]+$', line) or line == '':
            #     print("WARNNING: NULL ATTRIBUTE.  %s"   %(self.storeReq.id + " Output"))

        else:
            line = self.line.strip()
        
        pos = line.find(' ')
        if pos != -1:
            line = line[:pos]                           

        patn = r'^[a-zA-Z0-9_.]+$'
        res = re.search(patn, line)
        
        if line != '' and res != None:        
            self.storeReq.dataOut.append(line)
        elif line == '':
            print("WARNNING: NULL ATTRIBUTE.  %s"   %(self.storeReq.id + " Output"))

    def procHandle(self):

        mm = re.search('[：:]', self.line)
        if mm:
            pos = mm.start()
            line = self.line[pos + 1 :]
            line = line.strip()
        else:
            line = self.line.strip()
        
        # if line == '':
        #     print("WARNNING: NULL ATTRIBUTE.  %s"   %(self.storeReq.id + " Handle"))

    def procPerfm(self):
        
        mm = re.search('[：:]', self.line)
        if mm:
            pos = mm.start()
            line = self.line[pos + 1 :]
            line = line.strip()
        else:
            line = self.line.strip()
        
        # if line == '':
        #     print("WARNNING: NULL ATTRIBUTE.  %s"   %(self.storeReq.id + " Perfm"))

    def procVerify(self):

        pos = re.search('[：:]', self.line).start()
        line = self.line[pos + 1 :]
        line = line.strip()
        
        if line != '':
            self.storeReq.verify = line
        else:
            print("WARNNING: NULL ATTRIBUTE.  %s"   %(self.storeReq.id + " Verify"))

    def procInterface(self):

        pos = re.search('[：:]', self.line).start()
        line = self.line[pos + 1 :]
        
        self.storeReq.verify = line
        self.storeReq.type = 'INTF'

    def procTrace(self):

        """
        proc trace
        """
        pos = re.search('[：:]', self.line).start()
        line = self.line[pos + 1 :]
        line = line.strip()
        line = re.split('[,，]', line)

        # delete front and end space of every element
        strip_line = [ele.strip() for ele in line]
        
        # if strip_line:
        #     # do nothing
        #     pass
        # else:
        if '' in strip_line:
            print("WARNNING: NULL ATTRIBUTE.  %s"   %(self.storeReq.id + " Trace"))
        
        self.storeReq.trace = strip_line


    def procExcp(self):
        print("Format error.\n")
        raise UserWarning(self.line, self.storeReq.id)

    def setState(self, pst):
        self.pState = pst
    
    def setLine(self, aLine):

        self.line = aLine
    
    def parseLine(self):

        # warning words check
        if self.cf.get("enSw", "enSwWordsWarn") == '1':
            warnWdsPars(self.line)

        self.pState.lineParse(self)
    
    def doParse(self, f):

        #to avoid trace before multiple parse
        #self.state = 0

        self.storeReq = TotalReq()

        #for line in f:
        # todo
        for para in f.paragraphs:

            line = para.text

            # delete last char \n
            line = line.strip()

            # for debug
            #print("****\n")
            #print(type(self.pState))
            #if line == "ID:  SRS_Safe_OxMng_SelSysWorkMode_IsSysBlt":
            #    a = 100

            self.setLine(line)
            self.parseLine()

        self.state = 100

        #self.setState(StateDone())    
    







