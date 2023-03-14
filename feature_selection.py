# method for feature selection is from the following sources
# idea: http://venom.cs.utsa.edu/dmz/techrep/2007/CS-TR-2007-011.pdf
# python implementation: https://stats.stackexchange.com/questions/108743/methods-in-r-or-python-to-perform-feature-selection-in-unsupervised-learning 

"""
PFA is an unsupervised learning technique which selects features using only the feature data
It is non-deterministic as it uses k-means, therefore to robustly select the most important
features it is important for the PFA to be ran for a number of iterations, then pick the most
common features that come up as the most important 
"""

from pfa import PFA
import numpy as np

def feature_selection(n_features, features):
    """
    Function to select features using the PFA technique

    Inputs
    -------
    n_features : int
        Desired number of feautures to select from the data
    features : array
        Numpy array of data, rows are datapoints and columns are features
    
    Returns
    --------
    top_features : list
        Column index of the selected features
    """

    # Initialise things
    iterations = 100                                            # Number of times to perform PFA 
    count = 0                                                   
    column_indices_mat = np.empty([iterations, n_features])     # Empty matrix to store the results of PFA analysis 

    # Perform pfa for as many iterations as are specified above, save the results each time in column_indices_mat array
    while count < iterations:
        # Create pfa
        pfa = PFA(n_features)
        # Fit with features
        pfa.fit(features)
        # Features array with selected feautures
        X = pfa.features_
        # Indices of selected columns 
        column_indices = pfa.indices_
        column_indices_mat[count,:] = column_indices
        count += 1

    # See which features are most commonly suggested as the most important ones
    column_indices_mat = column_indices_mat.astype(int)
    freq = np.bincount(column_indices_mat.flatten())
    freq = np.asarray(freq)
    
    # Initialise list for storing the index of the top features
    top_features = []

    # Add the most frequently selected features to the top features list 
    while len(top_features) < n_features:
        idx = np.argmax(freq)
        top_features.append(idx)
        freq[idx] = 0

    # Sort list 
    top_features.sort()

    return top_features
