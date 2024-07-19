import pandas as pd

dictData = {
    'Introduction': ['I am Prahlad Shah Teli ', 'I am from Kathmandu Nepal'],
    'Footer': ['satungal', 'kathmandu']
}

data = pd.DataFrame(dictData)
print(data)
file = data.to_csv('Prahlad.csv', index=False)
