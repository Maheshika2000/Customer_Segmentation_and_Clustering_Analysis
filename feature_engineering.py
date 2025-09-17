import pandas as pd
from datetime import timedelta

# Load the cleaned dataset
customer_data = pd.read_csv('Customer_Clean_Data.csv')

# Ensure InvoiceDate is datetime
customer_data['InvoiceDate'] = pd.to_datetime(customer_data['InvoiceDate'], errors='coerce')

# Create TotalPrice column (in case missing)
if 'TotalPrice' not in customer_data.columns:
    customer_data['TotalPrice'] = customer_data['Quantity'] * customer_data['UnitPrice']

# Reference date for Recency calculation
reference_date = customer_data['InvoiceDate'].max() + timedelta(days=1)

# -------------------------------
# RFM + Extra Features
# -------------------------------
rfm = customer_data.groupby('CustomerID').agg({
    'InvoiceDate': lambda x: (reference_date - x.max()).days,   # Recency
    'InvoiceNo': 'nunique',                                    # Frequency (unique invoices)
    'TotalPrice': 'sum',                                       # Monetary
    'Quantity': 'sum',                                         # Total items bought
})

#------------------ Average Basket Size = Total Quantity / Number of Invoices
rfm['AvgBasketSize'] = rfm['Quantity'] / rfm['InvoiceNo']

#------------------ Average Order Value = Total Monetary / Number of Invoices
rfm['AvgOrderValue'] = rfm['TotalPrice'] / rfm['InvoiceNo']

# Keep Monetary column consistent name
rfm.rename(columns={
    'InvoiceDate': 'Recency',
    'InvoiceNo': 'Frequency',
    'TotalPrice': 'Monetary'
}, inplace=True)

# Reset index
rfm = rfm.reset_index()

# -------------------------------
# Add Country Feature (One-hot Encoding)
# -------------------------------
# Take each customer’s most common country
customer_country = customer_data.groupby('CustomerID')['Country'].agg(lambda x: x.mode()[0])
rfm = rfm.merge(customer_country, on='CustomerID')

# One-hot encode Country
rfm = pd.get_dummies(rfm, columns=['Country'], drop_first=True)

# -------------------------------
# Save features
# -------------------------------
rfm.to_csv('Customer_Features_Extended.csv', index=False)

print("Sample of engineered features:")
print(rfm.head())
