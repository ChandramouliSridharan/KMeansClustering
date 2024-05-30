# KMeansClustering
Implementing  k-means clustering on UCI_datasets without using Libarary implementing K-Means.

**Tasks Performed:**
  1. Program take one argument which is the path name of a file.
  2. Initialized the K-means clustering and ran the K-means clustering for a range of K values (2-10). Here we are using Eucledian Distance for calculating the distance betweeen centrid and data point
  3. Initial Centroid are taken at random where the random state = 0.
  4. For each cluster range, we perform 20 iterations.
  5. Calculated the SSE value after 20 iteration.
  6. Finally, graph is being plotted using Matplotlib that shows Error values (on the y-axis) corresponding to the different values of K clusters (on the x-axis).
