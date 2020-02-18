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

