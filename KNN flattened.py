from sklearn.neighbors import NearestNeighbors as nn
import random as rd
import numpy as np
import pandas as pd
import csv


def write(data, testFile, fn):
    with open(testFile, 'w', newline='') as wr:
        out = csv.writer(wr, delimiter=",", quotechar='|')
        out.writerow(heading())
        for d in data:
            out.writerow(d)


def splitData(proportion, filename):
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
    fn = ["FetchDate", "CusID", "EmployeeIdx", "CntyOfResidence", "Sex",  # Fieldnames
          "Age", "1stContract", "NewCusIdx", "Seniority", "CusType",
          "RelationType", "ForeignIdx", "ChanEnter", "DeceasedIdx", "ProvCode",
          "ActivIdx", "Income", "Segment",

          "SavingAcnt", "Guarantees",
          "CurrentAcnt", "DerivativesAcnt", "PayrollAcnt", "JuniorAcnt", "MoreParticularAcnt",
          "ParticularAcnt", "ParticularPlusAcnt", "ShortDeposit", "MediumDeposit", "LongDeposit",
          "eAcnt", "Funds", "Mortgage", "Pensions", "Loans",
          "Taxes", "CreditCard", "Securities", "HomeAcnt", "Payroll",
          "PayrollPensions", "DirectDebit"]
    df = pd.read_csv(filename, header=0, dtype=dic)
    data = df.as_matrix()
    rowsNum = len(data)
    custNum = rowsNum / 17
    for i in range(len(proportion)):
        proportion[i] = round(proportion[i] * custNum, 0) * 17
    output1 = flattenData(data[:int(proportion[0])])
    write(output1, 'flattened_fitData.csv', fn)


def randSelect():
    out1, out2 = [], []
    rand = rd.randint(1, 15)
    idx = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    for r in range(rand):
        i = rd.randint(0, len(idx) - 1)
        out1.append(idx.pop(i))
    for i in idx:
        if checkList(out1, i) == -1:
            out2.append(i)
    return out1, out2


def selectData(testData, testFile, comparefile):
    x = testData[0][1]
    test = []
    fn = ["FetchDate", "CusID", "EmployeeIdx", "CntyOfResidence", "Sex",  # Fieldnames
          "Age", "1stContract", "NewCusIdx", "Seniority", "CusType",
          "RelationType", "ForeignIdx", "ChanEnter", "DeceasedIdx", "ProvCode",
          "ActivIdx", "Income", "Segment",

          "SavingAcnt", "Guarantees",
          "CurrentAcnt", "DerivativesAcnt", "PayrollAcnt", "JuniorAcnt", "MoreParticularAcnt",
          "ParticularAcnt", "ParticularPlusAcnt", "ShortDeposit", "MediumDeposit", "LongDeposit",
          "eAcnt", "Funds", "Mortgage", "Pensions", "Loans",
          "Taxes", "CreditCard", "Securities", "HomeAcnt", "Payroll",
          "PayrollPensions", "DirectDebit"]
    with open(testFile, 'w', newline='') as wr1, open(comparefile, 'w', newline='') as wr2:
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


def sortData(filein):
    df = pd.read_csv(filein)
    df = df.sort_values(['CusID', 'FetchDate'], ascending=[True, True])
    df.to_csv('test1.csv', index=False, sep=',', encoding='utf-8')


def checkList(list, input):
    try:
        list.index(input)
    except ValueError:
        return -1
    else:
        return list.index(input)


