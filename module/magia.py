def mine(file):
    data  = []
    dataD = []
    file = open(file, 'r')
    for line in file.readlines():
        data.append(line)
    for index, item in enumerate(data):
         if index % 5 == 0 and index > 0:
            rest = {}
            rest['name'] = data[index - 5].rstrip()
            rest['rating'] = data[index - 4].rstrip().replace('%', '')
            rest['price'] = data[index - 3].rstrip()
            if ',' in data[index - 2].rstrip():
                rest['cuisines'] = [data[index - 2].rstrip().split(',')[0], data[index - 2].rstrip().split(',')[1]]
            else:
                rest['cuisines'] = [data[index - 2].rstrip()]
            dataD.append(rest)
    return dataD

