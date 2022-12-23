from sklearn import model_selection
from sklearn.neural_network import MLPClassifier
from sklearn import metrics

from main import data_file, dict_word, dict_category, two_before_and_after


def multiLayerPerceptron3(file, context_information_type):
    X, Y = two_before_and_after(data_file(file), dict_word(file), dict_category(file), context_information_type)
    X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=0.30)
    #TODO choisir plusieurs valeurs de couches cachees
    clf3 = MLPClassifier(hidden_layer_sizes=(10, 10, 10), max_iter=1000).fit(X_train, Y_train)
    clf3_pred = clf3.predict(X_test)
    clf3.score(X_test,Y_test)
    clf3_accuracy = metrics.accuracy_score(Y_test, clf3_pred)

   # clf100 = MLPClassifier(hidden_layer_sizes=100, random_state=1, max_iter=1000).fit(X_train, Y_train)
    #clf100_pred = clf100.predict(X_test)
    #clf100.score(X_test, Y_test)

    print("Accuracy:", "%.2f" % (clf3_accuracy * 100), "%")


def multiLayerPerceptron2(file, context_information_type):
    X, Y = two_before_and_after(data_file(file), dict_word(file), dict_category(file), context_information_type)
    X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=0.30)
    #TODO choisir plusieurs valeurs de couches cachees
    clf2 = MLPClassifier(hidden_layer_sizes=(10, 10), max_iter=1000).fit(X_train, Y_train)
    clf2_pred = clf2.predict(X_test)
    clf2.score(X_test,Y_test)
    clf2_accuracy = metrics.accuracy_score(Y_test, clf2_pred)

    print("Accuracy:", "%.2f" % (clf2_accuracy * 100), "%")


def multiLayerPerceptron1(file, context_information_type):
    X, Y = two_before_and_after(data_file(file), dict_word(file), dict_category(file), context_information_type)
    X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=0.30)
    #TODO choisir plusieurs valeurs de couches cachees
    clf1 = MLPClassifier(hidden_layer_sizes=10, max_iter=1000).fit(X_train, Y_train)
    clf1_pred = clf1.predict(X_test)
    clf1.score(X_test,Y_test)
    clf1_accuracy = metrics.accuracy_score(Y_test, clf1_pred)

    print("Accuracy:", "%.2f" % (clf1_accuracy * 100), "%")


# TODO changer le x pour le nombre correct de couches cachees
print("***Classifier: Multi Layer Perceptron with 3 hidden layers***")
print("Feature: words")
multiLayerPerceptron3('interest.acl94.txt', 'words')
print("Feature: categories")
multiLayerPerceptron3('interest.acl94.txt', 'categories')

print("***Classifier: Multi Layer Perceptron with 2 hidden layers***")
print("Feature: words")
multiLayerPerceptron2('interest.acl94.txt', 'words')
print("Feature: categories")
multiLayerPerceptron2('interest.acl94.txt', 'categories')

print("***Classifier: Multi Layer Perceptron with 1 hidden layers***")
print("Feature: words")
multiLayerPerceptron1('interest.acl94.txt', 'words')
print("Feature: categories")
multiLayerPerceptron1('interest.acl94.txt', 'categories')