def getData(file, CI):
    m = ['16463', '16494', '16522', '16553', '16583', '16614', '16644', '16675', '16706', '16736', '16767', '16797',
         '16828', '16859', '16888', '16919', '16949']
    ave = []

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
    df = pd.read_csv(file, header=0, dtype=dic)

    for i in range(1,18):
        df.drop(["FetchDate"+str(i),"CusID"+str(i)], axis=1, inplace=True)
    if CI == True:
        for i in range(1,18):
            df.drop(["SavingAcnt"+str(i), "Guarantees"+str(i),
                 "CurrentAcnt"+str(i), "DerivativesAcnt"+str(i), "PayrollAcnt"+str(i), "JuniorAcnt"+str(i), "MoreParticularAcnt"+str(i),
                 "ParticularAcnt"+str(i), "ParticularPlusAcnt"+str(i), "ShortDeposit"+str(i), "MediumDeposit"+str(i), "LongDeposit"+str(i),
                 "eAcnt"+str(i), "Funds"+str(i), "Mortgage"+str(i), "Pensions"+str(i), "Loans"+str(i),
                 "Taxes"+str(i), "CreditCard"+str(i), "Securities"+str(i), "HomeAcnt"+str(i), "Payroll"+str(i),
                 "PayrollPensions"+str(i), "DirectDebit"+str(i)], axis=1, inplace=True)
    head = list(df)
    for h in head:
        ave.append(df[h].mean())

    data2d = df.as_matrix()
    output2d = np.array(data2d)
    return ave, head, output2d


def lookID(indices, comp_id):
    id = []
    out = {}
    s = 0
    for i in indices:
        for x in i:
            if checkList(id, comp_id[x]) == -1:
                id.append(comp_id[x])
                out[comp_id[x]] = 1
            else:
                out[comp_id[x]] += 1
            s += 1
    for k, v in out.items():
        out[k] = float(v / s)
    return out


def checkDraw(id_dic):
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


def predictFrom(indices, comp_data2d):  # returns index of comp data to predict from
    out = []
    for i in indices:
        out.append(comp_data2d[i])
    return out


def calcRow(predData, head):  # output ave from predData
    output = []
    arr = np.array(predData)
    df = pd.DataFrame(data=arr, columns=head)
    df = df.convert_objects(convert_numeric=True)
    for h in head:
        output.append(df[h].mean())
    return output




def padRow(row, fn):
    out = []
    out.append(row[(fn.index("EmployeeIdx") - 2)])
    out.append(row[(fn.index("CntyOfResidence") - 2)])
    out.append(row[(fn.index("Sex") - 2)])
    out.append(row[(fn.index("Age") - 2)])
    out.append(row[(fn.index("1stContract") - 2)])
    out.append(row[(fn.index("NewCusIdx") - 2)])
    out.append(row[(fn.index("Seniority") - 2)])
    out.append(row[(fn.index("CusType") - 2)])
    out.append(row[(fn.index("RelationType") - 2)])
    out.append(row[(fn.index("ForeignIdx") - 2)])
    out.append(row[(fn.index("ChanEnter") - 2)])
    out.append(row[(fn.index("DeceasedIdx") - 2)])
    out.append(row[(fn.index("ProvCode") - 2)])
    out.append(row[(fn.index("ActivIdx") - 2)])
    out.append(row[(fn.index("Income") - 2)])
    out.append(row[(fn.index("Segment") - 2)])
    return out


def closeDate(month, missing_m, miss, date):
    x = 1000
    out = 0
    idx = checkList(month, miss)
    for i in range(idx):
        if checkList(missing_m, int(month[i])) == -1:
            out = int(month[i])
    output = checkList(date, out)
    return output


def padding(cusID, missing_m, date, test, fn):
    month = ['16463', '16494', '16522', '16553', '16583', '16614', '16644', '16675', '16706', '16736', '16767', '16797',
             '16828', '16859', '16888', '16919', '16949']
    output = []
    for miss in missing_m:  # for each missing month
        idx = closeDate(month, missing_m, miss, date)
        out = padRow(test[idx], fn)
        out.insert(0, cusID)
        out.insert(0, miss)
        output.append(out)
    return output


