from sklearn.neighbors import NearestNeighbors as nn
import random as rd
import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt

def write (data, testFile, fn):
    with open (testFile, 'w', newline= '') as wr:
        out = csv.writer(wr, delimiter=",", quotechar='|')
        out.writerow(fn)
        for d in data:
            out.writerow(d)

def splitData(proportion, filename):
    dic = {
        'EmplooyeeIdx':int, 'CntyOfResidence':int, 'Sex':int, 'Age':int, '1stContract':int,
        'NewCusIdx':int, 'Seniority':int, 'CusType':int, 'RelationType':int, 'ForeignIdx':int,
        'ChnlEnter':int, 'DeceasedIdx':int, 'ProvCode':int, 'ActivIdx':int, 'Income':float,
        'Segment':int,

        'SavingAcnt':int, 'Guarantees':int, 'CurrentAcnt':int, 'DerivativesAcnt':int, 'PayrollAcnt':int,
        'JuniorAcnt':int, 'MoreParticularAcnt':int, 'ParticularAcnt':int, 'ParticularPlusAcnt':int, 'ShortDeposit':int,
        'MediumDeposit':int, 'LongDeposit':int, 'eAcnt':int, 'Funds':int, 'Mortgage':int,
        'Pensions':int, 'Loans':int, 'Taxes':int, 'CreditCard':int, 'Securities':int,
        'HomeAcnt':int, 'Payroll':int, 'PayrollPensions':int, 'DirectDebit':int
           }
    fn = ["FetchDate", "CusID", "EmployeeIdx", "CntyOfResidence", "Sex",    #Fieldnames
                 "Age", "1stContract", "NewCusIdx", "Seniority", "CusType",
                 "RelationType", "ForeignIdx", "ChanEnter", "DeceasedIdx", "ProvCode",
                 "ActivIdx", "Income", "Segment",

              "SavingAcnt", "Guarantees",
                 "CurrentAcnt", "DerivativesAcnt", "PayrollAcnt", "JuniorAcnt", "MoreParticularAcnt",
                 "ParticularAcnt", "ParticularPlusAcnt", "ShortDeposit", "MediumDeposit", "LongDeposit",
                 "eAcnt", "Funds", "Mortgage", "Pensions", "Loans",
                 "Taxes", "CreditCard", "Securities", "HomeAcnt", "Payroll",
                 "PayrollPensions", "DirectDebit" ]
    df = pd.read_csv(filename, header=0, dtype=dic)
    data = df.as_matrix()
    rowsNum = len(data)
    custNum = rowsNum/17
    for i in range (len(proportion)):
        proportion[i] = round(proportion[i]*custNum,0)*17
    output1 = data[:int(proportion[0])]
    write(output1, 'fitData.csv', fn)
    output2 = data[int(proportion[0]):]
    write(output2, 'test0.csv', fn)

def randSelect():
    out1, out2 = [], []
    rand = rd.randint(1,15)
    idx = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    for r in range(rand):
        i = rd.randint(0, len(idx)-1)
        out1.append(idx.pop(i))
    for i in idx:
        if checkList(out1, i) == -1:
            out2.append(i)
    return out1, out2

