#Handwritten Digits Visualization

import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import KernelPCA
from sklearn.datasets import load_digits

# Load the digits dataset
digits = load_digits()
data = digits.data
target = digits.target

# Filter digits 2 and 3
mask = np.isin(target, [2, 3])
data = data[mask]
target = target[mask]

# Perform Kernel PCA
kpca = KernelPCA(n_components=2, kernel='rbf', gamma=0.04)
data_kpca = kpca.fit_transform(data)

# Plot the results
plt.scatter(data_kpca[:, 0], data_kpca[:, 1], c=target, cmap='viridis', edgecolor='k', s=40)
plt.title('Kernel PCA of Handwritten Digits (2s and 3s)')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.colorbar()
plt.show()