def predMiss(cusID, missing_m, averaged, head, data, fn, test, date):
    month = ['16463', '16494', '16522', '16553', '16583', '16614', '16644', '16675', '16706', '16736', '16767', '16797',
             '16828', '16859', '16888', '16919', '16949']
    output = []
    for miss in missing_m:  # for each missing month
        test2 = []  # matrix to sum the weights
        test2.append(miss)
        test2.append(cusID)

        h = int(len(head)/17)
        idx = month.index(str(miss))  # Find index for stated missing month
        start = int(idx * (len(head) / 17))
        end = int(start + h)

        for i in range(start, end):
            test2.append(averaged[i])
        output.append(test2)

    cons = ['Sex', '1stContract', 'Age','Seniority', 'Income' ]
    for o in output:
        min = 20
        idx1 = month.index(o[0])
        for m in month:
            if checkList(missing_m, m)==-1:
                idx2 = month.index(m)
                if abs(idx1-idx2) < min:
                    min = abs(idx1-idx2)
                    closeIdx = date.index(float(m))
        for f in fn[:fn.index('SavingAcnt')]:
            o[int(fn.index(f))] = round(float(o[(fn.index(f))]), 0)
        for c in cons:
            o[int(fn.index(c))] = test[closeIdx][int(fn.index(c)-2)]
    return output


def impute(date, id, data, numbers, comp_data2d, head, CusID, missing_m, fn, test):
    output = []
    distances, indices = numbers.kneighbors([data])
    indices = indices.flatten()
    predData = predictFrom(indices, comp_data2d)
    averaged = calcRow(predData, head)
    oPred = predMiss(CusID, missing_m, averaged, head, data, fn, test, date)
    output.append(oPred)
    return output

def heading():
    head = []
    fn = ["FetchDate", "CusID", "EmployeeIdx", "CntyOfResidence", "Sex",  # Fieldnames
          "Age", "1stContract", "NewCusIdx", "Seniority", "CusType",
          "RelationType", "ForeignIdx", "ChanEnter", "DeceasedIdx", "ProvCode",
          "ActivIdx", "Income", "Segment",

          "SavingAcnt", "Guarantees",
          "CurrentAcnt", "DerivativesAcnt", "PayrollAcnt", "JuniorAcnt", "MoreParticularAcnt",
          "ParticularAcnt", "ParticularPlusAcnt", "ShortDeposit", "MediumDeposit", "LongDeposit",
          "eAcnt", "Funds", "Mortgage", "Pensions", "Loans",
          "Taxes", "CreditCard", "Securities", "HomeAcnt", "Payroll",
          "PayrollPensions", "DirectDebit"]
    for i in range(17):
        for f in fn:
            head.append((f + str(i + 1)))
    return head

def flattenData(data):
    test, output = [], []
    x = data[0][1]
    for row in data:
        if row[1] == x:
            test.append(row)
        else:
            print(test[0][1])
            arr = np.array(test)
            out = arr.flatten()
            output.append(out)

            x = row[1]
            test = []
            test.append(row)

    arr = np.array(test)
    out = arr.flatten()
    output.append(out)
    return output

def flattenTest(test, date, ave, head):
    month = ['16463', '16494', '16522', '16553', '16583', '16614', '16644', '16675', '16706', '16736', '16767', '16797',
             '16828', '16859', '16888', '16919', '16949']
    out = []
    for m in month:
        if checkList(date, int(float(m))) == -1:
            h = int(len(head) / 17)
            idx = month.index(m)  # Find index for stated missing month
            start = int(idx * (len(head) / 17))
            end = int(start + h)
            temp = []
            for i in range(start, end):
                temp.append(ave[i])
            out.append(temp)
        else:
            idx = date.index(int(m))
            out.append(test[idx])
    output = np.array(out)
    output = output.flatten()
    return output

def convInt(row):
    for i in range(len(row)):
        row[i] = (float(row[i]))
    return row

