<<<<<<< HEAD
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt 


#load customer dataset 
customer_data = pd.read_csv('online_retail.csv')

#Display basic dataset information 
print("\n Dataset Information:")
print(customer_data.info())

#Identify missing values in each colums
print("\n Missing values count:")
print(customer_data.isnull().sum())

#Visualisation missing values using a heatmap
plt.figure(figsize=(10,6))
sns.heatmap(customer_data.isnull(), cmap="coolwarm", cbar=False)
plt.title("Missing values heatmap in Customer Dataset")
plt.show() 

# Drop duplicates if any
customer_data = customer_data.drop_duplicates()

# Convert InvoiceDate to datetime
customer_data['InvoiceDate'] = pd.to_datetime(customer_data['InvoiceDate'])


#Drop rows with missing CustomerID
customer_data = customer_data.dropna(subset=['CustomerID',])

#Fill raws with missing Description 
customer_data['Description'] = customer_data['Description'].fillna('Unknown')

#Missing values After cleaning 
print("\n Missing values count after cleaning:")
print(customer_data.isnull().sum())


# Create TotalPrice column (Quantity * UnitPrice)
customer_data['TotalPrice'] = customer_data['Quantity'] * customer_data['UnitPrice']


customer_data.to_csv('Customer_Clean_Data.csv', index=False)   



=======
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt 


#load customer dataset 
customer_data = pd.read_csv('online_retail.csv')

#Display basic dataset information 
print("\n Dataset Information:")
print(customer_data.info())

#Identify missing values in each colums
print("\n Missing values count:")
print(customer_data.isnull().sum())

#Visualisation missing values using a heatmap
plt.figure(figsize=(10,6))
sns.heatmap(customer_data.isnull(), cmap="coolwarm", cbar=False)
plt.title("Missing values heatmap in Customer Dataset")
plt.show() 

# Drop duplicates if any
customer_data = customer_data.drop_duplicates()

# Convert InvoiceDate to datetime
customer_data['InvoiceDate'] = pd.to_datetime(customer_data['InvoiceDate'])

# Add TotalPrice column
customer_data['TotalPrice'] = customer_data['Quantity'] * customer_data['UnitPrice']


#Drop rows with missing CustomerID
customer_data = customer_data.dropna(subset=['CustomerID',])

#Fill raws with missing Description 
customer_data['Description'] = customer_data['Description'].fillna('Unknown')

#Missing values After cleaning 
print("\n Missing values count after cleaning:")
print(customer_data.isnull().sum())


customer_data.to_csv('Customer_Clean_Data.csv', index=False)   



>>>>>>> 2cdedf186cfb8d8fa1da1c1c3f4859ee55244d99
