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
    for i in rows[1:]:
        data.append(i.split(','))
        return data[0][0]
f=open('fruits.csv')
print(get_frutis_name(f.read())) 
