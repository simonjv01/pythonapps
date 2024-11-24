import pandas as pd

# Create a simple DataFrame
data = {'Name': ['John', 'Anna', 'Peter'],
        'Age': [28, 24, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)

# Print the DataFrame
print(df)

carbondata = pd.read_csv('C:/Users/sjvar/dev/datasets/Carbon_CO2_Emissions_by_Country.csv')
print(carbondata.head())

print(carbondata.shape)



