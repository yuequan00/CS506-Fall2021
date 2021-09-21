import random

# Question 1
def import_data(filename):
    X=[]
    y=[]
    f = open(filename, 'r')
    lines = f.readlines()

    #len of lines =280
    #converting to list of list
    wholeList = []
    for line in lines:
        list = []
        for l in line.split("\n"):
            list.append(l)
        wholeList.append(list)
    #set it to regular list of list
    O = []
    for row in range(len(wholeList)):
        O.append([wholeList[row][0]])
        for num in O[row]:
            l=[]
            count=1
            for i in num.split(","):
                if (count == 280):
                    if (i == "?"):
                        y.append("NaN")
                    else:
                        y.append(float(i))
                elif (i == "?"):
                    l.append("NaN")
                else:
                    l.append(float(i))
                count+=1
            X.append(l)
    return X,y
                    
# Question 2(a)
def impute_missing(input): 
    nanList = []
    nanColumn = []
    for row in range(len(input)):
        for col in range(len(input[0])):
            if (input[row][col] == 'NaN'):
                if (len(nanColumn)==0):
                    nanColumn.append(col)
                else:
                    # if temp=true, 'nan'col does not exist at current nanList list, need to be added
                    temp = True
                    for i in nanColumn:
                        if (i==col):
                            temp = False
                    if (temp):
                        nanColumn.append(col)
                            
                nanList.append([row,col]) 

    # j is the index of nanColumn
    j=0
    for i in nanColumn:
        median = 0
        r = 0
        for row in range(len(input)):
            if (isinstance(input[row][i],float)):
                median += input[row][i]
            r += 1
        median = median/r
        nanColumn[j] = [i,median]
        j+=1

    for i in nanList:
        #i[0]->row #, i[1]->column #
        #j[0]->nancolumn,j[1]-> median of nancolumn
        for j in nanColumn:
            if (j[0]==i[1]):
                input[i[0]][i[1]] = j[1]
    return input

#2(b) Answer: When experiencing outliers in the data set, median is more accurate than the mean.

#2(c)
def discard_missing(X, y ):
    X1 = []
    y1 = []
    for row in X:
        i=True
        for item in row:
            if (item == "NaN"):
                i = False
        if (i):
            X1.append(row)
    for item in y:
        if (item != "NaN"):
            y1.append(item)
    X = X1
    y = y1
    return X,y

#3(a)
def shuffle_data ( X, y ):
    random.shuffle(X)
    random.shuffle(y)
    return X,y

#3(b)
def compute_std( X ):
    if (isinstance(X[0], list)):
        std_X = [0]*(len(X[0]))
        for col in range(len(X[0])):
            sum_ = 0
            for row in range (len(X)):
                sum_ += X[row][col]
            mean = sum_/len(X)
            for row in range(len(X)):
                x_i = X[row][col]
                std_X[col] += (x_i - mean) * (x_i - mean)
            std_X[col] = (std_X[col]/(len(X))-1)**0.5
        return std_X
    else:
        std_y = 0
        mean = sum(X)/len(X)
        for col in range(len(X)):
            x_i = X[col]
            std_y += (x_i - mean) * (x_i - mean)
        std_y = (std_y/(len(X)-1))**0.5
        return std_y
#3(c)
#helper function -> compute mean in advance
def mean(X):
    if (isinstance(X[0], list)):
        l = [0]*len(X[0])
        for col in range(len(X[0])):
            sum_ = 0
            for row in range (len(X)):
                sum_ += X[row][col]
            mean = sum_/len(X)
            l[col] = mean
        return l
    else:
        mean = 0
        mean = sum(X)/len(X)
    return mean

def remove_outlier ( X, y ):
    X1 = []
    y1 = []
    std_X = compute_std(X)
    std_y = compute_std(y)
    mean_X = mean(X)
    mean_y = mean(y)
    for row in range(len(X)):
        temp = True
        for col in range(len(X[0])):
            # upper and lower are complex numberes
            upper = mean_X[col]+ (2*(std_X[col]))
            upper = int(upper.real)
            lower = mean_X[col]-(2*(std_X[col]))
            lower =  int(lower.real)
            if ((X[row][col] > upper) or (X[row][col] < lower)):
                temp = False
        if (temp):
            X1.append(X[row])
    for item in y:
        if (item < (mean_y+ 2*std_y)) or (item > (mean_y- 2*std_y)):
            y1.append(item)
    return X1,y1

#3(d)
#The time complexity for this function is O(n^2)
def standardize_data ( X ):
    mean_X = mean(X)
    std = compute_std(X)
    for row in range(len(X)):
        for col in range(len(X[0])):
            X[row][col] = (X[row][col] - mean_X[col])/std[col]
    return X

#4
def import_data_nonNum(filename):
    X=[]
    y=[]
    f = open(filename, 'r')
    lines = f.readlines()
    #converting to list of list
    wholeList = []
    for line in lines:
        list = []
        for l in line.split("\n"):
            list.append(l)
        wholeList.append(list)
    #set it to regular list of list
    O = []
    for row in range(len(wholeList)):
        O.append([wholeList[row][0]])
        # adding values to generate new list
        first_row = 0
        for num in O[row]:
            l=[]
            count=1
            for i in num.split(","):
                if ((count == 4 )or (count == 9) or (count == 11)):
                    continue
                elif(first_row == 0):
                    if (count == 2):
                        y.append(str(i))
                    else:
                        l.append(str(i))
                elif (count == 2):
                        y.append(float(i))
                elif (count ==5):
                    if (i=='female'):
                        l.append(int(0))
                    elif (i=='male'):
                        l.append(int(1))
                    else:
                        l.append('NaN')
                elif (count ==12):
                    if (i=='C'):
                        l.append(int(0))
                    elif (i=='Q'):
                        l.append(int(1))
                    elif(i=='S'):
                        l.append(int(2))
                    else:
                        l.append('NaN')
                elif (i == "?"):
                    l.append("NaN")
                else:
                    l.append(float(i))
                count+=1
            X.append(l)
            first_row += 1
    return X,y
