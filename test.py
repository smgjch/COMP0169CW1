import numpy as np

# Modify X to include pairwise terms up to the 2nd degree
def modify_X(X):
    # Get the number of samples and the number of original features
    num_samples, num_features = X.shape
    
    # Initialize an empty feature matrix with zeros
    X_modified = np.zeros((num_samples, num_features * (num_features + 1) // 2))
    
    # Populate the modified feature matrix with pairwise terms
    col = 0
    for i in range(num_features):
        for j in range(i, num_features):
            print(i,j)
            X_modified[:, col] = X[:, i] * X[:, j]
            col += 1
    
    return X_modified

# Example usage
X = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  # Example X with 3 variables
X_modified = modify_X(X)

print(X_modified)
