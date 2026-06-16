import pandas as pd

# Create a DataFrame from a dictionary


df = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]], columns=['A', 'B', 'C'], index=['Row1', 'Row2', 'Row3']    )
print(df.head())
print(df.tail())
print(df.index)
print(df.columns)
print(df.values)
print(df.describe())
print(df.info())
print(df.unstack())
print(df.unique())
print(df.nunique())
print(df.shape)
''' Read a CSV file into a DataFrame '''
coffee=pd.read_csv('coffee_data.csv')
print(coffee.head())

results= pd.read_parquet('results.parquet')

olympics_data = pd.read_excel('olympics_data.xlsx')
print(olympics_data.head())

print(coffee.head())
print(coffee.tail())
#randomly sample 5 rows from the DataFrame
print(coffee.sample(5))

print(coffe.loc[row_indexer, column_indexer])
print(coffee.loc[5:8, [days, sales]])
coffee.index=coffee.Day
print(coffee.head())
print(coffee.iloc[0:5, 0:2])
coffee.loc[1,"units sold"]=10
print(coffee.head())
coffee.at[1,"units sold"]=15
print(coffee.head())
coffee.iat[1,1]=20
print(coffee.head())
coffee.day or coffee["day"]
.sort_values > ascending, descending
for index, row in coffee.iterrows():
    print(index, row["day"], row["units sold"])

bios= olympic data set example

bios.loc[bios[height] > 200]
bios.loc[(bios[height] > 200) & (bios[sport] == "Basketball")]
bios[bios['name'].str.contains('Michael|Mike')]
bios[bios['name'].str.contains('Michael|Mike', case=False)]
bios[bios['born_country'].isin(['United States', 'Canada'])]
bios[bios['name'].str.startswith('M')]
bios[bios['name'].str.endswith('son')]

bios.query('born_country == "United States" and sport == "Basketball" ')
coffee['price']=4.99
import numpy as np
coffee['new_price'= np.where(coffee['units sold'] > 10, coffee['price'] * 0.9, coffee['price'])]
print(coffee.head())

coffee.drop(columns=['price'], inplace=True)
print(coffee.head())

coffee_new=coffe.copy()
coffee_new['price']=4.99
print(coffee_new.head())
coffee['revenue']=coffee['units sold'] * coffee_new['price']
print(coffee.head())
coffe.rename(columns={'units sold': 'units_sold'}, inplace=True)
print(coffee.head())
bios_new=bios.copy()
bios_new['first_name']=bios_new['name'].str.split().str[0]
bios_new['last_name']=bios_new['name'].str.split().str[-1]
print(bios_new.head())
bios_new.drop(columns=['name'], inplace=True)
print(bios_new.head())
bios_new['born_date']=pd.to_datetime(bios_new['born_date'])
print(bios_new.head())  
bios_new['born_year']=bios_new['born_date'].dt.year
print(bios_new.head())
bios['height_category']=pd.cut(bios['height'], bins=[0, 170, 190, np.inf], labels=['Short', 'Medium', 'Tall'])
print(bios.head())
bios['height_category'].value_counts()
bios['height_category'].value_counts(normalize=True)
bios['height_category'].value_counts().plot(kind='bar')
def categorize_height(height):
    if height < 170:
        return 'Short'
    elif height < 190:
        return 'Medium'
    else:
        return 'Tall'
bios['category']=bios['height'].apply(categorize_height)
print(bios.head())
nocs=pd.read_csv('./data/noc_regions.csv')
pd.merge(bios, nocs, left_on='born_country', right_on='region', how='left')

usa=bios[bios['born_country'] == 'United States']
new_df=pd.concat([usa, bios[bios['born_country'] == 'Canada']])

coffee.loc[[0,1], 'units sold']= np.nan
print(coffee.head())
coffee =coffee.fillna({'units sold': 0})
#interpolate, mean, median, mode, forward fill, backward fill

coffee.dropna()
bios[bios['born country'].isnull()].value_counts(dropna=False)
bios.groupby('sport')['height'].mean()
pivot_table = bios.pivot_table(index='sport', values='height', aggfunc='mean')
 """.shift() to shift values in a column up or down
 .rank() to rank values in a column
 .cumsum() to calculate the cumulative sum of a column
 .rolling() to calculate rolling statistics (e.g., rolling mean) for a column
 .expanding() to calculate expanding statistics (e.g., expanding mean) for a column
 .apply() to apply a custom function to a column or DataFrame
 .agg() to apply multiple aggregation functions to a column or DataFrame
 .groupby() to group data by one or more columns and perform operations on the groups
 .resample() to resample time series data
 .corr() to calculate the correlation between two columns
 .sd() to calculate the standard deviation of a column
 .skew() to calculate the skewness of a column
 .kurt() to calculate the kurtosis of a column
 .sort_values() to sort a DataFrame by one or more columns"""












