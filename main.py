# returns a list of 2 lists (lists of words and lists of categories)
def preprocess_file(file_name):
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


# function that removes whitespaces and other characters
def remove_line_filler(line):
    current_line = line.replace('=', '')
    current_line = current_line.replace(',/,', '')
    current_line = current_line.replace('[', '')
    current_line = current_line.replace(']', '')
    current_line = current_line.replace('\n', '')
    current_line = current_line.replace('/', ' ')
    return list(filter(None, current_line.split(' ')))  # removes all the whitespaces in line


# extracts features depending on the context_information_type (words or category, extra the 2 contexts before and after
# the index
# TODO: implement category extraction, same logic as words extraction, feel free to rename variables!!
def extract_features(file, context_information_type):
    words_list = file[0]
    words_before_after_idx = []
    sense = []  # TODO: extract interest_ and append to sense list

    if context_information_type == 'words':
        for x in words_list:

            interest_idx = index_lookup(x, 'interest')
            context_before_idx = []
            context_after_idx = []

            # smallest_idx: idx du mot - 2 positions avant
            smallest_idx = interest_idx - 2

            """
            if we're unable to keep 2 words before the idx (out of bound), start at the beginning of the list at idx 0
            and append the words until we reach the idx, else append 2 words before the idx as per usual
            """
            if smallest_idx <= 0:
                smallest_idx = 0
                while smallest_idx < interest_idx:
                    context_before_idx.append(x[smallest_idx])
                    smallest_idx += 1
            else:
                while smallest_idx < interest_idx:
                    context_before_idx.append(x[smallest_idx])
                    smallest_idx += 1

            # bigger_idx: idx du mot + 2 positions apres
            bigger_idx = interest_idx + 2

            """
            if we're unable to keep 2 words after the idx (out of bound), start at the end of the list at len(list)
            and append the words until we reach the idx, else append 2 words after the idx as per usual
            """
            if bigger_idx >= len(x):
                bigger_idx = len(x) - 1
                while bigger_idx > interest_idx:
                    context_after_idx.append(x[bigger_idx])
                    bigger_idx -= 1
            else:
                while bigger_idx > interest_idx:
                    context_after_idx.append(x[bigger_idx])
                    bigger_idx -= 1

            extracted_outputs = context_before_idx + context_after_idx
            print(extracted_outputs)
            words_before_after_idx.append(extracted_outputs)

    return words_before_after_idx


# function that returns the idx for a given word
def index_lookup(line, word):
    for x, elem in enumerate(line):
        if word in elem:
            return x
    return None


if __name__ == '__main__':
    file = preprocess_file('interest.acl94.txt')
    extract_features(file, 'words')
    # extract_features(file, 'categories')
