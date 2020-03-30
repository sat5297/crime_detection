import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

%matplotlib inline

df1 = pd.read_csv('dataset_part1.csv')
##so I HAVE ALL the dataset with the following crimes to be removed.

##cleaning the dataset1 for including the crimes
##the dataset_split1 which we chose from df2 will be treated

def cleandata():
    ctr = 0
    ctr1 = 0
    for ele in df1.iloc[:,2]:
        f = 0
        print("The crime in dataset :: ",ele)
        for elem in crimes:
            if elem == ele:
                    print(elem,"  " ,ele)
                    f=1
                    break
        print("THe flag val :: " , f)
        if f == 0: 
            print("Dropping initiated")
            df1.drop(df1.index[ctr],inplace=True)
        if f == 1:
            print("NO drop needed")
            ctr += 1
        print(ctr," ",f)
        ctr1+=1
    print("Greg")
    print("Count of ones :: ",ctr1)


cleandata()


df1.to_csv('data1.csv')


##generalising the dataset
##the reduced dataset is being generalised in this attempt

# this will replace "Boston Celtics" with "Omega Warrior" 
#df.replace(to_replace ="Boston Celtics", 
                 #value ="Omega Warrior") 

def generalizeData():
    ctr = 0
    ctr1 = 0
    for elem in df1.iloc[:,2]:
        print(elem)
        for ele,val in crime_dictionary.items():
            print(ele,"  " , val)
            df1.replace(to_replace=elem, 
                        value = val,inplace=True)

generalizeData()

