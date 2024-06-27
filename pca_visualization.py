#Handwritten Digits Visualization
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.datasets import load_digits

# Load the digits dataset
digits = load_digits()
data = digits.data
target = digits.target

# Filter digits 2 and 3
mask = np.isin(target, [2, 3])
data = data[mask]
target = target[mask]

# Perform PCA
pca = PCA(n_components=2)
data_pca = pca.fit_transform(data)

# Plot the results
plt.scatter(data_pca[:, 0], data_pca[:, 1], c=target, cmap='viridis', edgecolor='k', s=40)
plt.title('PCA of Handwritten Digits (2s and 3s)')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.colorbar()
plt.show()