def selectData(test0, testFile, comparefile):
    dic = {
        'EmplooyeeIdx': int, 'CntyOfResidence': int, 'Sex': int, 'Age': int, '1stContract': int,
        'NewCusIdx': int, 'Seniority': int, 'CusType': int, 'RelationType': int, 'ForeignIdx': int,
        'ChnlEnter': int, 'DeceasedIdx': int, 'ProvCode': int, 'ActivIdx': int, 'Income': float,
        'Segment': int,

        'SavingAcnt': int, 'Guarantees': int, 'CurrentAcnt': int, 'DerivativesAcnt': int, 'PayrollAcnt': int,
        'JuniorAcnt': int, 'MoreParticularAcnt': int, 'ParticularAcnt': int, 'ParticularPlusAcnt': int,
        'ShortDeposit': int,
        'MediumDeposit': int, 'LongDeposit': int, 'eAcnt': int, 'Funds': int, 'Mortgage': int,
        'Pensions': int, 'Loans': int, 'Taxes': int, 'CreditCard': int, 'Securities': int,
        'HomeAcnt': int, 'Payroll': int, 'PayrollPensions': int, 'DirectDebit': int
    }
    df = pd.read_csv(test0, header=0, dtype=dic)
    testData = df.as_matrix()
    print (np.shape(testData))
    x = testData[0][1]

    test = []
    fn = ["FetchDate", "CusID", "EmployeeIdx", "CntyOfResidence", "Sex",    #Fieldnames
                 "Age", "1stContract", "NewCusIdx", "Seniority", "CusType",
                 "RelationType", "ForeignIdx", "ChanEnter", "DeceasedIdx", "ProvCode",
                 "ActivIdx", "Income", "Segment",

              "SavingAcnt", "Guarantees",
                 "CurrentAcnt", "DerivativesAcnt", "PayrollAcnt", "JuniorAcnt", "MoreParticularAcnt",
                 "ParticularAcnt", "ParticularPlusAcnt", "ShortDeposit", "MediumDeposit", "LongDeposit",
                 "eAcnt", "Funds", "Mortgage", "Pensions", "Loans",
                 "Taxes", "CreditCard", "Securities", "HomeAcnt", "Payroll",
                 "PayrollPensions", "DirectDebit" ]
    with open (testFile, 'w', newline= '') as wr1, open (comparefile, 'w', newline= '') as wr2:
        out1 = csv.writer(wr1, delimiter=",", quotechar='|')
        out2 = csv.writer(wr2, delimiter=",", quotechar='|')
        out1.writerow(fn)
        out2.writerow(fn)
        for row in testData:
            if row[1] == x:
                test.append(row)
            else:
                idx1, idx2 = randSelect()

                for i in idx1:
                    out1.writerow(test[i])
                for j in idx2:
                    out2.writerow(test[j])
                test = []
                test.append(row)
                x = row[1]
        idx1, idx2 = randSelect()

        for i in idx1:
            out1.writerow(test[i])
        for j in idx2:
            out2.writerow(test[j])
    sortData(testFile)

def sortData (filein):
    df = pd.read_csv(filein)
    df = df.sort_values(['CusID','FetchDate'], ascending = [True, True])
    df.to_csv('test1.csv',index=False, sep = ',', encoding = 'utf-8')

def checkList (list, input):
    try:
        list.index(input)
    except ValueError:
        return -1
    else:
        return list.index(input)

def getData(file, CI):
    m = ['16463', '16494', '16522', '16553', '16583', '16614', '16644', '16675', '16706', '16736', '16767', '16797',
         '16828', '16859', '16888', '16919', '16949']
    dic = {
        'EmplooyeeIdx':int, 'CntyOfResidence':int, 'Sex':int, 'Age':int, '1stContract':int,
        'NewCusIdx':int, 'Seniority':int, 'CusType':int, 'RelationType':int, 'ForeignIdx':int,
        'ChnlEnter':int, 'DeceasedIdx':int, 'ProvCode':int, 'ActivIdx':int, 'Income':float,
        'Segment':int,

        'SavingAcnt':int, 'Guarantees':int, 'CurrentAcnt':int, 'DerivativesAcnt':int, 'PayrollAcnt':int,
        'JuniorAcnt':int, 'MoreParticularAcnt':int, 'ParticularAcnt':int, 'ParticularPlusAcnt':int, 'ShortDeposit':int,
        'MediumDeposit':int, 'LongDeposit':int, 'eAcnt':int, 'Funds':int, 'Mortgage':int,
        'Pensions':int, 'Loans':int, 'Taxes':int, 'CreditCard':int, 'Securities':int,
        'HomeAcnt':int, 'Payroll':int, 'PayrollPensions':int, 'DirectDebit':int
           }
    df = pd.read_csv(file, header=0, dtype=dic)
    date = df.pop('FetchDate')
    date = date.as_matrix()
    id  = df.pop('CusID')
    id = id.as_matrix()
    if CI == True:
        df.drop(["SavingAcnt", "Guarantees",
                 "CurrentAcnt", "DerivativesAcnt", "PayrollAcnt", "JuniorAcnt", "MoreParticularAcnt",
                 "ParticularAcnt", "ParticularPlusAcnt", "ShortDeposit", "MediumDeposit", "LongDeposit",
                 "eAcnt", "Funds", "Mortgage", "Pensions", "Loans",
                 "Taxes", "CreditCard", "Securities", "HomeAcnt", "Payroll",
                 "PayrollPensions", "DirectDebit"], axis=1, inplace=True)
    data2d = df.as_matrix()
    output2d = np.array(data2d)
    return id, date, output2d

