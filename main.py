
def data_file(file_name):
    data = []
    word_lists = []
    category_lists = []
    with open(file_name) as f:
        lines = f.readlines()
        for line in lines:
            if line[:2] != '$$':
                current_line = remove_line_filler(line)

                # separate words and categories in 2 lists
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

def one_before_and_after(file, dict_word , dict_categories, context_information_type):
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


        # smallest_idx: idx du mot - 1 positions avant
        smallest_idx = interest_idx - 1

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

        # bigger_idx: idx du mot + 1 positions apres
        bigger_idx = interest_idx + 1

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

        if (len(extracted_categories_outputs)) == 2:
            categories_before_after_idx.append(extracted_categories_outputs)
        if (len(extracted_word_outputs)) == 2:
            words_before_after_idx.append(extracted_word_outputs)

        if (len(extracted_categories_outputs)) and (len(extracted_word_outputs)) == 2:
            interests_list.append(interest_sense)

    if context_information_type == 'words':
        return words_before_after_idx, interests_list
    elif context_information_type == 'categories':
        return categories_before_after_idx, interests_list

# extracts features depending on the context_information_type (words or category)
def two_before_and_after(file, dict_word , dict_categories, context_information_type):
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

def three_before_and_after(file, dict_word, dict_categories, context_information_type):
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

            # smallest_idx: idx du mot - 3 positions avant
            smallest_idx = interest_idx - 3

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

            # bigger_idx: idx du mot + 3 positions apres
            bigger_idx = interest_idx + 3

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

            if (len(extracted_categories_outputs)) == 6:
                categories_before_after_idx.append(extracted_categories_outputs)
            if (len(extracted_word_outputs)) == 6:
                words_before_after_idx.append(extracted_word_outputs)

            if (len(extracted_categories_outputs)) and (len(extracted_word_outputs)) == 6:
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

