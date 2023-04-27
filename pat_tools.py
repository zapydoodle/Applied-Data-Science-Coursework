from data_tools import extract_features, extract_labels
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn import metrics 
from sklearn.ensemble import RandomForestClassifier
from scipy.stats import chi2_contingency, chi2
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.options.mode.chained_assignment = None  # default='warn'

def feat_and_lab(data_csv_filename):
    """
    Extract the features and labels from the dataframe
    """
    # Get dataframe
    data = pd.read_csv(data_csv_filename)

    # Extract features
    features_df = extract_features(data)

    # Take out sex
    features_df.drop(["sex"], axis=1, inplace=True)

    # Extract labels
    labels = extract_labels(data)

    return features_df, labels

def impute_features(features_df, imp_strategy='most_frequent'):
    """
    Impute missing data
    """
    # Save feature names before imputer takes them away
    feature_names = list(features_df.columns)

    # Create our imputer to replace missing values with the mode
    imp = SimpleImputer(missing_values=np.nan, strategy=imp_strategy)
    features_array = imp.fit(features_df).transform(features_df)

    features = pd.DataFrame(features_array, columns = feature_names)

    return features

def pick_label(dataframe, label_name):
    # Take has_dep_diag column
    label = dataframe[label_name]
    return label

"""""""""""""""""""""""""""
-CHI-SQUARED INDEPENDENCE-
"""""""""""""""""""""""""""

def independence_test(features, labels, chosen_label):
    """
    Performs an independence test for each feature in the dataframe
    and returns a list of bools for the independence of each feature
    """
    # Extract label you're using
    label = pick_label(labels, chosen_label)

    # Initialise independence list
    dependence_dict = {}

    # Loop through features
    for column in features:
        # Get the entries for each row
        feature = features[column]
        # Make a contingency table
        contingency_tab = pd.crosstab(feature, label)
        # Perform chi2 contingency function
        stat, p, dof, expected = chi2_contingency(contingency_tab)
        # Check for independence
        prob = 0.80
        critical = chi2.ppf(prob, dof)
        # Update dependence list
        if abs(stat) >= critical:
            dependence_dict[column] = True
        else:
            dependence_dict[column] = False

    return dependence_dict

"""""""""""""""""""""
--MACHINE LEARNING--
"""""""""""""""""""""

def decision_tree(features, labels, chosen_label, depth=3):
    # Take has_dep_diag column
    has_dep = pick_label(labels, chosen_label)

    # Train test split
    X_train, X_test, y_train, y_test = train_test_split(features, has_dep, test_size=0.3, random_state=1, stratify=has_dep) # 70% training and 30% test

    # Assign weights for class imbalance
    no_dep_num = len(y_train[y_train==0])
    dep_num = len(y_train[y_train==1])
    total = len(y_train)
    weights = {0:dep_num/total, 1:no_dep_num/total}

    # Create Decision Tree classifer object
    clf = DecisionTreeClassifier(criterion='entropy', class_weight=weights, max_depth=depth)

    # Train Decision Tree Classifer
    clf = clf.fit(X_train,y_train)

    # Predict the response for test dataset
    y_pred = clf.predict(X_test)

    return y_pred, y_test, clf
   

def random_forest(features, labels, chosen_label):
    # Take has_dep_diag column
    has_dep = pick_label(labels, chosen_label)

    # Train test split
    X_train, X_test, y_train, y_test = train_test_split(features, has_dep, test_size=0.3, random_state=1, stratify=has_dep) # 70% training and 30% test

    # Assign weights for class imbalance
    no_dep_num = len(y_train[y_train==0])
    dep_num = len(y_train[y_train==1])
    total = len(y_train)
    weights = {0:dep_num/total, 1:no_dep_num/total}

    # Create Random Forest Classifier object
    clf = RandomForestClassifier(max_depth=3, criterion='entropy', class_weight=weights)

    # Random Forest Classifier
    clf = clf.fit(X_train,y_train)

    # Predict the response for test dataset
    y_pred = clf.predict(X_test)

    return y_pred, y_test


def make_conmat(y_pred, y_test, normalised=True):
    """
    Returns a confusion matrix
    """
    # Confusion matrix
    tn, fp, fn, tp = metrics.confusion_matrix(y_test, y_pred).ravel()
    if normalised:
        conmat = np.array([[tn/(tn+fn), fp/(tp+fp)],[fn/(tn+fn),tp/(tp+fp)]])
    else:
        conmat = np.array([[tn, fp],[fn,tp]])

    return conmat

def plot_conmat(conmat):
    # Plot confusion matrix
    fig, ax = plt.subplots(figsize=(3,3), dpi=100)

    im = ax.imshow(conmat.T, cmap="cool")

    # Show all ticks and label them with the respective list entries
    ax.set_xticks(np.arange(2), labels=["No depression", "Depression"])
    ax.set_yticks(np.arange(2), labels=["No depression", "Depression"])

    ax.set(ylabel="Predicted", xlabel="Actual")

    # Loop over data dimensions and create text annotations.
    meanings = {(0,0) : "TN",
                (0,1) : "FP",
                (1,0) : "FN",
                (1,1) : "TP"}
    for i in range(2):
        for j in range(2):
            text = ax.text(j, i, str(round(conmat.T[j, i],2))+f" ({meanings[(i,j)]})",
                        ha="center", va="center", color="k")

    plt.show()