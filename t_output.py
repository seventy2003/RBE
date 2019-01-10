import pandas as pds
import csv


'''
a = [1, 2, 3]
b = [4, 5, 6]

dataFrame = pds.DataFrame({'a_til':a, 'b_til':b})

dataFrame.to_csv("../output/test.csv", index=False, sep=',')
'''
#testDict = {'k1': 'k1val', 'k2': 'k2val', 'k3': 'k3val'}
testDict = {'k1': ['k1_1', 'k1_2', 'k1_3'], 'k2': ['k2_1', 'k2_2', 'k2_3'], 'k3': ['k3_1', 'k3_2', 'k3_3']}


f = open('../output/testCsvOut.csv','w', newline="")

csvWriter = csv.writer(f)
'''
for k,v in testDict.items():
    csvWriter.writerow([k, v])
f.close()
'''

for k in testDict:
    csvWriter.writerow([k, testDict[k][0], testDict[k][1], testDict[k][2]])
f.close()
