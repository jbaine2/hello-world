import numpy as np

import matplotlib.pyplot as plt

from scipy import linalg, interpolate, optimize, cluster


equation = np.array([[1,5,1], [3,7,2], [5,11,3]])
solution = np.array([[6], [9], [12]])
roots = linalg.solve(equation, solution)
print("Q1")
print(roots)


m = np.array([[1,2],[3,4]])

n = linalg.inv(m)
print(linalg.det(n))
print("Q2")

def f1(x):

    return x**3 + 1

# problem 3
measured_time = np.linspace(-1, 1, 10)
noise = (np.random.random(10)*2 - 1) * 1e-1
measures = f1(measured_time) + noise
plt.plot(measured_time, measures, 'bo', 'r-')
plt.savefig("test_1.png")
print("Q3)")




def f2(x, a, b):

  return a * np.exp(-b / x) + 10

measured_value_1 = np.linspace(0.5, 10, 50)
measured_value_2 = np.linspace(0.5, 10, 50)
measured_value_3 = np.linspace(0.5, 10, 50)

noise_2 = (np.random.random(10)*2 - 1) * 1e-1

measures_2 = f2(measured_value_1, measured_value_2, measured_value_3) + noise

a = np.random.multivariate_normal([10, 10], [[3, 1], [1, 4]], size=[100])
b = np.random.multivariate_normal([-5, -5], [[6, 1], [6, 4]], size=[100])

fitted_data = f2(measured_value_1, a, b)

plt.plot(measured_value_1, measures_2, 'bo')
plt.plot(noise, 'ro')
plt.plot(fitted_data, 'go')
plt.savefig("test_2.png")
print("Q4)")



a = np.random.multivariate_normal([10, 10], [[3, 1], [1, 4]], size=[100])

b = np.random.multivariate_normal([-5, -5], [[6, 1], [6, 4]], size=[100])

c = np.random.multivariate_normal([0, 0], [[6, 1], [6, 4]], size=[100])

d = np.random.multivariate_normal([-10, 10], [[6, 1], [6, 4]], size=[100])

data = np.concatenate((a, b, c, d))

centroids,output = cluster.vq.kmeans(data,4)

plt.scatter(data[:, 0], data[:, 1], data[:, 2], data[:, 3])
plt.scatter(centroids[:, 0], centroids[:, 1], centroids[:, 2], centroids[:, 3], c='r', s=100)

clx,output = cluster.vq.vq(data,centroids)

cluster_1 = []
cluster_2 = []
cluster_3 = []
cluster_4 = []

i = 0
for a in clx:
    if a == 0:
        cluster_1.append(data[i])
    elif a == 1:
        cluster_2.append(data[i])

    elif a == 2:
        cluster_3.append(data[i])

    else:
        cluster_4.append(data[i])

    i += 1

cluster_1 = np.array(cluster_1)
cluster_2 = np.array(cluster_2)
cluster_3 = np.array(cluster_3)
cluster_4 = np.array(cluster_4)

plt.scatter(cluster_1[:, 0], cluster_1[:, 1], cluster_1[:, 2], cluster_1[: 3])
plt.scatter(cluster_2[:, 0], cluster_2[:, 1], cluster_2[:, 2], cluster_2[: 3])
plt.scatter(cluster_3[:, 0], cluster_3[:, 1], cluster_3[:, 2], cluster_3[: 3])
plt.scatter(cluster_4[:, 0], cluster_4[:, 1], cluster_4[:, 2], cluster_4[: 3])


print("Q5")
