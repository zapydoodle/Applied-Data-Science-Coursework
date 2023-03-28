"""
Python file for functions used to help with the data when analysing/running models
"""

def extract_features(data):
    """
    Extract features from the data (note this only works with Data.csv)

    Input
    --------------
    data : dataframe
        dataframe to extract the features from

    Output
    --------------
    features : dataframe
        dataframe containing the extracted features
    """
    # Define the label columns to drop (quicker than specifying the features to keep)
    labels = [
        'dep_band_15',
        'dep_band_13',
        'dep_band_10',
        'dep_band_07',
        'anx_band_15',
        'anx_band_13',
        'anx_band_10',
        'anx_band_07',
        'has_dep_diag',
        'secd_diag',
        'prim_diag',
        'panic_score',
        'dep_score',
        'X'
    ]

    # Remove the labels from the data frame
    features = data.drop(labels, axis=1)

    return features

def extract_labels(data):
    """
    Extract labels from the data (note this only works with Data.csv)

    Input
    --------------
    data : dataframe
        dataframe to extract the labels from

    Output
    --------------
    labels : dataframe
        dataframe containing the extracted features
    """
    # Define the label columns
    labels = [
        'dep_band_15',
        'dep_band_13',
        'dep_band_10',
        'dep_band_07',
        'anx_band_15',
        'anx_band_13',
        'anx_band_10',
        'anx_band_07',
        'has_dep_diag',
        'secd_diag',
        'prim_diag',
        'panic_score',
        'dep_score'
    ]

    # Select these columns as a new dataframe
    labels = data[labels]

    return labels 