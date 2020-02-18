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

codeText = ""

classDefStatement = """class State$var$(PState):

    def lineParse(self, pars):
"""

selfStatement = """        if (pars.match$var$()):
            pars.proc$var$()
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

f = open('tplText.tpl.py', 'r')

inText = f.readlines()

output = open('pState.py', 'w')

for line in inText:
    codeText += line

# generate itemDict and null Items list FROM json, todo 
tmlJson = json.load(open('rules.json'))
nullItems = tmlJson["allItems"][:]
itemDict = {}
del tmlJson["allItems"]
for ele in nullItems:
    postList = []

    if ele == "None" or ele == "Excp":
        continue
    for key in tmlJson:
        if key == "allItems":
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


# process null class
nullItems.remove("None")
nullItems.remove("Excp")
code = ""
if nullItems:
    for it in nullItems:
        code += classDefStatement.replace("$var$", it)
        code += nullClassStatement

        kw = "#" + it + "#"
        codeText = codeText.replace("#" + it + "#", code)

# idCode = ""
# idCode += selfStatement.replace("$var$", "Id")
# idCode += postStatement.replace("$var$", "Disc")
# idCode += excpStatement.replace("$var$", "Verify")
# idCode += elseStatement.replace("$var$", "Excp")

# codeTextNew = codeText.replace("#Id#", idCode)

output.write(codeText)
output.close()


print("Done.")
