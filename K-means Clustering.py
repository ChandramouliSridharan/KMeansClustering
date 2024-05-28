import numpy as np
import os
import random
import matplotlib.pyplot as plt
import sys
import time

# Reading the file by removing the last column.
def read_data(file_path):
    with open(file_path, 'r') as file:
        data = []    
        for line in file:
            line_data = list(map(float, line.strip().split()))
            data.append(line_data[:-1])
    return data

# Calculating the initial centroid for each Cluster.
def initial_centroids(clusters_count, data_points):
    # random.seed(0)
    centroids = random.sample(data_points, clusters_count)
    clusters, data_points = assign_clusters(clusters_count, data_points, centroids)
    return clusters, data_points
    
# Assigning the data points to their cluster centroids based on the minimum eucledian distance.
def assign_clusters(clusters_count, data_points, centroids):
    clusters = [[] for _ in range(clusters_count)]
    for data_point in data_points:
        distances = []
        for centroid in centroids:
            distances.append(calculate_euclidean_distance(data_point, centroid))
        index = np.argmin(distances)
        clusters[index].append(data_point)
    return clusters, data_points

# Updating the centroid by calculating the average of the points in the cluster.
def update_centroids(k, no_of_dimensions, clusters):
    centroids = [[0] * no_of_dimensions for _ in range(k)]
    for index in range(k):
        if len(clusters[index]) > 0:
            for point_index in range(len(clusters[index])):
                 for dimension in range(no_of_dimensions):
                    centroids[index][dimension] += clusters[index][point_index][dimension]        
    for index in range(k):
        if len(clusters[index]) > 0:
            for dimension in range(no_of_dimensions):
                centroids[index][dimension] /= len(clusters[index])
    return centroids

# Calculating the euclidean distance between two data points.
def calculate_euclidean_distance(point1, point2):
    differences = []
    squares = []
    for i in range(len(point1)):
        differences.append(point1[i] - point2[i])
    for difference in differences:
        squares.append(difference ** 2)
    sum_squares = sum(squares)
    total_distance = sum_squares ** 0.5
    return total_distance


# Calculating the SSE value.
def calculate_sse(clusters_count, clusters, centroids):
    error = []
    for index in range(clusters_count):
        if len(clusters[index]) > 0:
            sse_distance = []
            for point_index in range(len(clusters[index])):
                sse_distance.append(calculate_euclidean_distance(clusters[index][point_index], centroids[index]))
            error.append(sum(sse_distance))
    sum_of_error = sum(error)
    return sum_of_error

# Plotting the graph with SSE vs Cluster count
def plotGraph(clusters_count, sse_values):
    plt.plot(list(clusters_count), sse_values, marker='o', color='red', linestyle='-')
    plt.xlabel("Number of Clusters")
    plt.ylabel("SSE Value")
    plt.title(f"K-Means Clustering: SSE Value vs Numbers of Clusters")
    plt.grid(True)
    plt.show()
    
def main():
    start_time = time.time()
    random.seed(0)
    file_path = sys.argv[1]
    if os.path.exists(file_path):
        data = read_data(file_path)
    else:
        print("File doesn't exist!!")
        
    clusters_count = range(2, 11)
    no_of_iterations = 20
    ssevalues =[]
    
    # Performing K-Means clustering for Cluster count 2 to 10.
    for k in clusters_count:
        clusters, data_points = initial_centroids(k, data)
        no_of_dimensions = len(data_points[0])   

        #  Perform 20 iterations for each Cluster count.
        for _ in range(no_of_iterations):
            # Updates the centroid and assign the datapoint.
            centroids = update_centroids(k, no_of_dimensions, clusters) 
            clusters, data_points = assign_clusters(k, data_points, centroids)   

        # Calculating the Sum of Squared Error value after 20 iterations. 
        sse = calculate_sse(k, clusters, centroids)
        print(f"For k = {k} After {no_of_iterations} iterations: Error = {sse:.4f}")
        ssevalues.append(sse)
    
    # Visualizing the SSE Error vs Cluster using Graph.
    plotGraph(clusters_count, ssevalues)
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    main()

