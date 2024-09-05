import pandas as pd 


Data = [

    {'name': 'sunny', 'age':28, 'city': 'bjopal'},
    {'name': 'sunny', 'age':22, 'city': 'bjopa2'}]


Data = pd.DataFrame(Data)
Data.to_csv("data/data.csv", index=False)