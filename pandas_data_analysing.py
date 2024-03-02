import pandas as pd
import seaborn as sb

# import the data
df = pd.read_csv('train.csv')

df.head(10)
df.dtypes

# Clean up data
df[df['State'] == 'California']
df2 = df[(df['State'] == 'California') & (df['Ship Mode'] == 'Standard Class')]

# delete numbers after dot in postal codes
df2['Postal Code'] = df2['Postal Code'].astype(str).str.split('.').str.get(0)

# drop "Region" column
df2 = df2.drop(['Region'], axis = 1)

# drop "Row ID" column
df2 = df2.drop(['Row ID'], axis = 1)

df2.head()

# check if there are null values
df2.isna().sum()

# check if there are any duplicates
df2[df2.duplicated() == True]

# reset the index numbers
df2.reset_index(drop = True)

# visualize the comparison num of selled categories in different years
sb.histplot(df2, x = df2['Order Date'].astype(str).str.split('/').str[2], hue = 'Category')

# vizualize the amount of sales over years
df2['Order_Year'] = df2['Order Date'].astype(str).str.split('/').str[2]
sb.barplot(data=df2, x='Order_Year', y='Sales')

# which category sells the best
df2.groupby(['Category'])['Sales'].sum()

# which month is the best selling one in average
df2['Month'] = df2['Order Date'].astype(str).str.split('/').str[1]
df2.groupby(['Month'])['Sales'].mean()
