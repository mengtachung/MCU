#### K nearest neighbor ####

from math import sqrt
 
# calculate the Euclidean distance between two vectors
def euclidean_distance(row1, row2):
	distance = 0.0
	for i in range(len(row1)-1):
		distance += (row1[i] - row2[i])**2
	return sqrt(distance)
 
# Locate the most similar neighbors
def get_neighbors(train, test_row, num_neighbors):
	distances = list()
	for train_row in train:
		dist = euclidean_distance(test_row, train_row)
		distances.append((train_row, dist))
	distances.sort(key=lambda tup: tup[1])
	neighbors = list()
	for i in range(num_neighbors):
		neighbors.append(distances[i][0])
	return neighbors
 
# Make a classification prediction with neighbors
def predict_classification(train, test_row, num_neighbors):
	neighbors = get_neighbors(train, test_row, num_neighbors)
	output_values = [row[-1] for row in neighbors]
	prediction = max(set(output_values), key=output_values.count)
	return prediction
 
# Test distance function
dataset = [[161, 61, 0],    #### Herself
                [158, 58, 0],
                [158, 59, 0],
                [158, 63, 0],
                [160, 59, 0],
                [160, 60, 0],
                [163, 60, 0],
                [163, 61, 0],
                [160, 64, 1],
                [163, 64, 1],
                [165, 61, 1],
                [165, 62, 1],
                [165, 65, 1],
                [168, 62, 1],
                [168, 63, 1],
                [168, 66, 1],
                [170, 63, 1],
                [170, 64, 1],
                [170, 68,1]]
neighbors = get_neighbors(dataset, dataset[0], 6)    #### K=5
for neighbor in neighbors:
        print(neighbor)

