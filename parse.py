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

from req import Req, TotalReq, ValidFuncReq, IntfReq
from req import FuncReqFactory, IntfReqFactory

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

    #funcFact = FuncReqFactory()
    #intfFact = IntfReqFactory()
    reqFact = None
    
    def __init__(self):
        self.storeReq = TotalReq()
    
    def run(self, f):

        self.state = 0
        self.storeReq = TotalReq()

        #for line in f:
        for para in f.paragraphs:
            line = para.text

            # delete last char \n
            line = line.strip()

            # ID
            if re.match(r'SRS_', line):

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
                self.storeReq.resetReq(line)

            # input data    
            elif re.match(r'输入[：:]', line):
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
            elif re.match(r'输出[：:]', line):
                self.state = 3

                pos = re.search('[：:]', line).start()
                line = line[pos + 1 :]
                line = line.strip()
                pos = line.find(' ')
                line = line[:pos]                
                
                self.storeReq.dataOut.append(line)

            # verify method   
            elif re.match(r'验证方法[：:]', line):
                self.state = 4

                pos = re.search('[：:]', line).start()
                line = line[pos + 1 :]
                line = line.strip()
                
                self.storeReq.verify = line

            # trace  
            elif re.match(r'Traceability[：:]', line):
                self.state = 5

                pos = re.search('[：:]', line).start()
                line = line[pos + 1 :]
                line = line.strip()
                line = re.split('[,，]', line)

                # delete front and end space of every element
                strip_line = [ele.strip() for ele in line]
                
                self.storeReq.trace = strip_line

            elif re.match(r'接口标识[：:]', line):
                self.state = 6

                pos = re.search('[：:]', line).start()
                line = line[pos + 1 :]
                
                self.storeReq.verify = line
                self.storeReq.type = 'INTF'

            elif re.match(r'异常处理[：:]', line):
                self.state = 7
                
            elif re.match(r'相关性能需求[：:]', line):
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















