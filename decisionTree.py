from sklearn import model_selection
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics


from main import data_file, dict_word, dict_category, two_before_and_after


def decisionTree(file, context_information_type):
    X, Y = two_before_and_after(data_file(file), dict_word(file), dict_category(file),context_information_type)
    X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, train_size=0.80, test_size=0.20,
                                                                        random_state=50)
    clf = DecisionTreeClassifier(max_depth=3, random_state=50).fit(X_train, Y_train)
    Y_pred = clf.predict(X_test)
    print("Accuracy:", metrics.accuracy_score(Y_test, Y_pred))

print("***Classifier: Decision Tree***")
print("Feature: words")
decisionTree('interest.acl94.txt', 'words')
print("Feature: categories")
decisionTree('interest.acl94.txt', 'categories')
