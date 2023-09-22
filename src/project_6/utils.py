
import pandas as pd
from src.project_6.logger import logging
import pymysql
from src.project_6.exception import CustomeException
import sys

host= 'localhost'
user = 'root'
password='admin'
database='mydb'

def read_sql_data():
    logging.info("Reading SQL database started")
    try:
        mydb=pymysql.connect(
        host = host,
        user = user,
        password= password,
        database = database
        )
        logging.info("Connection OK",mydb)
        df= pd.read_sql_query("select * from data",mydb)
        # print(df.head())
        return df
    except Exception as ex:
        raise CustomeException(ex,sys)








    