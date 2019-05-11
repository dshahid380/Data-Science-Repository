# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 16:44:39 2018

@author: Abhik Banerjee

Given below is the code for implementing Agglomerative Nesting using Python. Agglomerative nesting falls under Hierarchial Clustering.
Here, AGNES is implemented using minimum distance metric. The same algorithm can be implmented using average distance and maximum distance 
metrics as well. 

This implementation is also known as 'Single Linkage' and is a 'bottom-up' approach.

Pass the dataframe and the number of cluster to form and then run 'job()'.
"""


class AGNES_single(object):
    def __init__(self,dataframe,numClusters=0,radius=0,path=""):
        self.path=path
        import pandas
        if(type(dataframe)!=pandas.core.frame.DataFrame):
            raise TypeError
        self.numClusters=numClusters
        self.radius=radius
        self.df=dataframe.values.tolist()
        self.numAttri=len(self.df[0])
        self.numObs=len(self.df)
        import numpy as np
        self.df=np.unique(self.df,axis=0).tolist()
       
        
    def distance(p1,p2):
        import numpy as np
        d=[]
        for x in range(len(p1)):
            d.append((p1[x]-p2[x])**2)
        d=sum(d)**0.5
        return np.round(d,3)

    def distWrapper(l1,l2):
        if type(l1[0]) is list and type(l2[0]) is float:
            
            d=[]
            for x in l1:
                d.append(AGNES_single.distance(x,l2))
            return min(d)
        
        elif type(l2[0]) is list and type(l1[0]) is float:
            
            d=[]
            for x in l2:
                d.append(AGNES_single.distance(x,l1))
            return min(d)
        
        elif type(l1[0]) is list and type(l2[0]) is list:
            
            d=[]
            for x in l1:
                tem=[]
                for y in l2:
                    tem.append(AGNES_single.distance(x,y))
                d.append(min(tem))
            return min(d)
            
        else:
            #print('cond4')
            return AGNES_single.distance(l1,l2)
    def appendWrap(self,p1,p2):
        if type(p1[0]) is list and type(p2[0]) is list:
            #print('cond1')
            p1=p1+p2
            self.df.append(p1)
        elif type(p1[0]) is list:
            #print('cond2')
            p1.append(p2)
            self.df.append(p1)
        elif type(p2[0]) is list:
            #print('cond3')
            p2.append(p1)
            self.df.append(p1)
        else:
            #print('cond4')
            self.df.append([p1,p2])
        return self.df
    def radii(df):
        r=[]
        flag=True
        for x in df:
            if(type(x[0])==list):
                flag=False
                import numpy as np
                m=np.mean(x,axis=0)
                d=0
                for y in x:
                    d+=AGNES_single.distance(y,m)**2
                d/=len(x)
                d=d**0.5
                r.append(d)
        if(flag):
            return [0]
        else:
            return r
    def writeCluster(self,df):
        f=open(self.path,"w")
        for x in df:
            if type(x[0])==list:
                for y in x:
                    for z in y:
                        f.write(str(z)+"\t")
                    f.write(str(df.index(x))+"\n")
            else:
                for z in x:
                        f.write(str(z)+"\t")
                f.write(str(df.index(x))+"\n")
        f.close()
                    
            
    def clusterBased(self): 
        import numpy as np
        while(len(self.df)!=self.numClusters):
            distMatrix=[]
            
            for x in self.df:
                distMatrix.append([])#Appending the row for each point
                for y in self.df:
                    #print(x,y)
                    distMatrix[self.df.index(x)].append(AGNES_single.distWrapper(x,y))
                    if x==y:
                        break
            #to print the minimum distance between two points except the last distance in that row (which is 0)
            #print(distMatrix[distMatrix.index(np.min(distMatrix[1:],axis=0))].index(min(distMatrix[distMatrix.index(np.min(distMatrix[1:],axis=0))][:-1])))
            
            p1=distMatrix.index(np.min(distMatrix[1:],axis=0)) #gets the point along the row
            p2=distMatrix[p1].index(min(distMatrix[p1][:-1]))
            p1=self.df.pop(p1)
            p2=self.df.pop(p2)
            self.df=self.appendWrap(p1,p2)
            print("Number of Clusters:",len(self.df))
        if self.path=="":
            return self.getResults()
        else:
            self.writeCluster(self.df)
    def radiusBased(self):
        import numpy as np
        r=AGNES_single.radii(self.df)
        while(max(r)<self.radius):
            distMatrix=[]
            print("Cluster Radii:",r)
            for x in self.df:
                distMatrix.append([])#Appending the row for each point
                for y in self.df:
                    #print(x,y)
                    distMatrix[self.df.index(x)].append(AGNES_single.distWrapper(x,y))
                    if x==y:
                        break
            #to print the minimum distance between two points except the last distance in that row (which is 0)
            #print(distMatrix[distMatrix.index(np.min(distMatrix[1:],axis=0))].index(min(distMatrix[distMatrix.index(np.min(distMatrix[1:],axis=0))][:-1])))
            
            p1=distMatrix.index(np.min(distMatrix[1:],axis=0)) #gets the point along the row
            p2=distMatrix[p1].index(min(distMatrix[p1][:-1]))
            p1=self.df.pop(p1)
            p2=self.df.pop(p2)
            self.df=self.appendWrap(p1,p2)
            r=AGNES_single.radii(self.df)
            print("Number of Clusters:",len(self.df))
        if self.path=="":
            return self.getResults()
        else:
            self.writeCluster(self.df)
    def getdict(df):
        d={}
        for x in df:
            d[df.index(x)]=x
        return d
    def getResults(self):
        #return AGNES_single.getdict(self.df)
        return self.df
    
    def __str__(self):
        return "Single-Linkage Clustering Algorithm.\nGive the Data in form of Dataframe. Then, you have 2 choices:\n\
    1>Select the Number of Clusters (by numClusters parameter) and then execute the self.clusterBased() job\n\
    2>Select the Max Radius of the Clusters (by radius parameter) and then execute the self.radiusBased() job."+\
    "The result of any job is returned as a list of clusters left at the end of the job.\n\n   Info:\nNumber of Clusters Selected="+str(self.numClusters)+\
    "\nMax Radius of the Clusters="+str(self.radius)+"\n\nNo. of Attributes in Data-"+str(self.numAttri)+\
    "\nNo. of Observations in Data-"+str(self.numObs)
    
import pandas as pd
#d=pd.read_csv('C:/Users/USER/Downloads/wine.data',header=None)
#df=d.iloc[:,1:13].values.tolist()
from sklearn.datasets import load_iris
d=load_iris()
d=pd.DataFrame(d.data)
df=d.iloc[:,0:2]

a=AGNES_single(df,numClusters=10,path="d:/test.txt")
a.clusterBased()
result=a.getResults()

#The code below is for Vizualization of the result
color_codes=('#008000','#ADFF2F','#FF6A6A','#FFF68F','#F08080','#FF8000','#FFFF00','#FF3E96','#FF6347','#63B8FF','#97FFFF','#CAFF70','#8B6508','#FFB90F','#FFF8DC','#76EE00','#98F5FF','#8A360F','#A52A2A','#0000FF','#000000')
import matplotlib.pyplot as plt

#plt.style.use('ggplot2')
for x in result:
    if type(x[0])==list:
        for y in x:
            plt.scatter(y[0],y[1],color=color_codes[result.index(x)])
    else:
        plt.scatter(x[0],x[1],color=color_codes[result.index(x)])
plt.show()
             
             
