import pandas as pd
import numpy as np
import random
import math
import matplotlib.pyplot as plt

#### Data 
#d = {'X1':[1,1.5,5,3,4,3], 'X2':[1,1.5,5,4,4,3.5]}    #### Hierarchical clustering example
d = [15, 15, 16, 19, 19, 20, 20, 21, 22, 28, 35, 40, 41, 42, 43, 44, 60, 61, 65]
df = pd.DataFrame(data=d)

#################################
def calRandomCentroids(k, df):
    centroids = []
    for i in range(k):
        rand = random.randint(0,len(df)-1)
        randVal = tuple(df.loc[rand].values)
        while randVal in centroids:
            rand = random.randint(0,len(df)-1)
            randVal = tuple(df.loc[rand].values)
        else:
            centroids.append(randVal)
    return centroids
#######################################
def calDist(a,b):
    return math.sqrt(sum((np.array(a)-np.array(b))**2))

def makeClusters(k, df, centroids):
    clusters = {}
    for tup in centroids:
        clusters[tup] = []
    for i in range(len(df)):
        pointDists = {}
        for tup in centroids:
            dist = calDist(tuple(df.loc[i].values),tup)
            pointDists[dist] = tup
        ncp = pointDists.get(min(pointDists)) 
        clusters[ncp].append(i) #or i
    return clusters  
#########################################
def calNewCentroids(clusters):
    newcentroids = []
    for k in clusters:
        sumc = 0
        for l in range(len(clusters[k])):
            sumc += df.loc[clusters[k][l]]
        cent = sumc/len(clusters[k])
        newcentroids.append(tuple(cent))
    return newcentroids
##############################################
def checkConvergence(k,oldcentroids,newcentroids):
    result = []
    for i in range(k):
        rs = calDist(oldcentroids[i],newcentroids[i])
        result.append(rs)
    print("convergence result is {}".format(result))
    count = 0
    for i in range(len(result)):
        if result[i] <= 0.5:
            count = count+1
    return True if count == len(result) else False 
####################################################
def kMeans(k, df):
    
    centroids = calRandomCentroids(k, df)
    print("random centroids are {}".format(centroids))
    oldcentroids = centroids
    
    clusters = makeClusters(k, df, oldcentroids)
    print("first iter clusters are {}".format(clusters))   
    
    newcentroids = calNewCentroids(clusters)
    print("new centroids are {}".format(newcentroids))
    
    res = checkConvergence(k,oldcentroids,newcentroids)
    print(res)
    
    while res == False:
        oldcentroids = newcentroids
        clusters = makeClusters(k, df, oldcentroids)
        print("further iter clusters are {}".format(clusters))   
        newcentroids = calNewCentroids(clusters)
        res = checkConvergence(k,oldcentroids,newcentroids)
        print(res)
    else:
        print("Final clusterings are {}".format(clusters))    
    

kMeans(2, df) ######### K=2
