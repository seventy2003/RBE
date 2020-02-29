# -*- coding: utf-8 -*-

"""
FILE : tplGen 

DESCRIPTION:   
                                                                                       
FUNCTION LIST:  
1. xx

REVISION:  
  
Ver  | yyyymmdd | Who    | Description of changes
1.00 | 20200218 | wxhao  | Create.

"""

import json
import time

codeText = ""

classDefStatement = """class State$var$(PState):

    def lineParse(self, pars):
"""

selfStatement = """        if (pars.match$var$()):
            pars.proc$var$()
"""

selfStatementHead = """        if (pars.match$var$()):
            pars.resetState()
            pars.proc$var$()
"""

selfStatementTail = """        if (pars.match$var$()):
            pars.proc$var$()
            pars.endState()
"""

selfNoneStatement = """        if (pars.match$var$()):
            pars.setState(State$var$())
            pars.parseLine()
"""

postStatement = """        elif (pars.match$var$()):
            pars.setState(State$var$())
            pars.parseLine()
"""

excpStatement = """        elif (pars.match$var$()):
            pars.setState(StateExcp())
            pars.parseLine()
"""

attriEndStatement = """        else:
            pars.setState(State$var$())
            pars.parseLine()
"""

attriContStatement = """        else:
            pars.proc$var$()
"""

nullClassStatement = """        pass
"""

lineParseStatement = """    def lineParse(self, pars):

        if (pars.match$var$()):
            pars.setState(State$var$())
            pars.parseLine()
"""


f = open('tplText.tpl.py', 'r')

inText = f.readlines()

output = open('pState.py', 'w')

for line in inText:
    codeText += line

# generate itemDict and null Items list FROM json file
tmlJson = json.load(open('rules.json'))
nullItems = tmlJson["allItems"][:]
head = tmlJson["headAttribute"]
tail = tmlJson["tailAttribute"]

itemDict = {}
del tmlJson["allItems"]
del tmlJson["headAttribute"]
del tmlJson["tailAttribute"]

for ele in nullItems:
    postList = []

    if ele == "None" or ele == "Excp":
        continue
    for key in tmlJson:
        if key == "allItems" :
            continue
        if ele in tmlJson[key]:
            idx = tmlJson[key].index(ele) + 1
            if idx == len(tmlJson[key]):
                curEle = tmlJson[key][0]
                #postList.append(tmlJson[key][0])
            else:
                curEle = tmlJson[key][idx]
                #postList.append(tmlJson[key][idx])
            if postList.count(curEle) == 0:
                postList.append(curEle)
            
            #postList.append(tmlJson[key][idx])
    
    # exert null list? 
    if len(postList) != 0:
        itemDict[ele] = postList


#itemDict = {"Id":["Disc"], "Disc":["Input", "Verify"], "Input":["Output"], "Output":["Handle"], "Handle":["Perfm"], "Perfm":["Verify"], "Verify":["Trace"], "Trace":["Id"] }
#nullItems =  ["Id", "Disc", "Input", "Output", "Handle", "Perfm", "Verify", "Trace", "None", "Excp", "Interface", "Abcdefg"]

# valid json, todo
# funReq items must in allItems, head and tail must in allItems, and must be head and end of funReq and other type of Req.

itemEnum = []

for key in itemDict:
    itemEnum.append(key)
    nullItems.remove(key)


for key in itemDict:
    code = ""
    elifEnum = itemEnum[:]
    elifEnum.remove(key)

    # part 0: class def code
    if key != "Excp" and key != "None":
        code += classDefStatement.replace("$var$", key)

    # part 1: self code
    if key == head:
        code += selfStatementHead.replace("$var$", key)
    elif key == tail:
        code += selfStatementTail.replace("$var$", key)
    else:
        code += selfStatement.replace("$var$", key)

    # part 2: post code
    for it in itemDict[key]:
        code += postStatement.replace("$var$", it)
        elifEnum.remove(it)
    
    for it in elifEnum:
        code += excpStatement.replace("$var$", it)

    # part 3: else code
    if key == "Id" or key == "Verify":
        code += attriEndStatement.replace("$var$", "Excp")
    elif key == "Trace":
        code += attriEndStatement.replace("$var$", "None")
    else:
        code += attriContStatement.replace("$var$", key)

    kw = "#" + key + "#"
    codeText = codeText.replace("#" + key + "#", code)

"""
code of 'None' state
"""

code = ""
code += classDefStatement.replace("$var$", "None")

# if code
code += selfNoneStatement.replace("$var$", head)

# elif code
for key in itemDict:
    if key == head:
        continue
    else:
        code += excpStatement.replace("$var$", key)

# else code
#code += attriEndStatement.replace("$var$", "None")

codeText = codeText.replace("#" + "None" + "#", code)

"""
code of lineParse
"""
code = ""
code += lineParseStatement.replace("$var$", head)
codeText = codeText.replace("#" + "lineParse" + "#", code)

"""
process null class
"""

nullItems.remove("None")
nullItems.remove("Excp")

if nullItems:
    for it in nullItems:
        code = ""
        code += classDefStatement.replace("$var$", it)
        code += nullClassStatement

        kw = "#" + it + "#"
        codeText = codeText.replace("#" + it + "#", code)

"""
update time
"""
curDay = time.strftime("%Y%m%d", time.localtime())
codeText = codeText.replace("#GENDAY#", curDay)

curTime = time.strftime("%H:%M:%S", time.localtime())
codeText = codeText.replace("#GENTIME#", curTime)


# idCode = ""
# idCode += selfStatement.replace("$var$", "Id")
# idCode += postStatement.replace("$var$", "Disc")
# idCode += excpStatement.replace("$var$", "Verify")
# idCode += elseStatement.replace("$var$", "Excp")

# codeTextNew = codeText.replace("#Id#", idCode)

"""
write file
"""

output.write(codeText)
output.close()


print("Done.")
