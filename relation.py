# -*- coding: utf-8 -*-

"""
FILE : relation 

DESCRIPTION:   
                                                                                       
FUNCTION LIST:  
  1. relation

REVISION:  

  
Ver  | yyyymmdd | Who    | Description of changes
1.00 | 20200307 | wxhao  | Create.

"""

import csv

from req import srsDict

class Relation:
  
  levelRt = None

  def __init__(self):

    self.levelRt = {}

  def genLevelRt(self):

      for k in sorted(srsDict.keys()):
        srsList = []
        pos = k.rfind('_')
        
        while pos != -1:
          sub = k[:pos]
          sub = sub.strip()

          if sub in srsDict:
            srsList.append(sub)
            self.levelRt[k] = srsList

          pos = sub.rfind('_')


  def outputRt(self):
      # generate output file of relations
      f = open('../output/relation.csv','w', newline="")

      csvWriter = csv.writer(f)
      for k in self.levelRt:
          if self.levelRt[k]:
              csvWriter.writerow([k, self.levelRt[k]])

      f.close()

