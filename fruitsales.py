import pandas as pd
data = {'Apples' :[35, 41],
        'Bananas' :[ 21 , 34]}

index = ['2017 Sales', '2018 Sales']
# create a data frame
fruit_sales = pd.DataFrame(data, index=index)
fruit_sales.to_csv('fruit.csv')
print("DataFrame written to 'fruit.csv' successfully.")

print(data)
"""import pandas as pd

# Example DataFrame
data = {'Apples': [35, 41], 'Bananas': [21, 34]}
index = ['2017 Sales', '2018 Sales']
df = pd.DataFrame(data, index=index)

# Print to check if data is correctly populated
print(df)

# Writing the DataFrame to CSV
df.to_csv('fruit.csv')

# Save to a specific directory
df.to_csv('data/fruit.csv')  # Ensure 'data' directory exists"""


