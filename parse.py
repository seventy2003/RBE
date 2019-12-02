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
from req import FuncReqFactory, IntfReqFactory
#from pState import StateInit


class PState:
    
    def lineParse(self, Parse):
        pass


class StateInit(PState):

    def __init__(self):
        pass

    def lineParse(self, pars):

        if (pars.matchId()):
            pars.setState(StateId())
            pars.parseLine()

class StateId(PState):

    def lineParse(self, pars):

        if (pars.matchId()):
            pars.procId()
        elif (pars.matchDisc()):
            pars.setState(StateDisc())
            pars.parseLine()
        else:
            pars.setState(StateExcp())
            pars.parseLine()

class StateDisc(PState):

    def lineParse(self, pars):
        
        if (pars.matchDisc()):
            pars.procDisc()
        elif (pars.matchInput()):
            pars.setState(StateInput())
            pars.parseLine()
        elif (pars.matchVerify()):
            pars.setState(StateVerify())
            pars.parseLine()
        elif (pars.matchId()):
            pars.setState(StateExcp())
            pars.parseLine()
        elif (pars.matchOutput()):
            pars.setState(StateExcp())
            pars.parseLine()
        # more state to add, todo
        else:
            pars.procDisc()            


class StateInput(PState):

    def lineParse(self, pars):

        if (pars.matchInput()):
            pars.procInput()
        elif (pars.matchOutput()):
            pars.setState(StateOutput())
            pars.parseLine()
        elif (pars.matchId()):
            pars.setState(StateExcp())
            pars.parseLine()
        # more state to add, todo
        else:
            pars.procInput()

class StateOutput(PState):

    def lineParse(self, pars):

        if (pars.matchOutput()):
            pars.procOutput()
        elif (pars.matchHandle()):
            pars.setState(StateHandle())
            pars.parseLine()
        elif (pars.matchId()):
            pars.setState(StateExcp())
            pars.parseLine()
        # more state to add, todo
        else:
            pars.procOutput()

class StateHandle(PState):

    def lineParse(self, pars):

        if (pars.matchPerfm()):
            pars.setState(StatePerfm())
            pars.procPerfm()
        elif (pars.matchId()):
            pars.setState(StateExcp())
            pars.parseLine()
        elif (pars.matchOutput()):
            pars.setState(StateExcp())
            pars.parseLine()
        # more state to add, todo
        else:
            pars.procHandle()

class StatePerfm(PState):

    def lineParse(self, pars):

        if (pars.matchVerify()):
            pars.setState(StateVerify())
            pars.parseLine()
        elif (pars.matchId()):
            pars.setState(StateExcp())
            pars.parseLine()
        # more state to add, todo
        else:
            pars.procPerfm()

class StateVerify(PState):

    def lineParse(self, pars):

        if (pars.matchVerify()):
            pars.procVerify()
        elif (pars.matchTrace()):
            pars.setState(StateTrace())
            pars.parseLine()
        else:
            pars.setState(StateExcp())
            pars.parseLine()


class StateTrace(PState):

    def lineParse(self, pars):

        if (pars.matchTrace()):
            pars.procTrace()
        elif (pars.matchId()):
            pars.setState(StateId())
            pars.parseLine()
        elif (pars.matchInput()):
            pars.setState(StateExcp())
            pars.parseLine()            
        # more state to add, todo
        else:
            pars.setState(StateNone())
            pars.parseLine()

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

class StateInterface(PState):
    
    def lineParse(self, pars):
        
        if (pars.matchInterface()):
            pars.procInterface()
        elif (pars.matchTrace()):
            pars.setState(StateTrace())
            pars.parseLine()

class StateExcp(PState):

    def lineParse(self, pars):
        pars.procExcp()

