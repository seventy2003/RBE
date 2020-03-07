# -*- coding: utf-8 -*-

"""
FILE : output 

DESCRIPTION:   
                                                                                       
FUNCTION LIST:  
  1. class definition of Output

REVISION:  
  
Ver  | yyyymmdd | Who    | Description of changes
1.00 | 20191122 | wxhao  | Create.

"""

import csv

from req import srsDict
from ioProc import *

class OutputRBE:

    def __init__(self):
        pass

    def srsOutput(self):
        
        # generate output file of srs
        f = open('../output/srsGeneral.csv','w', newline="")

        csvWriter = csv.writer(f)
        for k in sorted(srsDict.keys()):
            if srsDict[k]:
                csvWriter.writerow([srsDict[k].id, srsDict[k].type, srsDict[k].trace])

        f.close()

        # input and output list file of srs
        f = open('../output/srsIO.csv','w', newline="")

        csvWriter = csv.writer(f)
        csvWriter.writerow(["Requirement ID", "Input", "Output"])
        for k in sorted(srsDict.keys()):
            if srsDict[k].type is 'FUNC':
                csvWriter.writerow([srsDict[k].id, srsDict[k].dataIn, srsDict[k].dataOut])

        f.close()


        # IO data dictionary
        # check there have input and output attribute, todo

        f = open('../output/ioDict.csv','w', newline="")

        csvWriter = csv.writer(f)
        csvWriter.writerow(["Requirement ID", "Direction", "Input", "Output", "类型", "字节数", "单位", "范围", "定标", "备注"])

        ioD = IOProc()
        ioD.genDict()
        
        # write file
        for k in sorted(ioD.ioDict.keys()):
            #if srsDict[k].type is 'FUNC':
            if ioD.ioDict[k].inDict == 1 and ioD.ioDict[k].outDict == 1:
                direction = 'IO'
            elif ioD.ioDict[k].inDict == 1:
                direction = 'I'
            else:
                direction = 'O'

            csvWriter.writerow([k, direction, ioD.ioDict[k].inData, ioD.ioDict[k].outData])

        f.close()
