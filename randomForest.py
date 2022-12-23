from sklearn import model_selection
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics

from main import data_file, dict_word, dict_category, two_before_and_after


def random_forest(file, context_information_type):
    X, Y = two_before_and_after(data_file(file), dict_word(file), dict_category(file), context_information_type)
    X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=0.30,
                                                                        random_state=100)

    forest = RandomForestClassifier(n_estimators=100, random_state=100)
    forest.fit(X_train, Y_train)
    Y_pred = forest.predict(X_test)
    print("Accuracy:", metrics.accuracy_score(Y_test, Y_pred))

print("***Classifier: Random Forest***")
print("Feature: words")
random_forest('interest.acl94.txt', 'words')
print("Feature: categories")
random_forest('interest.acl94.txt', 'categories')