from sklearn import model_selection
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics

from main import data_file, dict_word, dict_categorie, three_before_and_after, \
    two_before_and_after, one_before_and_after


def naiveBayes_one(file, context_information_type):
    X, Y = one_before_and_after(data_file(file), dict_word(file), dict_categorie(file), context_information_type)
    X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=0.30,
                                                                        random_state=100)
    gnb = GaussianNB()
    gnb.fit(X_train, Y_train)
    Y_pred = gnb.predict(X_test)
    print("Accuracy:", metrics.accuracy_score(Y_test, Y_pred))

def naiveBayes_two(file, context_information_type):
    X, Y = two_before_and_after(data_file(file), dict_word(file), dict_categorie(file), context_information_type)
    X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=0.30,
                                                                        random_state=100)
    gnb = GaussianNB()
    gnb.fit(X_train, Y_train)
    Y_pred = gnb.predict(X_test)
    print("Accuracy:", metrics.accuracy_score(Y_test, Y_pred))


def naiveBayes_three(file, context_information_type):
    X, Y = three_before_and_after(data_file(file), dict_word(file), dict_categorie(file), context_information_type)
    X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=0.30,
                                                                        random_state=100)
    gnb = GaussianNB()
    gnb.fit(X_train, Y_train)
    Y_pred = gnb.predict(X_test)
    print("Accuracy:", metrics.accuracy_score(Y_test, Y_pred))

print("***Classifier: Naive Bayes with 1 word/category***")
print("Feature: words")
naiveBayes_one('interest.acl94.txt', 'words')
print("Feature: categories")
naiveBayes_one('interest.acl94.txt', 'categories')

print("***Classifier: Naive Bayes with 2 words/categories***")
print("Feature: words")
naiveBayes_two('interest.acl94.txt', 'words')
print("Feature: categories")
naiveBayes_two('interest.acl94.txt', 'categories')

print("***Classifier: Naive Bayes with 3 words/categories***")
print("Feature: words")
naiveBayes_three('interest.acl94.txt', 'words')
print("Feature: categories")
naiveBayes_three('interest.acl94.txt', 'categories')
