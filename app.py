import sys
from src.project_6.logger import logging
from src.project_6.utils  import read_sql_data
from flask import Flask
import pandas as pd


# app = Flask(__name__)
# app.route("/")
# def home():
#     df= read_sql_data()
#     print(df.head())




# if __name__=="__main__":
#     logging.info("Exception started")

# app.run(debug=True)

df= read_sql_data()
print(df)
df.to_csv('sqlTableData')