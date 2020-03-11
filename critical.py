# -*- coding: utf-8 -*-

"""
FILE : critical 

DESCRIPTION:   
                                                                                       
FUNCTION LIST:  
  1. critical

REVISION:  

  
Ver  | yyyymmdd | Who    | Description of changes
1.00 | 20200307 | wxhao  | Create.

"""

import csv

from req import srsDict

class Critical:
  
  crtal = None

  def __init__(self):

    self.crtal = {}

  def genLevelRt(self):
      
      pass

  def outputCrtal(self):
      # generate output file of critical
      f = open('../output/critical.csv','w', newline="")

      csvWriter = csv.writer(f)

      csvWriter.writerow(["SRS ID", "用户定义重要性", "成本权值", "进度权值", "风险权值", "性能权值", "成本", "进度", "风险", "性能", "重要性"])

      for k in srsDict:
        csvWriter.writerow([k])

      f.close()