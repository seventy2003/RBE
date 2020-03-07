# -*- coding: utf-8 -*-

"""
FILE : ioDict 

DESCRIPTION:   
                                                                                       
FUNCTION LIST:  
  1. generate IO data dictionary.

REVISION:  
  
Ver  | yyyymmdd | Who    | Description of changes
1.00 | 20200305 | wxhao  | Create.

"""

#ioDict = {}

from req import srsDict

class IOData:

    inData = None
    outData = None
    inDict = 0
    outDict = 0

    def __init__(self):

        self.inData = []
        self.outData = []
        inDict = 0
        outDict = 0

    def appendIn(self, inD):

        self.inData.append(inD)

    def appendOut(self, outD):
        
        self.outData.append(outD)


class IOProc:

    ioDict = None

    def __init__(self):

        self.ioDict = {}

    def genDict(self):

        for k in sorted(srsDict.keys()):
            if srsDict[k].type is 'FUNC':
                #csvWriter.writerow([srsDict[k].id, srsDict[k].dataIn, srsDict[k].dataOut])
                # process input
                if srsDict[k].dataIn:
                    for ele in srsDict[k].dataIn:
                        if ele in self.ioDict:
                            self.ioDict[ele].inData.append(srsDict[k].id)
                        else:
                            newData = IOData()
                            newData.appendIn(srsDict[k].id)
                            self.ioDict[ele] = newData

                        self.ioDict[ele].inDict = 1
                        
                
                # process output
                if srsDict[k].dataOut:
                    for ele in srsDict[k].dataOut:
                        #ioDict[ele].outData.append(srsDict[k].id)
                        if ele in self.ioDict:
                            self.ioDict[ele].outData.append(srsDict[k].id)
                        else:
                            newData = IOData()
                            newData.appendOut(srsDict[k].id)
                            
                            self.ioDict[ele] = newData
                            #ioDict[ele] = newData.appendOut(srsDict[k].id)

                            #ioDict[ele] = newData.outData.append(srsDict[k].id)
                        
                        self.ioDict[ele].outDict = 1
