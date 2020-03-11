# -*- coding: utf-8 -*-

"""
FILE : req 

DESCRIPTION:   
                                                                                       
FUNCTION LIST:  
1. definition of class Req

REVISION:  
  
Ver  | yyyymmdd | Who    | Description of changes
1.00 | 20181105 | wxhao  | Create.

"""

srsDict = {}

class Req:

    id = ''
    type = ''
    valid = 0
    state = 0
    grade = 0
    trace = []

    def __init__(self):
        pass

class FuncReq(Req):
    pass

class NoFuncReq(Req):
    pass

class ValidFuncReq(FuncReq):

    verify = ''
    dataIn = []
    dataOut = []

class InvalidFuncReq(FuncReq):
    pass

class PerfReq(Req):
    verify = ''
    dataIn = []
    dataOut = []

class SafeReq(Req):
    verify = ''
    dataIn = []
    dataOut = []

class IntfReq(Req):

    intfId = ''
    #trace = []

class TotalReq(ValidFuncReq, IntfReq, PerfReq, SafeReq):

    def resetReq(self):
        self.id = ''
        self.type = 'NONFUNC'
        self.valid = ''
        self.state = 0
        self.grade = 0
        self.dataIn = []
        self.dataOut = []
        self.verify = ''
        self.trace = []

"""
class definition of Requirement factory
"""

class ReqFactory:

    def __init__(self):
        self.req = None

    def create(self):
        pass

    def store(self):
        self.req.concreteStore(self.req)

    def concreteStore(self, reqP):
        pass
    

class FuncReqFactory(ReqFactory):

    def create(self):
        self.req = ValidFuncReq()

    def concreteStore(self, reqP):
        self.req.id = reqP.id
        self.req.dataIn = reqP.dataIn
        self.req.dataOut = reqP.dataOut        
        self.req.type = 'FUNC'
        self.req.trace = reqP.trace
        self.req.verify = reqP.verify

        if self.req.id in srsDict:
            print("Same ID found.")
            print(self.req.id)
            assert self.req.id not in srsDict
        
        srsDict[self.req.id] = self.req

class PerfReqFactory(ReqFactory):

    def create(self):
        self.req = PerfReq()

    def concreteStore(self, reqP):
        self.req.id = reqP.id      
        self.req.type = 'PERF'
        self.req.trace = reqP.trace
        self.req.verify = reqP.verify

        if self.req.id in srsDict:
            print("Same ID found.")
            print(self.req.id)
            assert self.req.id not in srsDict
        
        srsDict[self.req.id] = self.req    

class SafeReqFactory(ReqFactory):
    
    def create(self):
        self.req = SafeReq()

    def concreteStore(self, reqP):
        self.req.id = reqP.id      
        self.req.type = 'SAFE'
        self.req.trace = reqP.trace
        self.req.verify = reqP.verify

        if self.req.id in srsDict:
            print("Same ID found.")
            print(self.req.id)
            assert self.req.id not in srsDict
        
        srsDict[self.req.id] = self.req    

class IntfReqFactory(ReqFactory):

    def create(self):
        self.req = IntfReq()
        return self.req

    def concreteStore(self, reqP):
        self.req.id = reqP.id
        self.req.intfId = reqP.intfId
        self.req.type = 'INTF'
        self.req.trace = reqP.trace
        self.req.verify = reqP.verify

        if self.req.id in srsDict:
            print("Same ID found.")
            print(self.req.id)
            assert self.req.id not in srsDict        

        srsDict[self.req.id] = self.req










    
