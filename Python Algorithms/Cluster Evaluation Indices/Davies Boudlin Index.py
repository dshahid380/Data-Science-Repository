
"""
Implementation of Davies Boudlin Index Score.

Provide the clusters as a nested list. Where each list inside the varriable 'clusters' represents a specific cluster. 
The points inside the cluster should be n-dimensional lists as well.

The value of 'p' determines the distance measure used to evaluate the indices.
p=1 gives Manhattan Distance while p=2 gives Euclidean Distance.

The method returns a list of scores of the clusters passed in order in the 'clusters' list.

Code by Abhik Banerjee.
"""

def davies_bouldin_index(clusters,p):
    
    import numpy as np
    
    numCluster=len(clusters)
    
    meansList=[]
    
    intraClusterDistance=[]
    
    for eachCluster in clusters:
        
        clusterMean=np.array(np.mean(eachCluster,axis=0))
        
        distance=0
        
        for eachPoint in eachCluster:
            
            eachPoint=np.array(eachPoint)
            
            distance+= (eachPoint**p)-(clusterMean**2)
            
        averageDistance=(distance/len(eachCluster))**(1/p)
        
        intraClusterDistance.append(averageDistance)
        
        meansList.append(clusterMean)
    
    #interClusterSeparation is a dictionary that maps the distance between (cluster1,cluster2) 
    interClusterSeparation={}
    for eachMean1 in meansList:
        for eachMean2 in meansList:
            if eachMean1!=eachMean2:
                interClusterSeparation[(meansList.index(eachMean1),meansList.index(eachMean2))]=(eachMean1**p-eachMean2**p)**(1/p)
            
    DBIScore=[]
    for clusterIndex1 in range(numCluster):
        r=[]
        for clusterIndex2 in range(numCluster):
            
            if clusterIndex1 != clusterIndex2:
                
                r.append((intraClusterDistance[clusterIndex1]+intraClusterDistance[clusterIndex2])/interClusterSeparation[(clusterIndex1,clusterIndex2)])
                
        DBIScore.append(np.max(r))   
    
    return DBIScore
                
    
    
    