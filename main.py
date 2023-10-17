def open_file(filepath):
    with open(filepath) as fl:
        return fl.read()


def count_words(contents):
    return len(contents.split())


def count_letters(contents):
    lower_content = contents.lower()
    letter_dict = {}
    for l in lower_content:
        if l in letter_dict:
            letter_dict[l] += 1
        else:
            letter_dict[l] = 1
    return letter_dict


def to_list(content):
    li = [{'letter': letter, 'count': content[letter]} for letter in content if letter.isalpha()]
    li.sort(reverse=True, key=lambda x: x["count"])
    return li


if __name__ == '__main__':
    filepath = 'books/frankenstein.txt'
    file_content = open_file(filepath)
    words_count = count_words(file_content)
    l_dict = count_letters(file_content)
    l_li = to_list(l_dict)

    print(f'--- Begin report of {filepath} ---')
    print(f'{words_count} words found in the document')
    print()

    for item in l_li:
        print(f'The {item["letter"]} character was found {item["count"]} times')

    print('--- End report ---')
