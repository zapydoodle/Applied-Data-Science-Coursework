from data_tools import extract_features, extract_labels
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn import metrics 
from scipy.stats import chi2_contingency, chi2
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.options.mode.chained_assignment = None  # default='warn'

class FeatureGroup:

    def __init__(self, data, study, description):
        self.data = data
        self.study = study
        self.description = description
        self.features = None
        self.label = None
        self.conmat = None
        self.tree = None


def feat_and_lab(data_csv_filename, balance=False):
    """
    Extract the features and labels from the dataframe
    """
    # Get dataframe
    data = pd.read_csv(data_csv_filename)

    # Balance data to have the same number of people who are depressed or not
    if balance:
        # Count the number of depressed and non depressed people
        dep_counts = data['has_dep_diag'].value_counts()
        not_dep_count = int(dep_counts[0])
        dep_count = int(dep_counts[1])
        not_dep_removal_num = not_dep_count-dep_count
        # Get all not depressed people 
        no_dep_people = data.loc[data["has_dep_diag"] == 0]
        # Choose some indexes at random to remove
        np.random.seed(10)
        drop_indices = np.random.choice(no_dep_people.index, not_dep_removal_num, replace=False)
        # Remove those indexes from the dataframe
        data.drop(drop_indices, inplace=True)

    # Extract features
    features_df = extract_features(data)

    # Take out sex
    features_df.drop(["sex"], axis=1, inplace=True)

    # Extract labels
    labels = extract_labels(data)

    # Pick out has_dep_diag
    label = pick_label(labels, 'has_dep_diag')

    return features_df, label

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

"""""""""""""""""""""
-SCREEN TIME SPLIT-
"""""""""""""""""""""

def screen_time_split(features, dataset):
    """
    Take in features dataframe and split into two
    one for screen-time features and one for non screen-time features
    """
    # List of screen time features (ALSPAC)
    alspac_screen = ["tv_bed_9","comp_games_bed","computer","phone","talk_mob","talk_phone","text","tv","fam_tv"]
    # List of non screen time features (ALSPAC)
    alspac_noscreen = ["mat_dep","mat_age","iq","pat_pres_10","pat_pres_8","pat_pres","agg_score","exercise","child_bull","musi_13","creat_14","alone","draw","abuse","music","outside_sum","outside_win","play","read","work","mother_anxiety"]
    # List of screen time features (MCS)
    mcs_screen = []
    # List of non screen time features (MCS)
    mcs_noscreen = []
    # Make dictionary from the lists
    label_dict = {"ALSPAC" : (alspac_screen, alspac_noscreen),
                  "MCS" : (mcs_screen, mcs_noscreen)}
    
    screentime_features = features.drop(label_dict[dataset][1], axis=1)
    noscreentime_features = features.drop(label_dict[dataset][0], axis=1)

    return screentime_features, noscreentime_features

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

def decision_tree(features, label, depth=3):

    # Train test split
    X_train, X_test, y_train, y_test = train_test_split(features, label, test_size=0.3, random_state=1, stratify=label) # 70% training and 30% test

    # Create Decision Tree classifer object
    clf = DecisionTreeClassifier(criterion='gini', class_weight='balanced', max_depth=depth, splitter='random')

    # Train Decision Tree Classifer
    clf = clf.fit(X_train,y_train)

    # Predict the response for test dataset
    y_pred = clf.predict(X_test)

    return y_pred, y_test, clf

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

def plot_conmat(conmat, ax):
    ax.imshow(conmat.T, cmap="cool")

    # Show all ticks and label them with the respective list entries
    ax.set_xticks(np.arange(2), labels=["No Dep", "Dep"])
    ax.set_yticks(np.arange(2), labels=["No Dep", "Dep"])

    ax.set(ylabel="Predicted", xlabel="Actual")

    # Loop over data dimensions and create text annotations.
    meanings = {(0,0) : "TN",
                (0,1) : "FP",
                (1,0) : "FN",
                (1,1) : "TP"}
    for i in range(2):
        for j in range(2):
            ax.text(j, i, str(round(conmat.T[j, i],2))+f" ({meanings[(i,j)]})",
                    ha="center", va="center", color="k")
            
    return ax