from mlxtend.evaluate import plot_learning_curves
from sklearn import datasets
from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeClassifier
import numpy as np



def test_training_size():

    iris = datasets.load_iris()
    X = iris.data
    y = iris.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.6, random_state=2)

    clf = DecisionTreeClassifier(max_depth=1, random_state=1)
    training_errors, test_errors = plot_learning_curves(X_train, y_train, X_test, y_test, clf, kind='training_size', suppress_plot=True)

    desired1 = [0.32, 0.33, 0.32, 0.33, 0.30, 0.31, 0.31, 0.22, 0.22, 0.22]
    desired2 = [0.35, 0.35, 0.35, 0.35, 0.43, 0.45, 0.35, 0.35, 0.45, 0.45]

    np.testing.assert_almost_equal(training_errors, desired1, decimal=2)
    np.testing.assert_almost_equal(test_errors, desired2, decimal=2)




def test_scikit_metrics():

    iris = datasets.load_iris()
    X = iris.data
    y = iris.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.6, random_state=2)

    clf = DecisionTreeClassifier(max_depth=1, random_state=1)
    training_errors, test_errors = plot_learning_curves(X_train, y_train, X_test, y_test, clf, kind='training_size', suppress_plot=True, scoring='accuracy')

    desired1 = [0.68, 0.67, 0.68, 0.67, 0.7, 0.69, 0.69, 0.78, 0.78, 0.78]
    desired2 = [0.65, 0.65, 0.65, 0.65, 0.57, 0.55, 0.65, 0.65, 0.55, 0.55]

    np.testing.assert_almost_equal(training_errors, desired1, decimal=2)
    np.testing.assert_almost_equal(test_errors, desired2, decimal=2)



def test_n_features():

    iris = datasets.load_iris()
    X = iris.data
    y = iris.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.6, random_state=2)

    clf = DecisionTreeClassifier(max_depth=1, random_state=1)
    training_errors, test_errors = plot_learning_curves(X_train, y_train, X_test, y_test, clf, kind='n_features', suppress_plot=True)

    desired1 = [0.40, 0.40, 0.32, 0.32]
    desired2 = [0.42, 0.42, 0.35, 0.35]

    np.testing.assert_almost_equal(training_errors, desired1, decimal=2)
    np.testing.assert_almost_equal(test_errors, desired2, decimal=2)