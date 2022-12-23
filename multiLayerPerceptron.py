from sklearn import model_selection
from sklearn.neural_network import MLPClassifier
from sklearn import metrics

from main import data_file, dict_word, dict_categorie, two_before_and_after


def multiLayerPerceptron(file, context_information_type):
    X, Y = two_before_and_after(data_file(file), dict_word(file), dict_categorie(file), context_information_type)
    X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=0.30,
                                                                        random_state=100)
    clf100 = MLPClassifier(hidden_layer_sizes=(10, 10, 10), random_state=1, max_iter=1000).fit(X_train, Y_train)
    clf100_pred = clf100.predict(X_test)
    clf100.score(X_test,Y_test)

   # clf100 = MLPClassifier(hidden_layer_sizes=100, random_state=1, max_iter=1000).fit(X_train, Y_train)
    #clf100_pred = clf100.predict(X_test)
    #clf100.score(X_test, Y_test)

    print("Accuracy:", metrics.accuracy_score(Y_test, clf100_pred))

print("Feature: words")
multiLayerPerceptron('interest.acl94.txt', 'words')
print("Feature: categories")
multiLayerPerceptron('interest.acl94.txt', 'categories')