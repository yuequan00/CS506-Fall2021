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
    std = []
    if (isinstance(X[0], list)):
        for col in range(len(X[0])):
            mean = sum(X[:][col])/len(X[:][col])
            for row in range(len(X)):
                x_i = X[row][col]
                std[col] += (x_i - mean) * (x_i - mean)
            std[col] = (std[col]/(len(X[:][col])-1))**0.5
    else:
        mean = sum(X)/len(X)
        for col in range(len(X)):
            x_i = X[col]
            std += (x_i - mean) * (x_i - mean)
        std = (std/(len(X)-1))**0.5
    return std

#3(c)
#helper function -> compute mean in advance
def mean(X):
    mean = []
    if (isinstance(X[0], list)):
        for col in range(len(X[0])):
            m = sum(X[:][col])/len(X[:][col])
            mean[col] = m
    else:
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
            if ((X[row][col] > (mean_X[col]+ 2*(std_X[col]))) or (X[row][col] < (mean_X[col]-2*(std_X[col])))):
                temp = False
        if (temp):
            X1[row] = X[row]
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

def main():
    #Q1
    data = import_data("./arrhythmia.data")
    X = data[0]
    y = data[1]
    
    #Q2(a)
    # print(impute_missing(X))
    #Q2(c)
    # print(discard_missing(X,y))
    #Q3(a)
    # print(shuffle_data ( X, y ))
    #Q3(b)
    d = discard_missing(X,y)
    y=d[1]
    print(compute_std( y ))
    #Q3(c)
    # print(remove_outlier(X,y))
    #Q3(d)
    # print(standardize_data(X))

main()