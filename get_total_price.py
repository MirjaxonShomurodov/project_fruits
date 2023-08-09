def get_total_price(data:str)->float:
    """
    This function returns the total price of the fruits

    args:
        data: CSV file with the fruits data
    returns:
        float: fruits total price
    """
    rows=data.split('\n')
    data=[]
    for i in rows[:-1]:
        data.append(i.split(','))
    for i in range(1,len(data)):
        prek=(data[i][1])
        print(prek)
    return prek
f=open('fruits.csv')
print(get_total_price(f.read())) 
    