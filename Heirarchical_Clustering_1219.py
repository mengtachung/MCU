import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage  
from matplotlib import pyplot as plt
X = np.array([[1,1],  
    [1.5,1.5],
    [5,5],
    [3,4],
    [4,4],
    [3,3.5],])


labels = range(1, 7)  
plt.figure(figsize=(10, 7))  
plt.subplots_adjust(bottom=0.1)  
plt.scatter(X[:,0],X[:,1], label='True Position')

for label, x, y in zip(labels, X[:, 0], X[:, 1]):  
    plt.annotate(
        label,
        xy=(x, y), xytext=(-3, 3),
        textcoords='offset points', ha='right', va='bottom')
plt.show()  

#from scipy.cluster.hierarchy import dendrogram, linkage  
#from matplotlib import pyplot as plt

linked = linkage(X, 'single')

labelList = range(1, 7)

plt.figure(figsize=(10, 7))  
dendrogram(linked,  
            orientation='top',
            labels=labelList,
            distance_sort='descending',
            show_leaf_counts=True)
plt.show() 
