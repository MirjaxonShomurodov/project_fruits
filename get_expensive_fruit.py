def get_expensive_fruit(data: str) -> str:
    """
    This function returns the name of the most expensive fruit

    args:
        data: CSV file with the fruits data
    returns:
        str: name of the most expensive fruit
    """
     # your code here
    rows=data.split('\n')
    data=[]
    for row in rows[:-1]:
        data.append(row.split(','))
    
    first_row =data[1]
    max_price=float(first_row[1])
    max_id = 1

    for i in range(1,len(data)):
        price=float(data[i][1])
        if max_price > price:
            max_price=price
            max_id = i
    return data[max_id][0]

f=open('fruits.csv')
print(get_expensive_fruit(f.read())) 


