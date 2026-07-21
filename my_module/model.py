import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.tree import DecisionTreeClassifier

# Load the breast cancer dataset
cancer = load_breast_cancer()
X = cancer.data
y = cancer.target

# Train Decision Tree Classifier
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X, y)


def predict(input_features):
    # Convert the input list to a numpy array
    features_array = np.array([input_features])
    prediction = clf.predict(features_array)

    # Return the predicted class name malignant or benign
    return cancer.target_names[prediction][0]