from sklearn import model_selection
from sklearn import svm
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier
def data_file(file_name):
    data = []
    word_lists = []
    category_lists = []
    with open(file_name) as f:
        lines = f.readlines()
        for line in lines:
            if line[:2] != '$$':
                current_line = remove_line_filler(line)

                # seperate words and categories in 2 lists
                word_list = current_line[::2]
                category_list = current_line[1::2]

                # words_categories_data = [word_list, category_list]
                # data.append(words_categories_data)
                word_lists.append(word_list)
                category_lists.append(category_list)

        data.append(word_lists)
        data.append(category_lists)

    return data

# returns a list of 2 lists (lists of words and lists of categories)
def dict_word(file_name):
    dict_word = {}
    with open(file_name) as f:
        lines = f.readlines()
        for line in lines:
            if line[:2] != '$$':
                current_line = remove_line_filler(line)
                # separate words and categories in 2 lists
                word_list = current_line[::2]
                for i in word_list:
                    if i not in dict_word:
                        dict_word[i] = len(dict_word) + 1
    return dict_word

def dict_categorie(file_name):
    dictcategories ={}
    with open(file_name) as f:
        lines = f.readlines()
        for line in lines:
            if line[:2] != '$$':
                current_line = remove_line_filler(line)
                category_list = current_line[1::2]
                for j in category_list:
                    if j not in dictcategories:
                        dictcategories[j] = len(dictcategories) + 1
    return dictcategories

# function that removes whitespaces and other characters
def remove_line_filler(line):
    current_line = line.replace('=', '')
    current_line = current_line.replace(',/,', '')
    current_line = current_line.replace('[', '')
    current_line = current_line.replace(']', '')
    current_line = current_line.replace('\n', '')
    current_line = current_line.replace('/', ' ')
    return list(filter(None, current_line.split(' ')))  # removes all the whitespaces in line


# extracts features depending on the context_information_type (words or category)
def extract_context_information_type(file, dict_word , dict_categories, context_information_type):
    words_list = file[0]
    categories_list = file[1]

    words_before_after_idx = []
    categories_before_after_idx = []

    # contains all the interest_ or interests_
    interests_list = []

    for x, y in zip(words_list, categories_list):

        words_before_idx = []
        words_after_idx = []
        categories_before_idx = []
        categories_after_idx = []

        interest_idx, interest_sense = index_lookup(x, 'interest')


        # smallest_idx: idx du mot - 2 positions avant
        smallest_idx = interest_idx - 2

        """
        if we're unable to keep 2 words/categories before the idx (out of bound), start at the beginning of the list 
        at idx 0 and append the words/categories until we reach the idx, else append 2 words/categories 
        before the idx as per usual
        """
        if smallest_idx <= 0:
            smallest_idx = 0
            while smallest_idx < interest_idx:
                words_before_idx.append(dict_word[x[smallest_idx]])
                categories_before_idx.append(dict_categories[y[smallest_idx]])
                smallest_idx += 1
        else:
            while smallest_idx < interest_idx:
                words_before_idx.append(dict_word[x[smallest_idx]])
                categories_before_idx.append(dict_categories[y[smallest_idx]])
                smallest_idx += 1

        # bigger_idx: idx du mot + 2 positions apres
        bigger_idx = interest_idx + 2

        """
        if we're unable to keep 2 words/categories after the idx (out of bound), start at the end of the list at 
        len(list) and append the words/categories until we reach the idx, else append 2 words/categories 
        after the idx as per usual
        """
        if bigger_idx >= len(x):
            bigger_idx = len(x) - 1
            while bigger_idx > interest_idx:
                words_after_idx.append(dict_word[x[bigger_idx]])
                categories_after_idx.append(dict_categories[y[bigger_idx]])
                bigger_idx -= 1
        else:
            while bigger_idx > interest_idx:
                words_after_idx.append(dict_word[x[bigger_idx]])
                categories_after_idx.append(dict_categories[y[bigger_idx]])
                bigger_idx -= 1

        extracted_word_outputs = words_before_idx + words_after_idx
        extracted_categories_outputs = categories_before_idx + categories_after_idx

        if (len(extracted_categories_outputs)) == 4:
            categories_before_after_idx.append(extracted_categories_outputs)
        if (len(extracted_word_outputs)) == 4:
            words_before_after_idx.append(extracted_word_outputs)

        if (len(extracted_categories_outputs)) and (len(extracted_word_outputs)) == 4:
            interests_list.append(interest_sense)

    if context_information_type == 'words':
        return words_before_after_idx, interests_list
    elif context_information_type == 'categories':
        return categories_before_after_idx, interests_list