def lookID(indices, comp_id):
    id = []
    out = {}
    s = 0
    for i in indices:
        for x in i:
            if checkList(id,comp_id[x]) == -1:
                id.append(comp_id[x])
                out[comp_id[x]] = 1
            else:
                out[comp_id[x]] +=1
            s +=1
    for k, v in out.items():
        out[k]=float(v/s)
    return out

def checkDraw (id_dic):
    ls = []
    for k, v in id_dic.items():
        ls.append(v)
    unique = set(ls)
    if len(unique) != len(ls):
        return True
    else:
        return False

def missingM(date):
    month = ['16463', '16494', '16522', '16553', '16583', '16614', '16644', '16675', '16706', '16736', '16767', '16797',
         '16828', '16859', '16888', '16919', '16949']
    out = []
    for m in month:
        if checkList(date, int(m)) == -1:
            out.append(m)
    return out

def predictFrom(id_dic, comp_id, comp_data2d): #returns index of comp data to predict from
    out= {}
    idx = []
    for k, v in id_dic.items():
        row, = np.where(comp_id==k)
        for r in row:
            idx.append(comp_data2d[r])
        out[k]= idx
        idx = []
    return out

def calcRow(row, v, fn, test): # Padeach row of missing data
    row[(fn.index("EmployeeIdx")-2)] = round((row[(fn.index("EmployeeIdx")-2)]*v),0)
    row[(fn.index("CntyOfResidence")-2)] = round((row[(fn.index("CntyOfResidence")-2)]*v),0)
    row[(fn.index("Sex")-2)] = test[0][(fn.index('Sex')-2)]
    row[(fn.index("Age")-2)] = test[0][(fn.index("Age")-2)]
    row[(fn.index("1stContract")-2)] = test[0][(fn.index("1stContract")-2)]
    row[(fn.index("NewCusIdx")-2)] = round((row[(fn.index("NewCusIdx")-2)]*v),0)
    row[(fn.index("Seniority")-2)] = round((row[(fn.index("Seniority")-2)]*v),2)
    row[(fn.index("CusType")-2)] = round((row[(fn.index("CusType")-2)]*v),0)
    row[(fn.index("RelationType")-2)] = round((row[(fn.index("RelationType")-2)]*v),0)
    row[(fn.index("ForeignIdx")-2)] = round((row[(fn.index("ForeignIdx")-2)]*v),0)
    row[(fn.index("ChanEnter")-2)] = row[(fn.index("ChanEnter")-2)]
    row[(fn.index("DeceasedIdx")-2)] = round((row[(fn.index("DeceasedIdx")-2)]*v),0)
    row[(fn.index("ProvCode")-2)] = round((row[(fn.index("ProvCode")-2)]*v),0)
    row[(fn.index("ActivIdx")-2)] = round((row[(fn.index("ActivIdx")-2)]*v),0)
    row[(fn.index("Income")-2)] = test[0][(fn.index("Income")-2)]
    row[(fn.index("Segment")-2)] = round((row[(fn.index("Segment")-2)]*v),0)
    return row

def padRow (row, fn):
    out = []
    out.append(row[(fn.index("EmployeeIdx")-2)])
    out.append(row[(fn.index("CntyOfResidence")-2)])
    out.append(row[(fn.index("Sex")-2)])
    out.append(row[(fn.index("Age")-2)])
    out.append(row[(fn.index("1stContract")-2)])
    out.append(row[(fn.index("NewCusIdx")-2)])
    out.append(row[(fn.index("Seniority")-2)])
    out.append(row[(fn.index("CusType")-2)])
    out.append(row[(fn.index("RelationType")-2)])
    out.append(row[(fn.index("ForeignIdx")-2)])
    out.append(row[(fn.index("ChanEnter")-2)])
    out.append(row[(fn.index("DeceasedIdx")-2)])
    out.append(row[(fn.index("ProvCode")-2)])
    out.append(row[(fn.index("ActivIdx")-2)])
    out.append(row[(fn.index("Income")-2)])
    out.append(row[(fn.index("Segment")-2)])
    return out

