import pandas as pd
import seaborn as sb

# Load the data
df = pd.read_csv('shipment.csv')

# Filter for California and Standard Class
df2 = df[(df['State'] == 'California') & (df['Ship Mode'] == 'Standard Class')].copy()

# Remove decimals from postal codes
df2['Postal Code'] = df2['Postal Code'].astype(str).str.split('.').str.get(0)

# Drop unnecessary columns
df2.drop(columns=['Region', 'Row ID'], inplace=True)

# Check for null values
print(df2.isna().sum())

# Check for duplicates
print(df2.duplicated().sum())

# Reset the index
df2.reset_index(drop=True, inplace=True)

# Add Order_Year and Month columns for visualization
df2['Order_Year'] = df2['Order Date'].astype(str).str.split('/').str[2]
df2['Month'] = df2['Order Date'].astype(str).str.split('/').str[1]

# Visualize the comparison of the number of sold categories in different years
sb.histplot(data=df2, x='Order_Year', hue='Category')

# Visualize the amount of sales over years
sb.barplot(data=df2, x='Order_Year', y='Sales')

# Find which category sells the best
best_selling_category = df2.groupby('Category')['Sales'].sum()
print(best_selling_category)

# Find the best selling month on average
best_selling_month = df2.groupby('Month')['Sales'].mean()
print(best_selling_month)