# no use? to delete, todo
class StateDone(PState):

    def lineParse(self, pars):

        if (pars.matchId()):
            pars.setState(StateId())
            pars.parseLine()

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

    def procId(self):

        # reset storeReq
        pos = self.line.find(self.cf.get("regular", "srsIdRgl"))
        self.line = self.line[pos:].strip()

        self.storeReq.resetReq(self.line)

    def procDisc(self):
        pass

    def procInput(self):

        #pos = line.find('：')
        mm = re.search('[：:]', self.line)
        if mm:
            pos = mm.start()
            line = self.line[pos + 1 :]
            line = line.strip()
            pos = line.find(' ')
            line = line[:pos]
        else:
            line = self.line.strip()
            pos = line.find(' ')
            line = line[:pos]          

        if line != '':
            self.storeReq.dataIn.append(line)
        self.storeReq.type = 'FUNC'

    def procOutput(self):

        mm = re.search('[：:]', self.line)
        if mm:
            pos = mm.start()
            line = self.line[pos + 1 :]
            line = line.strip()
            pos = line.find(' ')
            line = line[:pos]
        else:
            line = self.line.strip()
            pos = line.find(' ')
            line = line[:pos]                           

        if line != '':        
            self.storeReq.dataOut.append(line)

    def procHandle(self):
        pass

    def procPerfm(self):
        pass

    def procVerify(self):

        pos = re.search('[：:]', self.line).start()
        line = self.line[pos + 1 :]
        line = line.strip()
        
        self.storeReq.verify = line

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
        
        self.storeReq.trace = strip_line

        """
        requirement store
        """
        # todo, requirement classification
        if self.storeReq.type == 'FUNC':
            self.reqFact = FuncReqFactory()
        elif self.storeReq.type == 'INTF':
            self.reqFact = IntfReqFactory()

        # store storeReq
        #if self.storeReq.type == 'FUNC' or self.storeReq.type == 'INTF':
        if self.storeReq.type != '':
            self.reqFact.create()
            self.reqFact.concreteStore(self.storeReq)


    def procExcp(self):
        print("Format error.\n")
        raise UserWarning(self.line, )

    def setState(self, pst):
        self.pState = pst
    
    def setLine(self, aLine):

        self.line = aLine
    
    def parseLine(self):

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
            # if line == "ID: SRS_IF_iFp_Ctl":
            #     a = 100

            self.setLine(line)
            self.parseLine()

        self.state = 100

        #self.setState(StateDone())    
    




    def run(self, f):

        self.state = 0
        self.storeReq = TotalReq()

        # get pattern from conf file
        cf = configparser.ConfigParser()
        cf.read("smg.conf",encoding="utf-8-sig")

        #for line in f:
        for para in f.paragraphs:
            line = para.text

            # delete last char \n
            line = line.strip()

            # get pattern from conf file
            #inPatn = cf.get("regular", "srsIdLineRgl")

            # ID
            #if re.match(r'SRS_', line):
            if re.match(cf.get("regular", "srsIdLineRgl"), line):

                # create concrete requirement
                if self.storeReq.type == 'FUNC':
                    self.reqFact = FuncReqFactory()
                elif self.storeReq.type == 'INTF':
                    self.reqFact = IntfReqFactory()

                # store storeReq
                #if self.storeReq.type == 'FUNC' or self.storeReq.type == 'INTF':
                if self.storeReq.type != '':
                    self.reqFact.create()
                    self.reqFact.concreteStore(self.storeReq)
                
                # set parse state
                self.state = 1

                # reset storeReq
                pos = line.find(self.cf.get("regular", "srsIdRgl"))
                line = line[pos:].strip()

                self.storeReq.resetReq(line)

            # input data    
            #elif re.match(r'输入[：:]', line):
            elif re.match(cf.get("regular", "inDataRgl"), line):
                self.state = 2

                #pos = line.find('：')
                pos = re.search('[：:]', line).start()
                line = line[pos + 1 :]
                line = line.strip()
                pos = line.find(' ')
                line = line[:pos]

                if line != '':
                    self.storeReq.dataIn.append(line)
                self.storeReq.type = 'FUNC'

            # output data    
            #elif re.match(r'输出[：:]', line):
            elif re.match(cf.get("regular", "outDataRgl"), line):
                self.state = 3

                pos = re.search('[：:]', line).start()
                line = line[pos + 1 :]
                line = line.strip()
                pos = line.find(' ')
                line = line[:pos]                
                
                self.storeReq.dataOut.append(line)

            # verify method   
            #elif re.match(r'验证方法[：:]', line):
            elif re.match(cf.get("regular", "vefyMtdRgl"), line):
                self.state = 4

                pos = re.search('[：:]', line).start()
                line = line[pos + 1 :]
                line = line.strip()
                
                self.storeReq.verify = line

            # trace  
            #elif re.match(r'Traceability[：:]', line):
            elif re.match(cf.get("regular", "tracRgl"), line):
                self.state = 5

                pos = re.search('[：:]', line).start()
                line = line[pos + 1 :]
                line = line.strip()
                line = re.split('[,，]', line)

                # delete front and end space of every element
                strip_line = [ele.strip() for ele in line]
                
                self.storeReq.trace = strip_line

            #elif re.match(r'接口标识[：:]', line):
            elif re.match(cf.get("regular", "InterfaceRgl"), line):
                self.state = 6

                pos = re.search('[：:]', line).start()
                line = line[pos + 1 :]
                
                self.storeReq.verify = line
                self.storeReq.type = 'INTF'

            #elif re.match(r'异常处理[：:]', line):
            elif re.match(cf.get("regular", "HandleRgl"), line):
                self.state = 7
                
            #elif re.match(r'相关性能需求[：:]', line):
            elif re.match(cf.get("regular", "perfmRgl"), line):
                self.state = 8

            else:
                if self.state == 2:

                    line = line.strip()
                    pos = line.find(' ')
                    line = line[:pos]
                    
                    if line != '':
                        self.storeReq.dataIn.append(line)

                elif self.state == 3:

                    line = line.strip()
                    pos = line.find(' ')
                    line = line[:pos]                    

                    if line != '':
                        self.storeReq.dataOut.append(line)

        """
        store the last requirement
        """

        # create concrete requirement
        if self.storeReq.type == 'FUNC':
            self.reqFact = FuncReqFactory()
        elif self.storeReq.type == 'INTF':
            self.reqFact = IntfReqFactory()

        # store storeReq
        # if self.storeReq.type == 'FUNC' or self.storeReq.type == 'INTF':
        if self.storeReq.type != '':
            self.reqFact.create()
            self.reqFact.concreteStore(self.storeReq)

        # set parse state: parse done
        self.state = 100

        # reset storeReq
        self.storeReq.resetReq(line)









