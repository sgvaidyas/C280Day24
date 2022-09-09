import csv
def fromCSV(path,delimiter,quotechar):
    import csv # import the csv module
    data=list() # any data we will read will be returned in a list
    with open(path, newline='') as csvfile: #o pen the file
        filecontent = csv.DictReader(csvfile, delimiter=delimiter, quotechar=quotechar)
        # access the content of the file
        for row in filecontent: # iterate through the rows
            data.append(row) # save the rows in the data list. Each row is a dictionary
    return data

data=fromCSV(path='stocks.csv',delimiter=',',quotechar='|')

# filter all elements in data where the open price is lower than the close price
data_filtered = filter(lambda x: float(x['Open']) < float(x['Close']), data)
print(type(data_filtered))

data_filtered_list = list(data_filtered) # convert the filter object into a list
for row in data_filtered_list: # display each element in the filtered list
    print(row)
