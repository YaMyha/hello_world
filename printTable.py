def printTable(list_of_lists):
    colWidth = [0] * len(list_of_lists)
    for i in range(len(list_of_lists)):
        colWidth[i] = max(list_of_lists[i], key=len)
    #width = len(max(colWidth, key=len))
    for k in range(len(list_of_lists[0])):
        for j in range(len(list_of_lists)):
            print(list_of_lists[j][k].rjust(len(colWidth[j])), end=' ')
        print()
DataTable = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(DataTable)
printprintpritjdhjdgsgbsdaaaaavxcvxxvxd