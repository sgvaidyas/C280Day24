def fromCSV(path,delimiter,quotechar):
    import csv # import the csv module
    data=list() # any data we will read will be returned in a list
    with open(path, newline='') as csvfile: # open the file
        filecontent = csv.DictReader(csvfile, delimiter=delimiter, quotechar=quotechar)
        # access the content of the file
        for row in filecontent:#iterate through the rows
            data.append(row) #save the rows in the data list. Each row is a dictionary
    return data

def extract_year(row):
    value = row['Date']
    MM=""
    # split function in python used to divide strings based on some delimiter
    a = value.split("/")
    YY = a[2]
    #implement logic here
    new_row = row.copy()
    new_row.update({'Year':YY})
    return new_row


data=fromCSV(path='stocks.csv',delimiter=',',quotechar='|')
print(data[0])

data_mapped = map(extract_year,data)
data_mapped_list = list(data_mapped)
print(data_mapped_list[0])
