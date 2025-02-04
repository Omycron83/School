import numpy as np
from random import choice

class KMeansClustering:
    def __init__(self, k, data) -> None:
        self.threshhold = 1e-6
        self.data = data
        self.means = data[np.random.choice(len(data), k, replace=False), :]
        self.get_means(data)

    def get_labels(self, data):
        distances = np.linalg.norm(data[:, np.newaxis] - self.means, axis=2)
        labels = np.argmin(distances, axis=1)
        return labels

    def get_nearest_category(self, data):
        return self.means[self.get_labels(data)]

    def get_means(self, data, iterations = 200):
        for i in range(iterations):
            labels = self.get_labels(data)
            new_means = np.array([data[labels == j].mean(axis=0) for j in range(len(self.means))])
            if np.linalg.norm(self.means - new_means) < self.threshhold:
                break
            else:
                self.means = new_means

def unit_test():
    z = np.random.rand(40, 40)
    g = KMeansClustering(20, z)
    x = g.get_labels(np.random.rand(40, 40))
    print(x)

if __name__ == '__main__':
    unit_test()