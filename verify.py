# -*- coding: utf-8 -*-

"""
FILE : verify 

DESCRIPTION:   
                                                                                       
FUNCTION LIST:  
  1. verify

REVISION:  

  
Ver  | yyyymmdd | Who    | Description of changes
1.00 | 20200307 | wxhao  | Create.

"""

import csv
import matplotlib.pyplot as plt
import numpy as np

from req import srsDict

class Verify:

    verf = None

    def __init__(self):

        self.verf = {}

    def genVerify(self):
        
        pass

    def outputVerify(self):
        # generate output file of verify
        f = open('../output/verify.csv','w', newline="")

        csvWriter = csv.writer(f)

        csvWriter.writerow(["SRS ID", "验证方法", "测试用例", "验证结果"])

        for k in srsDict:
            csvWriter.writerow([k, srsDict[k].verify])

        f.close()

    def genPieChart(self):

        testCnt = 0
        scanCnt = 0
        anaCnt = 0
        showCnt = 0
        otherCnt = 0

        for k in srsDict:
            if srsDict[k].verify == "测试":
                testCnt += 1
            elif srsDict[k].verify == "审查":
                scanCnt += 1
            elif srsDict[k].verify == "分析":
                anaCnt += 1
            elif srsDict[k].verify == "演示":
                showCnt += 1   
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

        data = [testCnt, scanCnt, anaCnt, showCnt, otherCnt]
        ingredients = ['测试', '审查', '分析', '演示', '其他']


        def func(pct, allvals):
            absolute = int(pct/100.*np.sum(allvals))
            return "{:.1f}%\n({:d}条)".format(pct, absolute)


        wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
                                        textprops=dict(color="w"))

        ax.legend(wedges, ingredients,
                title="验证方法",
                loc="center left",
                bbox_to_anchor=(1, 0, 0.5, 1))

        plt.setp(autotexts, size=8, weight="bold")

        ax.set_title("需求验证方法分布图")

        ##
        t = ("需求总条数：{:d}条".format(testCnt + scanCnt + anaCnt + showCnt + otherCnt))
        plt.text(1.8, 1, t, ha='right', wrap=True)

        plt.show()          