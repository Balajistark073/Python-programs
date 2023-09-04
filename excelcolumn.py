def excelcolumn(columnname):
    colnum=0
    for char in columnname:
        colnum=colnum*26+(ord(char)-ord('A')+1)
    return colnum
colname=input("Enter the column name: ")
converted=colname.upper()
result=excelcolumn(converted)
print(result)