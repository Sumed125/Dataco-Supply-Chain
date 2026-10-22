import json
import os
import numpy as np 
import pandas as pd
import sqlalchemy

# Credentials file path
script_dir_path = os.path.dirname(os.path.abspath(__file__))
parent_dir_path = os.path.dirname(script_dir_path)
credential_path = os.path.join(parent_dir_path, 'credential.json')

with open(credential_path, 'r') as file:
    credential = json.load(file)


host = credential['host']
username = credential['username']
password = credential['password']
port = credential['port']
database = credential['database']

# Creating connection to MySQL server and database
# Before creating connection, make sure database is already created in server
engine = sqlalchemy.create_engine("mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(username, password, host, port, database))

# Loading customer fact table in MySQL table
# Before loading customer fact table, ensure customer table is created in database
# For schema, you can refer database schema.txt file

script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(script_dir)
preprocessed_dir_path = os.path.join(parent_dir, 'preprocessed')
customer_file_path = os.path.join(preprocessed_dir_path, 'customer.csv')

customer_df = pd.read_csv(customer_file_path, encoding = 'latin-1')

# Loading customer table into MySQL
#customer_df.to_sql('customer', con = engine, index = False, if_exists = 'append')

# Similar process for product
product_file_path = os.path.join(preprocessed_dir_path, 'product.csv')

Product_df = pd.read_csv(product_file_path, encoding = 'latin-1')

Product_df['Product_Card_Id'] = Product_df['Product_Card_Id'].astype('object')
Product_df['Product_Category_Id'] = Product_df['Product_Category_Id'].astype('object')

#Product_df.to_sql('product', con = engine, index = False, if_exists = 'append')

# Loading transaction table in MySQL
transaction_file_path = os.path.join(preprocessed_dir_path, 'transaction.csv')

fact_df = pd.read_csv(transaction_file_path)
fact_df['Order_Id'] = fact_df['Order_Id'].map(str)
fact_df['Order_Item_Cardprod_Id'] = fact_df['Order_Item_Cardprod_Id'].map(str)
fact_df['Order_Item_Id'] = fact_df['Order_Item_Id'].map(str)
fact_df['Shipping_date_dateorders'] = pd.to_datetime(fact_df['Shipping_date_dateorders'])
fact_df['Order_date_dateorders'] = pd.to_datetime(fact_df['Order_date_dateorders'])
fact_df['Order_Zipcode'] = fact_df['Order_Zipcode'].map(str)
fact_df['Product_Status'] = fact_df['Product_Status'].map(str)
fact_df['Product_Card_Id'] = fact_df['Product_Card_Id'].map(str)
fact_df['Customer_Id'] = fact_df['Customer_Id'].map(str)

fact_df.to_sql('TRANSACTION', con = engine, index = False, if_exists = 'append')