def main(n, CI):
    trainFile = 'flattened_fitData.csv'
    testFile = 'test1.csv'

    '''
    trainfile = 'complete.csv'
    testFile = 'incomplete.csv'
    '''

    ave, head, comp_data2d = getData(trainFile, CI)
    numbers = nn(n_neighbors=n, algorithm='auto').fit(comp_data2d)

    if CI == True:
        x = '_flattened_CI_only'
    else:
        x = '_flattened'

    with open(testFile, 'r') as f, open("pred" + str(n) + x + ".csv", 'w', newline='') as wr1:  # open ("padd1.csv", 'w', newline= '') as wrP:
        inp = csv.reader(f, skipinitialspace=True, delimiter=',', quotechar='|')
        out1 = csv.writer(wr1, delimiter=",", quotechar='|')
        # outP = csv.writer(wrP, delimiter=",", quotechar='|')
        out = [out1]

        fn = next(inp)
        for o in out:
            o.writerow(fn)

        test = []
        date = []
        id = []
        x = 0

        for row in inp:
            if CI == True:
                del row[fn.index('SavingAcnt'):]
            if x == 0:
                date.append(int(float(row.pop(0))))
                id.append(row.pop(0))
                x = id[len(id) - 1]
                test.append(convInt(row))
            elif x == row[1]:
                date.append(int(float(row.pop(0))))
                id.append(row.pop(0))
                test.append(convInt(row))
            else:
                CusID = id[0]
                missing_m = missingM(date)
                data = flattenTest(test, date, ave, head)
                output = impute(date, id, data, numbers, comp_data2d, head, CusID, missing_m, fn, test)
                # output.append(padding(CusID, missing_m, date, test, fn))
                for i in range(len(output)):
                    for ans in output[i]:
                        out[i].writerow(ans)

                date, id, test = [], [], []
                date.append(int(float(row.pop(0))))
                id.append(row.pop(0))
                test.append(convInt(row))
                x = id[len(id) - 1]

        CusID = id[0]
        missing_m = missingM(date)
        data = flattenTest(test, date, ave, head)
        output = impute(date, id, data, numbers, comp_data2d, head, CusID, missing_m, fn, test)
        for i in range(len(output)):
            for ans in output[i]:
                out[i].writerow(ans)


def accuracy(file):  # test for compare1.csv and pred1.csv
    df0 = pd.read_csv('compare1_flattened.csv')
    df1 = pd.read_csv(file)
    df = [df0, df1]
    dm = []
    i = [0, 0]
    dr = ["FetchDate", "CusID", "SavingAcnt", "Guarantees", "CurrentAcnt",
          "DerivativesAcnt", "PayrollAcnt", "JuniorAcnt", "MoreParticularAcnt", "ParticularAcnt",
          "ParticularPlusAcnt", "ShortDeposit", "MediumDeposit", "LongDeposit", "eAcnt",
          "Funds", "Mortgage", "Pensions", "Loans", "Taxes",
          "CreditCard", "Securities", "HomeAcnt", "Payroll", "PayrollPensions", "DirectDebit"]
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
                    accu += 1
        accuracy = round(float(accu / tot), 4)
        print(accuracy)
        return accuracy



        # return float(i[1]/i[0])


for i in range(1, 36, 2):
    main(i, False)
'''
CI = True  # True - only CI, no PI.  False - both CI and PI
proportion = [0.9, 0.1]
oriFile = 'complete1.csv'
testFile = ['test1.csv', 'test2.csv', 'test3.csv', 'test4.csv', 'test5.csv']
compareFile = ['compare1.csv','compare2.csv','compare3.csv','compare4.csv','compare5.csv']
selectData(splitData(proportion, oriFile), testFile)  # splitting to test for accuracy

x = [0,1,2,3,4,5,6,7,8,9,10,17,34,51,68,85,102,119]
y = []
accu = ['padd1.csv', 'pred1.csv', 'pred2.csv', 'pred3.csv', 'pred4.csv', 'pred5.csv', 'pred6.csv', 'pred7.csv', 'pred8.csv' ,'pred9.csv', 'pred10.csv',
        'pred17.csv', 'pred34.csv', 'pred51.csv', 'pred68.csv', 'pred85.csv', 'pred102.csv', 'pred119.csv']

#for n in range (17, 120, 17):

for a in accu:
    y.append(accuracy(a))


plt.plot(x, y, c = 'r', marker= 'o', linestyle='-')
plt.axis([0, 120, 0, 1])
plt.show()
'''