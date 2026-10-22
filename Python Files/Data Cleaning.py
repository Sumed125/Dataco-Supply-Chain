import os
import pandas as pd 
import numpy as np 

# This py file is created to segregate dimension tables, fact tables from original dataset
# Creating directory to store preprocessed files or directing to that folder if already exists
script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(script_dir)
preprocessed_folder_path = os.path.join(parent_dir, 'preprocessed')

if os.path.isdir(preprocessed_folder_path):
    os.chdir(preprocessed_folder_path)
else:
    os.makedirs(preprocessed_folder_path)
    os.chdir(preprocessed_folder_path)

raw_file_path = os.path.join(parent_dir, 'raw', 'dataset.csv') # raw files location

# Loading data of customer in customer dataframe and saving file in preprocessed folder
columns = ['Customer City', 'Customer Country', 
'Customer Fname', 'Customer Id', 
'Customer Lname', 'Customer Segment', 'Customer State', 
'Customer Street', 'Customer Zipcode']

customer = pd.read_csv(raw_file_path, encoding = 'latin-1', usecols = columns) # Loading file in dataframe

customer['Customer Id'] = customer['Customer Id'].astype('object') # Changing customer id type in object
customer['Customer Zipcode'] = customer['Customer Zipcode'].astype('object') # Changing customer zipcode type in object

customer = customer.drop_duplicates() # removing duplicates from dataframe

# Changing column names in accordance with MySQL nomenclature
customer.rename(columns = {
    'Customer City':'Customer_City',
    'Customer Country':'Customer_Country',
    'Customer Fname':'Customer_Fname',
    'Customer Lname':'Customer_Lname',
    'Customer Id':'Customer_Id',
    'Customer Segment':'Customer_Segment',
    'Customer State':'Customer_State',
    'Customer Street':'Customer_Street',
    'Customer Zipcode':'Customer_Zipcode'
}, inplace = True)

customer.to_csv(os.path.join(preprocessed_folder_path, 'customer.csv'), index = False) # Saving customer dimension table in csv file

# Loading product file in product dataframe and saving file in preprocessed folder
columns = ['Product Card Id', 'Product Category Id', 
'Product Image', 'Product Name', 'Product Price', 'Category Name']

product = pd.read_csv(raw_file_path, encoding = 'latin-1', usecols = columns) # Loading file in dataframe

product.rename(columns = {
    'Product Card Id':'Product_Card_Id',
    'Product Category Id':'Product_Category_Id',
    'Product Image':'Product_Image',
    'Product Name':'Product_Name',
    'Product Price':'Product_Price',
    'Category Name':'Category_Name'
}, inplace = True)

product = product.drop_duplicates() # removing duplicates from dataframe

# Saving product dimension csv file
product.to_csv(os.path.join(preprocessed_folder_path, 'product.csv'), index = False) 

# Loading transactional data into csv file
# making columns to be dropped list
drop_columns = [
    'Customer City', 
    'Customer Country', 
    'Customer Email', 
    'Customer Fname', 
    'Customer Lname', 
    'Customer Segment', 
    'Customer State', 
    'Customer Street', 
    'Customer Zipcode',
    'Customer Password',
    'Product Category Id', 
    'Product Description', 
    'Product Image', 
    'Product Name', 
    'Product Price',
    'Department Id', 
    'Department Name', 
    'Latitude', 
    'Longitude', 
    'Category Id',
    'Category Name'
]

# Loading transaction file in pandas dataframe
df = pd.read_csv(raw_file_path, encoding = 'latin-1')
df = df.drop(columns = drop_columns) # Dropping columns from dimension tables

df['order date (DateOrders)'] = pd.to_datetime(df['order date (DateOrders)'])
df['shipping date (DateOrders)'] = pd.to_datetime(df['shipping date (DateOrders)'])
# Changing column names
df.rename(columns = {
    'Days for shipping (real)':'Days_for_shipping_real',
    'Days for shipment (scheduled)':'Days_for_shipment_scheduled',
    'Benefit per order':'Benefit_per_order',
    'Sales per customer':'Sales_per_customer',
    'Delivery Status':'Delivery_status',
    'Late_delivery_risk':'Late_delivery_risk',
    'Customer Id':'Customer_Id',
    'Order City':'Order_City',
    'Order Country':'Order_Country',
    'Order Customer Id':'Order_Customer_Id',
    'order date (DateOrders)':'Order_date_dateorders',
    'Order Id':'Order_Id',
    'Order Item Cardprod Id':'Order_Item_Cardprod_Id',
    'Order Item Discount':'Order_Item_Discount',
    'Order Item Discount Rate':'Order_Item_Discount_Rate',
    'Order Item Id':'Order_Item_Id',
    'Order Item Product Price': 'Order_Item_Product_Price',
    'Order Item Profit Ratio':'Order_Item_Profit_Ratio',
    'Order Item Quantity':'Order_Item_Quantity',
    'Order Item Total':'Order_Item_Total',
    'Order Profit Per Order':'Order_Profit_Per_Order',
    'Order Region':'Order_Region',
    'Order State':'Order_State',
    'Order Status':'Order_Status',
    'Order Zipcode':'Order_Zipcode',
    'Product Card Id':'Product_Card_Id',
    'Product Status':'Product_Status',
    'shipping date (DateOrders)':'Shipping_date_dateorders',
    'Shipping Mode':'Shipping_Mode'
}, inplace = True)


# Saving file in preprocessed folder
df.to_csv(os.path.join(preprocessed_folder_path, 'transaction.csv'), index = False)





