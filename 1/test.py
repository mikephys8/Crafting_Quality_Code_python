__author__ = 'Administrator'


file = open('restaurants_small.txt', 'r')
def read_words(file):
    word_list = []

    # line = file.readline()
    lines = file.readlines()
    for line in lines:
        if line != '' and line != '\n':
            word_list.append(line.rstrip('\n'))
    return word_list
print(read_words(file))
print('------------------------------------------------')


# x = read_words(file)
x = ['Georie Porgie', '87%', '$$$', 'Canadian,Pub Food',
     'Queen St. Cafe', '82%', '$', 'Malaysian,Thai',
     'Dumplings R Us', '71%', '$', 'Chinese',
     'Mexican Grill', '85%', '$$', 'Mexican',
     'Deep Fried Everything', '52%', '$', 'Pub Food']


def word_list_mod(x):
    i = 0
    # d = {}
    for i in range(0, len(x), 2):
        d = {x[i]: x[i+1]}
        i += 4
    return d
print(word_list_mod(x))


    # i = 0
    # new_word_list = []
    # while i != len(word_list):
    #     for item in word_list:
    #         while item != '':
    #             new_word_list