def closeDate(month, missing_m, miss, date):
    x = 1000
    out = 0
    idx = checkList(month, miss)
    for i in range (idx):
        if checkList(missing_m, int(month[i])) == -1:
            out = int(month[i])
    output = checkList(date, out)
    return output

def padding(cusID, missing_m, date, test, fn):
    month = ['16463', '16494', '16522', '16553', '16583', '16614', '16644', '16675', '16706', '16736', '16767', '16797',
         '16828', '16859', '16888', '16919', '16949']
    output = []
    for miss in missing_m: # for each missing month
        idx = closeDate(month, missing_m, miss, date)
        out = padRow(test[idx], fn)
        out.insert(0, cusID)
        out.insert(0, miss)
        output.append(out)
    return output

def predMiss(cusID, missing_m, id_dic, predData, fn, test):
    month = ['16463', '16494', '16522', '16553', '16583', '16614', '16644', '16675', '16706', '16736', '16767', '16797',
         '16828', '16859', '16888', '16919', '16949']
    output = []
    for miss in missing_m: # for each missing month
        test1 = [] # matrix to calculate weights
        test2 = [] # matrix to sum the weights
        prop = []

        idx = month.index(str(miss)) # Find index for stated missing month
        for k, v in id_dic.items(): # For each constituent of the predicted data
            test1.append(predData[k][idx])
            prop.append(v)
        for i in range(len(test1)):
            test2.append(calcRow(test1[i], prop[i], fn, test))
        out = [0] * 40
        for r in range(len(test2)):
            for c in range(len(fn)-2):
                out[c] += test2[r][c]
        out.insert(0, cusID)
        out.insert(0, miss)
        output.append(out)
    return (output)

def impute(date, id, test, numbers, comp_id, comp_data2d, fn, CusID, missing_m):
    output = []
    distances, indices = numbers.kneighbors(test)
    id_dic = lookID(indices, comp_id)
    predData = predictFrom(id_dic, comp_id, comp_data2d)
    oPred = predMiss(CusID, missing_m, id_dic, predData, fn, test)
    output.append(oPred)
    return output

def main(n, CI, testFile):


    trainFile = 'fitData.csv'

    '''
    trainfile = 'complete.csv'
    testFile = 'incomplete.csv'
    '''


    comp_id, comp_date, comp_data2d = getData(trainFile, CI)
    numbers =nn(n_neighbors=n, algorithm='auto').fit(comp_data2d)

    if CI == True:
        x = '_CI_only'
    else:
        x = ''

    with open(testFile, 'r') as f, open (("pred" + str(n) + x + testFile), 'w', newline= '') as wr1: #open (("padd" + x + testFile), 'w', newline= '') as wrP:
        inp = csv.reader(f, skipinitialspace=True, delimiter=',', quotechar='|')
        out1 = csv.writer(wr1, delimiter=",", quotechar='|')
        #outP = csv.writer(wrP, delimiter=",", quotechar='|')
        out = [out1]

        fn = next(inp)
        if CI == True:
            d = fn.index('SavingAcnt')
            del fn[d:]
        for o in out:
            o.writerow(fn)

        test = []
        date = []
        id = []
        x = 0

        for row in inp:
            if CI == True:
                del row[d:]
            if x == 0:
                date.append(int(float(row.pop(0))))
                id.append(row.pop(0))
                x = id[len(id)-1]
                test.append(row)
            elif x == row[1]:
                date.append(int(float(row.pop(0))))
                id.append(row.pop(0))
                test.append(row)
            else:
                output = []
                CusID = id[0]
                missing_m = missingM(date)
                output = impute(date, id, test, numbers, comp_id, comp_data2d, fn, CusID, missing_m)
                #output.append(padding(CusID, missing_m, date, test, fn))
                for i in range(len(output)):
                    for ans in output[i]:
                        out[i].writerow(ans)

                date, id, test = [], [], []
                date.append(int(float(row.pop(0))))
                id.append(row.pop(0))
                test.append(row)
                x = id[len(id) - 1]

        CusID = id[0]
        missing_m = missingM(date)
        output= []
        output = impute(date, id, test, numbers, comp_id, comp_data2d, fn, CusID, missing_m)
        #output.append(padding(CusID, missing_m, date, test, fn))
        for i in range(len(output)):
            for ans in output[i]:
                out[i].writerow(ans)