# name ticket carbin feathers

#5(a)
def train_test_split( X, y, t_f ):
    X_train = []
    y_train = []
    X_test = []
    y_test = []
    # only randomly change the order of the row - change the order of user's data
    randomlist = random.sample(range(0, len(X)), int((len(X)-1)*t_f))
    for i in range (len(X)):
        if (i == 0):
            X_train.append(X[0])
            X_test.append(X[0])
            y_train.append(y[0])
            y_test.append(y[0])
        else:
            temp = True
            for randomNum in randomlist:
                if (i == randomNum):
                    X_train.append(X[i])
                    y_train.append(y[i])
                    temp = False
            if (temp):
                X_test.append(X[i])
                y_test.append(y[i])

    return X_train, y_train, X_test, y_test
#5(b)
def train_test_CV_split( X, y, t_f, cv_f ): 
    X_train = []
    y_train = []
    X_test = []
    y_test = []
    X_cv = []
    y_cv = []
    randomlist = random.sample(range(0, len(X)), int((len(X)-1)*t_f))
    # make random num in a list with cross-validation
    cv_f_randomlist = randomlist[:int(len(X)*cv_f)]
    # make random num in a list with test/train
    t_f_randomlist = randomlist[int(len(randomlist)*cv_f):]
    for i in range (len(X)):
        if (i == 0):
            X_train.append(X[0])
            X_test.append(X[0])
            y_train.append(y[0])
            y_test.append(y[0])
            X_cv.append(X[0])
            y_cv.append(y[0])
        else:
            temp = True
            for t_f_randomNum in t_f_randomlist:
                if (i == t_f_randomNum):
                    X_train.append(X[i])
                    y_train.append(y[i])
                    temp = False
            for cv_f_randomNum in cv_f_randomlist:
                if (i == cv_f_randomNum):
                    X_cv.append(X[i])
                    y_cv.append(y[i])
                    temp = False
            if (temp):
                X_test.append(X[i])
                y_test.append(y[i])
    return X_train, y_train, X_test, y_test, X_cv, y_cv

def main():
    #Q1
    a_file = open("q1.txt", "w")
    data = import_data("./arrhythmia.data")
    print('Question 1: import data \n', data,file=a_file)
    a_file.close()
    # #Q2(a)
    a_file = open("q2a.txt", "w")
    X = data[0]
    y = data[1]
    print('Question 2(a): impute missing data in median value\n', impute_missing(X),file=a_file)
    a_file.close()
    #Q2(b)
    a_file = open("q2b.txt", "w")
    print('Answer for 2(b): When experiencing outliers in the data set, median is more accurate than the mean.\n',file=a_file)
    a_file.close()
    #Q2(c)
    a_file = open("q2c.txt", "w")
    print('Question 2(c): discard samples with missing valuess\n', discard_missing(X,y),file=a_file)
    a_file.close()
    df = discard_missing(X,y)
    X1 = df[0]
    y1 = df[1]
    #Q3(a)
    a_file = open("q3a.txt", "w")
    print('Question 3(a): shuffles the order of data entries \n', shuffle_data ( X1, y1 ),file=a_file)
    a_file.close()
    #Q3(b)
    a_file = open("q3b.txt", "w")
    print('Question 3(b): standard deviation of value: \n',compute_std( X1 ),file=a_file)
    a_file.close()
    # y_std = compute_std( y)

    #Q3(c)
    a_file = open("q3c.txt", "w")
    print('Question 3(c): remove outliers \n',remove_outlier(X1,y1),file=a_file)
    a_file.close()

    #Q3(d)
    a_file = open("q3d.txt", "w")
    print('Question 3(d): The time complexity for this function is O(n^2) \n standardized data \n',standardize_data(X1),file=a_file)
    a_file.close()

    #Q4
    a_file = open("q4.txt", "w")
    data = import_data_nonNum("./train.csv")
    print('Question 4: import data \n', data[0],file=a_file)
    a_file.close()

    #Q5(a)
    X = data[0]
    y = data[1]
    dt = train_test_split(X,y, 0.4)
    X_train = dt[0]
    y_train = dt[1]
    X_test = dt[2]
    y_test = dt[3]
    a_file = open("q5a.txt", "w")
    print('Question 5: train data of X is: \n',X_train , '\n train data of y is : \n',y_train, '\n test data of X is: \n',X_test, 
    '\n test data for y is: \n', y_test, file=a_file)
    a_file.close()

    #Q5(b)
    dt = train_test_CV_split( X, y, 0.4, 0.1 )
    X_train = dt[0]
    y_train = dt[1]
    X_test = dt[2]
    y_test = dt[3]
    X_cv = dt[4]
    y_cv = dt[5]
    a_file = open("q5b.txt", "w")
    print('Question 5: train data of X is: \n',X_train , '\n train data of y is : \n',y_train, '\n test data of X is: \n',X_test, 
    '\n test data for y is: \n', y_test, '\n cross-validation data for X is: \n',X_cv, '\n cross-validation data for y is: \n',y_cv,
    file=a_file)
    a_file.close()

main()

# TODO: 3c, 4