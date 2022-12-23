from sklearn import model_selection
from sklearn import svm
from sklearn.metrics import accuracy_score, f1_score
from sklearn.svm import LinearSVC

from main import data_file, dict_word, dict_category, two_before_and_after


def svm_classifer(file, context_information_type):
    X, Y = two_before_and_after(data_file(file), dict_word(file), dict_category(file),context_information_type)
    X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=0.30)
    rbf = svm.SVC().fit(X_train, Y_train)

    #TODO : peut-etre choisir d'autres degres pour les polynomes jsp
    poly1 = svm.SVC(kernel='poly', degree=1).fit(X_train, Y_train)
    poly2 = svm.SVC(kernel='poly', degree=2).fit(X_train, Y_train)
    poly3 = svm.SVC(kernel='poly', degree=3).fit(X_train, Y_train)


    #linear = LinearSVC(C=1, multi_class='ovr', max_iter=5000).fit(X_train, Y_train)

    rbf_pred = rbf.predict(X_test)
    poly1_pred = poly1.predict(X_test)
    poly2_pred = poly2.predict(X_test)
    poly3_pred = poly3.predict(X_test)

    #lin_pred = linear.predict(X_test)

    rbf_accuracy = accuracy_score(Y_test, rbf_pred)
    print('Accuracy (RBF Kernel): ', "%.2f" % (rbf_accuracy * 100), "%")

    poly1_accuracy = accuracy_score(Y_test, poly1_pred)
    # print('Accuracy (Polynomial Degree 1 Kernel): ', "%.2f" % (poly1_accuracy * 100), "%")


    poly2_accuracy = accuracy_score(Y_test, poly2_pred)
    # print('Accuracy (Polynomial Degree 2 Kernel): ', "%.2f" % (poly2_accuracy * 100), "%")


    poly3_accuracy = accuracy_score(Y_test, poly3_pred)
    print('Accuracy (Polynomial Degree 3 Kernel): ', "%.2f" % (poly3_accuracy * 100), "%")

    #lin_accuracy = accuracy_score(Y_test, lin_pred)
    #print('Accuracy (Linear Kernel): ', "%.2f" % (lin_accuracy * 100))


print("***Classifier: SVM***")
print("Feature: words")
svm_classifer('interest.acl94.txt', 'words')
print("Feature: categories")
svm_classifer('interest.acl94.txt', 'categories')
