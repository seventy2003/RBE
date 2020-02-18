
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
        elif (pars.matchInput()):
            pars.setState(StateExcp())
            pars.parseLine()
        elif (pars.matchOutput()):
            pars.setState(StateExcp())
            pars.parseLine()
        elif (pars.matchHandle()):
            pars.setState(StateExcp())
            pars.parseLine()
        elif (pars.matchPerfm()):
            pars.setState(StateExcp())
            pars.parseLine()
        elif (pars.matchVerify()):
            pars.setState(StateExcp())
            pars.parseLine()
        elif (pars.matchTrace()):
            pars.setState(StateExcp())
            pars.parseLine()
        else:
            pars.setState(StateExcp())
            pars.parseLine()

"""
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
"""            
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
        elif (pars.matchHandle()):
            pars.setState(StateExcp())
            pars.parseLine()
        elif (pars.matchPerfm()):
            pars.setState(StateExcp())
            pars.parseLine()
        elif (pars.matchTrace()):
            pars.setState(StateExcp())
            pars.parseLine()
        else:
            pars.procDisc()

"""
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
"""                

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
        elif (pars.matchDisc()):
            pars.setState(StateExcp())
            pars.parseLine()
        elif (pars.matchHandle()):
            pars.setState(StateExcp())
            pars.parseLine()
        elif (pars.matchPerfm()):
            pars.setState(StateExcp())
            pars.parseLine()
        elif (pars.matchVerify()):
            pars.setState(StateExcp())
            pars.parseLine()
        elif (pars.matchTrace()):
            pars.setState(StateExcp())
            pars.parseLine()
        else:
            pars.procInput()

"""
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
"""
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
        elif (pars.matchDisc()):
            pars.setState(StateExcp())
            pars.parseLine()
        elif (pars.matchInput()):
            pars.setState(StateExcp())
            pars.parseLine()
        elif (pars.matchPerfm()):
            pars.setState(StateExcp())
            pars.parseLine()
        elif (pars.matchVerify()):
            pars.setState(StateExcp())
            pars.parseLine()
        elif (pars.matchTrace()):
            pars.setState(StateExcp())
            pars.parseLine()
        else:
            pars.procOutput()

"""
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
"""

class StateHandle(PState):

    def lineParse(self, pars):
        if (pars.matchHandle()):
            pars.procHandle()
        elif (pars.matchPerfm()):
            pars.setState(StatePerfm())
            pars.parseLine()
        elif (pars.matchId()):
            pars.setState(StateExcp())
            pars.parseLine()
        elif (pars.matchDisc()):
            pars.setState(StateExcp())
            pars.parseLine()
        elif (pars.matchInput()):
            pars.setState(StateExcp())
            pars.parseLine()
        elif (pars.matchOutput()):
            pars.setState(StateExcp())
            pars.parseLine()
        elif (pars.matchVerify()):
            pars.setState(StateExcp())
            pars.parseLine()
        elif (pars.matchTrace()):
            pars.setState(StateExcp())
            pars.parseLine()
        else:
            pars.procHandle()

"""
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
"""
class StatePerfm(PState):

    def lineParse(self, pars):
        if (pars.matchPerfm()):
            pars.procPerfm()
        elif (pars.matchVerify()):
            pars.setState(StateVerify())
            pars.parseLine()
        elif (pars.matchId()):
            pars.setState(StateExcp())
            pars.parseLine()
        elif (pars.matchDisc()):
            pars.setState(StateExcp())
            pars.parseLine()
        elif (pars.matchInput()):
            pars.setState(StateExcp())
            pars.parseLine()
        elif (pars.matchOutput()):
            pars.setState(StateExcp())
            pars.parseLine()
        elif (pars.matchHandle()):
            pars.setState(StateExcp())
            pars.parseLine()
        elif (pars.matchTrace()):
            pars.setState(StateExcp())
            pars.parseLine()
        else:
            pars.procPerfm()
   
"""   
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
"""
class StateVerify(PState):

    def lineParse(self, pars):
        if (pars.matchVerify()):
            pars.procVerify()
        elif (pars.matchTrace()):
            pars.setState(StateTrace())
            pars.parseLine()
        elif (pars.matchId()):
            pars.setState(StateExcp())
            pars.parseLine()
        elif (pars.matchDisc()):
            pars.setState(StateExcp())
            pars.parseLine()
        elif (pars.matchInput()):
            pars.setState(StateExcp())
            pars.parseLine()
        elif (pars.matchOutput()):
            pars.setState(StateExcp())
            pars.parseLine()
        elif (pars.matchHandle()):
            pars.setState(StateExcp())
            pars.parseLine()
        elif (pars.matchPerfm()):
            pars.setState(StateExcp())
            pars.parseLine()
        else:
            pars.setState(StateExcp())
            pars.parseLine()

"""
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
"""
class StateTrace(PState):

    def lineParse(self, pars):
        if (pars.matchTrace()):
            pars.procTrace()
        elif (pars.matchId()):
            pars.setState(StateId())
            pars.parseLine()
        elif (pars.matchDisc()):
            pars.setState(StateExcp())
            pars.parseLine()
        elif (pars.matchInput()):
            pars.setState(StateExcp())
            pars.parseLine()
        elif (pars.matchOutput()):
            pars.setState(StateExcp())
            pars.parseLine()
        elif (pars.matchHandle()):
            pars.setState(StateExcp())
            pars.parseLine()
        elif (pars.matchPerfm()):
            pars.setState(StateExcp())
            pars.parseLine()
        elif (pars.matchVerify()):
            pars.setState(StateExcp())
            pars.parseLine()
        else:
            pars.setState(StateNone())
            pars.parseLine()

"""
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
"""

class StateInterface(PState):

    def lineParse(self, pars):
        pass


#Abcdefg#

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

class StateExcp(PState):

    def lineParse(self, pars):
        pars.procExcp()