# function that returns the idx and full string given a substring (interest)
def index_lookup(line, word):
    for x, elem in enumerate(line):
        if word in elem:
            return [x, elem]
    return None

def svm_classifer(file, context_information_type):
    X, Y = extract_context_information_type(data_file(file), dict_word(file), dict_categorie(file),context_information_type)
    X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, train_size=0.80, test_size=0.20,
                                                                        random_state=50)
    rbf = svm.SVC(kernel='rbf', gamma=0.5, C=0.1).fit(X_train, Y_train)
    poly = svm.SVC(kernel='poly', degree=3, C=1).fit(X_train, Y_train)

    poly_pred = poly.predict(X_test)
    rbf_pred = rbf.predict(X_test)

    poly_accuracy = accuracy_score(Y_test, poly_pred)
    poly_f1 = f1_score(Y_test, poly_pred, average='weighted')
    print('Accuracy (Polynomial Kernel): ', "%.2f" % (poly_accuracy * 100))
    print('F1 (Polynomial Kernel): ', "%.2f" % (poly_f1 * 100))

    rbf_accuracy = accuracy_score(Y_test, rbf_pred)
    rbf_f1 = f1_score(Y_test, rbf_pred, average='weighted')
    print('Accuracy (RBF Kernel): ', "%.2f" % (rbf_accuracy * 100))
    print('F1 (RBF Kernel): ', "%.2f" % (rbf_f1 * 100))

def decisionTree(file, context_information_type):
    X, Y = extract_context_information_type(data_file(file), dict_word(file), dict_categorie(file),context_information_type)
    X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, train_size=0.80, test_size=0.20,
                                                                        random_state=50)
    clf = DecisionTreeClassifier(max_depth=3, random_state=50).fit(X_train, Y_train)
    Y_pred = clf.predict(X_test)
    print("Accuracy:", metrics.accuracy_score(Y_test, Y_pred))

def foret_aleatoire(file, context_information_type):
    X, Y = extract_context_information_type(data_file(file), dict_word(file), dict_categorie(file), context_information_type)
    X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=0.30,
                                                                        random_state=100)

    forest = RandomForestClassifier(n_estimators=100, random_state=100)
    forest.fit(X_train, Y_train)
    Y_pred = forest.predict(X_test)
    print("Accuracy:", metrics.accuracy_score(Y_test, Y_pred))

def naiveBayes(file, context_information_type):
    X, Y = extract_context_information_type(data_file(file), dict_word(file), dict_categorie(file), context_information_type)
    X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=0.30,
                                                                        random_state=100)
    gnb = GaussianNB()
    gnb.fit(X_train, Y_train)
    Y_pred = gnb.predict(X_test)
    print("Accuracy:", metrics.accuracy_score(Y_test, Y_pred))

def multiLayerPerceptron(file, context_information_type):
    X, Y = extract_context_information_type(data_file(file), dict_word(file), dict_categorie(file), context_information_type)
    X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=0.30,
                                                                        random_state=100)
    clf = MLPClassifier(random_state=1, max_iter=500).fit(X_train, Y_train)
    Y_pred = clf.predict(X_test)
    clf.score(X_test,Y_test)

    print("Accuracy:", metrics.accuracy_score(Y_test, Y_pred))

if __name__ == '__main__':

    decisionTree('interest.acl94.txt', 'words')
    svm_classifer('interest.acl94.txt', 'words')
    foret_aleatoire('interest.acl94.txt', 'words')
    naiveBayes('interest.acl94.txt', 'words')
    multiLayerPerceptron('interest.acl94.txt', 'words')

    decisionTree('interest.acl94.txt', 'categories')
    svm_classifer('interest.acl94.txt', 'categories')
    foret_aleatoire('interest.acl94.txt', 'categories')
    naiveBayes('interest.acl94.txt', 'categories')
    multiLayerPerceptron('interest.acl94.txt', 'categories')