def accuracy(file1, file2):  # test for compare1.csv and pred1.csv
    fn = ["FetchDate", "CusID", "EmployeeIdx", "CntyOfResidence", "Sex",    #Fieldnames
                 "Age", "1stContract", "NewCusIdx", "Seniority", "CusType",
                 "RelationType", "ForeignIdx", "ChanEnter", "DeceasedIdx", "ProvCode",
                 "ActivIdx", "Income", "Segment",

              "SavingAcnt", "Guarantees",
                 "CurrentAcnt", "DerivativesAcnt", "PayrollAcnt", "JuniorAcnt", "MoreParticularAcnt",
                 "ParticularAcnt", "ParticularPlusAcnt", "ShortDeposit", "MediumDeposit", "LongDeposit",
                 "eAcnt", "Funds", "Mortgage", "Pensions", "Loans",
                 "Taxes", "CreditCard", "Securities", "HomeAcnt", "Payroll",
                 "PayrollPensions", "DirectDebit" ]
    df0 = pd.read_csv(file1, names= fn)
    df1 = pd.read_csv(file2, names=fn)
    df = [df0,df1]
    dm = []
    i = [0,0]
    dr = ["FetchDate", "CusID", "SavingAcnt", "Guarantees","CurrentAcnt",
          "DerivativesAcnt", "PayrollAcnt", "JuniorAcnt", "MoreParticularAcnt", "ParticularAcnt",
          "ParticularPlusAcnt", "ShortDeposit", "MediumDeposit", "LongDeposit", "eAcnt",
          "Funds", "Mortgage", "Pensions", "Loans", "Taxes",
          "CreditCard", "Securities", "HomeAcnt", "Payroll", "PayrollPensions", "DirectDebit" ]
    for d in df:
        d.drop(dr, inplace=True, axis=1)
        dm.append(d.as_matrix())
    if (len(dm[0]) == len(dm[1])):
        t = np.shape(dm[0])
        row = t[0]
        col = t[1]
        tot = row * col
        accu = 0
        for r in range(row):
            for c in range(col):
                if dm[0][r][c] == dm[1][r][c]:
                    accu +=1
        accuracy = round(float(accu/tot), 4)
        print (accuracy)
        return accuracy



            #return float(i[1]/i[0])
CI = [True]# True - only CI, no PI.  False - both CI and PI
proportion = [0.9, 0.1]
oriFile = 'complete1.csv'
testFile = ['test1.csv','test2.csv', 'test3.csv', 'test4.csv', 'test5.csv']
compareFile = ['compare1.csv','compare2.csv','compare3.csv','compare4.csv','compare5.csv']
#for i in range(len(testFile)) :
#    selectData('test0.csv', testFile[i], compareFile[i])
    # splitting to test for accuracy
#for c in CI:
#    for i in range(1, 36, 2):
#        main(i, c, 'test1.csv')

x = []
y = []
accu = []
comp = []
for i in range(2, 6):
    x.append(i-1)
    accu.append('paddtest'+str(i)+'.csv')
    comp.append(('compare'+str(i)+'.csv'))

#for n in range (17, 120, 17):

for a in range(len(accu)):
    y.append(accuracy(comp[a], accu[a]))


plt.plot(x, y, c = 'b', marker= 'o', linestyle='-')
plt.axis([0, 5, 0, 1])
plt.xlabel('trial')
plt.ylabel('Accuracy')
plt.show()