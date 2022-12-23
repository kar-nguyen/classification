from sklearn import model_selection
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics


from main import data_file, dict_word, dict_category, two_before_and_after


def decisionTree(file, context_information_type):
    X, Y = two_before_and_after(data_file(file), dict_word(file), dict_category(file),context_information_type)
    X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=0.30)
    clf = DecisionTreeClassifier().fit(X_train, Y_train)
    Y_pred = clf.predict(X_test)
    y_accuracy = metrics.accuracy_score(Y_test, Y_pred)
    print("Accuracy:", "%.2f" % (y_accuracy * 100), "%")

print("*** Classifier: Decision Tree ***")
print("Feature: words")
decisionTree('interest.acl94.txt', 'words')
print("Feature: categories")
decisionTree('interest.acl94.txt', 'categories')
