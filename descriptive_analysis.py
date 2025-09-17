<<<<<<< HEAD
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt 


#load customer dataset 
customer_data = pd.read_csv('Customer_Clean_Data.csv')

customer_data['Country'].value_counts().head(10).plot(kind='bar')
plt.title('Top 10 Countries by Transactions')
plt.show()


# Convert InvoiceDate to datetime
customer_data['InvoiceDate'] = pd.to_datetime(customer_data['InvoiceDate'])


# Convert InvoiceDate to datetime
customer_data['InvoiceDate'] = pd.to_datetime(customer_data['InvoiceDate'], errors='coerce')

# Now you can extract year, month, day
customer_data['InvoiceYear'] = customer_data['InvoiceDate'].dt.year
customer_data['InvoiceMonth'] = customer_data['InvoiceDate'].dt.month
customer_data['InvoiceDay'] = customer_data['InvoiceDate'].dt.day
customer_data['InvoiceWeekday'] = customer_data['InvoiceDate'].dt.day_name()


# Sales trend by month
monthly_sales = customer_data.groupby(['InvoiceYear', 'InvoiceMonth'])['TotalPrice'].sum()
monthly_sales.plot(kind='line', marker='o')
plt.title('Monthly Sales Trend')
plt.show()

# Sales by weekday
weekday_sales = customer_data.groupby('InvoiceWeekday')['TotalPrice'].sum().reindex([
    'Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'])
weekday_sales.plot(kind='bar')
plt.title('Sales by Weekday')
plt.show()
=======
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt 


#load customer dataset 
customer_data = pd.read_csv('Customer_Clean_Data.csv')

customer_data['Country'].value_counts().head(10).plot(kind='bar')
plt.title('Top 10 Countries by Transactions')
plt.show()


# Convert InvoiceDate to datetime
customer_data['InvoiceDate'] = pd.to_datetime(customer_data['InvoiceDate'])


# Convert InvoiceDate to datetime
customer_data['InvoiceDate'] = pd.to_datetime(customer_data['InvoiceDate'], errors='coerce')

# Now you can extract year, month, day
customer_data['InvoiceYear'] = customer_data['InvoiceDate'].dt.year
customer_data['InvoiceMonth'] = customer_data['InvoiceDate'].dt.month
customer_data['InvoiceDay'] = customer_data['InvoiceDate'].dt.day
customer_data['InvoiceWeekday'] = customer_data['InvoiceDate'].dt.day_name()


# Sales trend by month
monthly_sales = customer_data.groupby(['InvoiceYear', 'InvoiceMonth'])['TotalPrice'].sum()
monthly_sales.plot(kind='line', marker='o')
plt.title('Monthly Sales Trend')
plt.show()

# Sales by weekday
weekday_sales = customer_data.groupby('InvoiceWeekday')['TotalPrice'].sum().reindex([
    'Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'])
weekday_sales.plot(kind='bar')
plt.title('Sales by Weekday')
plt.show()
>>>>>>> 2cdedf186cfb8d8fa1da1c1c3f4859ee55244d99
