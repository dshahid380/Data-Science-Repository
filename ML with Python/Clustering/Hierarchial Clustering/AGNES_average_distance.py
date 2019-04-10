# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 16:44:39 2018

@author: Abhik Banerjee

Given below is the code for implementing Agglomerative Nesting using Python. Agglomerative nesting falls under Hierarchial Clustering.
Here, AGNES is implemented using average distance metric. The same algorithm can be implmented using minimum distance and maximum distance 
metrics as well. 

This implementation is also known as 'Average Linkage' and is a 'bottom-up' approach.

Pass the dataframe and the number of cluster to form and then run 'job()'.
"""


class AGNES_single(object):
    def __init__(self,numClusters,df):
        self.numClusters=numClusters
        
        import numpy as np
        #self.df=np.unique(df,axis=0)
        self.df=df
        if type(self.df) is not list:
            self.df=self.df.tolist()
        
        
    def distance(p1,p2):
        import numpy as np
        d=[]
        for x in range(len(p1)):
            d.append((p1[x]-p2[x])**2)
        d=sum(d)**0.5
        return np.round(d,3)

    def distWrapper(l1,l2):
        import numpy as np
        if type(l1[0]) is list and type(l2[0]) is float:
            
            d=[]
            for x in l1:
                d.append(AGNES_single.distance(x,l2))
            return np.mean(d)
        
        elif type(l2[0]) is list and type(l1[0]) is float:
            
            d=[]
            for x in l2:
                d.append(AGNES_single.distance(x,l1))
            return np.mean(d)
        
        elif type(l1[0]) is list and type(l2[0]) is list:
            
            d=[]
            for x in l1:
                tem=[]
                for y in l2:
                    tem.append(AGNES_single.distance(x,y))
                d.append(np.mean(tem))
            return np.mean(d)
            
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
    def job(self): 
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
        return self.df
    
from sklearn.datasets import load_iris
d=load_iris()
df=d.data[:,0:3].tolist()

a=AGNES_single(14,df)
result=a.job()
