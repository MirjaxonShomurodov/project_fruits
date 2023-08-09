def get_frutis_name(data:str)->list:
    """
    This function returns the names of the fruits

    args:
        data: CSV file with the fruits data
    returns:
        list: list of fruits names
    """
    # your code here
    rows=data.split('\n')
    data=[]
    for i in rows[:-1]:
        data.append(i.split(','))
    for i in range(1,len(data)):
        prek=(data[i][0])
        print(prek)
    return prek
f=open('fruits.csv')
print(get_frutis_name(f.read())) 
