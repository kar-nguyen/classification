def preprocess_file(file_name):
    data = []   # will contain [[words], [categories]] for each line
    with open(file_name) as f:
        lines = f.readlines()
        for line in lines:
            if line[:2] != '$$':
                # remove whitespace and punctuation
                current_line = line.replace('=', '')
                current_line = current_line.replace(',/,', '')
                current_line = current_line.replace('``/``', '')
                current_line = current_line.replace('[', '')
                current_line = current_line.replace(']', '')
                current_line = current_line.replace('\n', '')
                current_line = current_line.replace('/', ' ')
                current_line = list(filter(None, current_line.split(' ')))  # removes all the whitespaces in line

                # seperate words and categories in 2 lists
                word_list = current_line[::2]
                category_list = current_line[1::2]

                words_categories_data = [word_list, category_list]
                data.append(words_categories_data)

    return data


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    preprocess_file('interest.acl94.txt')
