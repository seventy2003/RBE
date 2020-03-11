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
import matplotlib.pyplot as plt
import numpy as np

from req import srsDict
from ioProc import *

class OutputRBE:

    def __init__(self):
        pass

    def srsOutput(self):
        
        # generate output file of srs
        f = open('../output/srsGeneral.csv','w', newline="")

        csvWriter = csv.writer(f)

        csvWriter.writerow(["SRS ID", "type", "verify", "Input", "Output", "Trace"])

        for k in sorted(srsDict.keys()):
            if srsDict[k]:
                if srsDict[k].type is 'FUNC' or srsDict[k].type is 'PERF' or srsDict[k].type is 'SAFE':
                    csvWriter.writerow([srsDict[k].id, srsDict[k].type, srsDict[k].verify, srsDict[k].dataIn, srsDict[k].dataOut, srsDict[k].trace])
                else:
                    csvWriter.writerow([srsDict[k].id, srsDict[k].type, srsDict[k].verify, 'N/A', 'N/A', srsDict[k].trace])

        f.close()

        # input and output list file of srs
        """
        f = open('../output/srsIO.csv','w', newline="")

        csvWriter = csv.writer(f)
        csvWriter.writerow(["Requirement ID", "Input", "Output"])
        for k in sorted(srsDict.keys()):
            if srsDict[k].type is 'FUNC':
                csvWriter.writerow([srsDict[k].id, srsDict[k].dataIn, srsDict[k].dataOut])

        f.close()
        """


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
    
    def genPieChart(self):

        funcCnt = 0
        perfCnt = 0
        safeCnt = 0
        otherCnt = 0

        for k in srsDict:
            if srsDict[k].type == "FUNC":
                funcCnt += 1
            elif srsDict[k].type == "PERF":
                perfCnt += 1
            elif srsDict[k].type == "SAFE":
                safeCnt += 1 
            else:
                otherCnt += 1

        """
        # Pie chart, where the slices will be ordered and plotted counter-clockwise:

        plt.rcParams['font.sans-serif'] = ['SimHei'] # 指定默认字体
        plt.rcParams['axes.unicode_minus'] = False 

        labels = '测试', '审查', '分析', '演示', '其他'
        sizes = [testCnt, scanCnt, anaCnt, showCnt, otherCnt]
        explode = (0, 0.1, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        plt.show()   
        """


        plt.rcParams['font.sans-serif'] = ['SimHei'] # 指定默认字体
        plt.rcParams['axes.unicode_minus'] = False 

        fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

        data = [funcCnt, perfCnt, safeCnt, otherCnt]
        ingredients = ['功能需求 {:d}条'.format(funcCnt), '性能需求 {:d}条'.format(perfCnt), '安全性需求 {:d}条'.format(safeCnt), '其他需求 {:d}条'.format(otherCnt)]


        def func(pct, allvals):
            absolute = int(pct/100.*np.sum(allvals))
            return "{:.1f}%".format(pct)


        wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
                                        textprops=dict(color="w"))

        ax.legend(wedges, ingredients,
                title="需求类型及条目数",
                loc="center left",
                bbox_to_anchor=(1, 0, 0.5, 1))

        plt.setp(autotexts, size=8, weight="bold")

        ax.set_title("需求类型分布图")

        ##
        t = ("需求总条数：{:d}条".format(funcCnt + perfCnt + safeCnt + otherCnt))
        plt.text(1.8, 1, t, ha='right', wrap=True)

        plt.show()  



