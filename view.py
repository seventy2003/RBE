# -*- coding: utf-8 -*-

"""
FILE : view 

DESCRIPTION:   
                                                                                       
FUNCTION LIST:  
1. UI
2. get input
3. debug 

REVISION:  
  
Ver  | yyyymmdd | Who    | Description of changes
1.00 | 20181105 | wxhao  | Create.

"""

import sys
import os
import configparser
from docx import Document
import csv

from strace import *
from req import *
from parse import Parse


# for debug display
from req import srsDict  

cmdUI = [
        '--------------------------------'  ,
        'Input command:'                    ,
        '  \'1\': start parse;'             ,
        '  \'2\': display list;'            ,
        '  \'3\': trace USER ID'            ,
        '  \'4\': generate csv file;'       ,        
        '  \'0\': exit.'
]

class View:
    
    def __init__(self):
        pass
    def init(self):
        pass
    def getInput(self):
        pass    
    def interact(self):
        pass
    def run(self):
        pass

class CmdView(View):

    parse = None
    trace = None
    
    def init(self):
        self.parse = Parse()

    def getInput(self):

        #self.parse = Parse()

        # get srs file
        try:
            cf = configparser.ConfigParser()
            cf.read("smg.conf")
            infile = cf.get("input", "inSrsFile")
            #self.f = open(infile, 'r', encoding = 'gb18030', errors = 'ignore')
            self.f = Document(infile)
        except IOError:
            print("File Open fail\n")
            raise Exception("File Open fail\n")

        #print('Done.')

    def interact(self):

        # display UI
        for line in cmdUI:
            print(line)

        cmd = input()
        if cmd == '1':
            print("Start parse...")
            self.parse.run(self.f)
            print('Done.')
        elif cmd == '2':
            self.display()
        elif cmd == '3':
            print('Trace User ID...')
            if self.parse.state == 100:
                print('Start trace')

                # get rw file
                try:
                    cf = configparser.ConfigParser()
                    cf.read("smg.conf")
                    infile = cf.get("input", "inUsrFile")
                    #self.f = open(infile, 'r', encoding = 'gb18030', errors = 'ignore')
                    self.fileRw = Document(infile)
                except IOError:
                    print("File Open fail\n")
                    raise Exception("File Open fail\n")

                self.trace = STrace(self.fileRw)
                self.trace.getUsrDict()
                self.trace.doTrace()
                self.trace.debug()
                self.trace.hasThisFun()
                #self.fc = fuck()
                #self.fc.funp()

            else:
                print('Parse first please.')
        elif cmd == '4':
            print('Generate csv file...')

            f = open('../output/dict.csv','w')

            csvWriter = csv.writer(f)
            for k in srsDict:
                if srsDict[k]:
                    csvWriter.writerow([k, srsDict[k].type])
            f.close()

        elif cmd == '0':
            os._exit(0)
        else:
            print('Invalid input.')
            
        return
        
    def run(self):
        self.init()
        while (1):
            self.getInput()
            self.interact()

    # for debug
    def display(self):
        # for debug
        for key in srsDict:
            if srsDict[key].type == 'FUNC':
                print(srsDict[key].id, "    ", srsDict[key].dataIn, "    ",
                      srsDict[key].dataOut, "    ", srsDict[key].trace, "    ",
                      srsDict[key].verify)
            if srsDict[key].type == 'INTF':
                print(srsDict[key].id, "    ", srsDict[key].trace, "    ",
                      srsDict[key].verify)

        print("Debug.")


