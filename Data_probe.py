### Simple EDA, probe and understand the data ###

import pandas as pd
import numpy as np

def checkList (list, input): # Modify Index Function
    try:
        list.index(input)
    except ValueError:
        return -1
    else:
        return list.index(input)

def getData (filename): # Import data
    dic = {
        'FetchDate':int, 'CusID':int,
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
    df = pd.read_csv(filename, header=0, dtype=dic)
    df.describe()
    arr = df.as_matrix()
    return arr

def countM (Mcounter, month, inp): # Number of data at each month
    idx = checkList(month, inp)
    Mcounter[idx] += 1
    return Mcounter

def countChange(changeCounter, test, fn): # Calculate frequency of binary change
    row = len(test) - 1
    column = len(fn)
    x = [0] * (len(changeCounter))
    for r in range(row):
        for c in range (column):
            if test[r][c] != test[r+1][c]:
                x[c]+=1
    for i in range(len(x)):
        changeCounter[i] += float(x[i]/(row+1))
        changeCounter[i] = round(changeCounter[i], 2)
    return  changeCounter

def countOnes(oneCount, test, fn): # Calculate frequency of specific product ownership
    for t in test:
        for i in range(len(t)):
            if t[i] == 1:
                oneCount[i] +=1
    return oneCount

def probe(filename): # Main
    month =[16463, 16494, 16522, 16553, 16583, 16614, 16644, 16675, 16706, 16736, 16767, 16797,
            16828, 16859, 16888, 16919, 16949]
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
    compCounter = [0, 0]
    Mcounter = [0] * (len(month))
    changeCount_comp = [0] * (len(fn))
    changeCount_incomp = [0] * (len(fn))
    oneCount_comp = [0]*(len(fn))
    oneCount_incomp = [0]*(len(fn))
    empIdx = [[0,0,0,0,0],[0,0,0,0,0]]
    data = getData(filename)
    dimension = np.shape(data)
    nrows = dimension[0]
    ncolumns = dimension [1]
    test = []
    x = data[0][1]


    for r in range(nrows):
        if data[r][1] == x:
            test.append(data[r])
        else:
            if len(test)==17:
                compCounter[0] +=1
                changeCount_comp = countChange(changeCount_comp, test, fn)
                oneCount_comp = countOnes(oneCount_comp, test, fn)
            else:
                compCounter[1] +=1
                Mcounter = countM(Mcounter, month, data[r][0])
                changeCount_incomp = countChange(changeCount_incomp, test, fn)
                oneCount_incomp = countOnes(oneCount_incomp, test, fn)
            #do sth
            test = []
            test.append(data[r])
            x = data[r][1]
    Change = [[],[]]
    for x in range(len(changeCount_incomp)):
        y = round(changeCount_incomp[x] / compCounter[1], 4)
        z = round(changeCount_comp[x] / compCounter[0], 4)
        Change[1].append(y)
        Change[0].append(z)

    print ('Mcounter: ' + str(Mcounter))
    print ('compCounter: ' + str(compCounter))
    print ('changeCount[0]: ' + str(changeCount_comp))
    print(Change[0])
    print ('changeCount[1]: ' + str(changeCount_incomp))
    print(Change[1])
    print('oneCount_comp: ' + str(oneCount_comp))
    print('oneCount_incomp' + str(oneCount_incomp[fn.index('SavingAcnt'):]))

probe('sorted.csv')

