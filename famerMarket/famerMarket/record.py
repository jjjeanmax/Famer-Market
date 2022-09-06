import os
from pathlib import Path

import pandas as pd
import psycopg2

from secret import get_secret

HOST = get_secret(section='DATABASE', setting='HOST')
PORT = get_secret(section='DATABASE', setting='PORT')
NAME = get_secret(section='DATABASE', setting='NAME')
USER = get_secret(section='DATABASE', setting='USER')
PASSWORD = get_secret(section='DATABASE', setting='PASSWORD')


class Reports:
    def __init__(self):
        global HOST, PORT, NAME, USER, PASSWORD
        try:
            self.db_conn = psycopg2.connect(
                "host=%s port=%s dbname=%s user=%s password=%s" % (HOST, PORT, NAME, USER, PASSWORD))
        except psycopg2.OperationalError:
            print("Database Not Found Or the Credentials are wrong.")
        self.cur = self.db_conn.cursor()

    def saveUploadedInventory(self):
        file = os.path.join(Path(__file__).resolve().parent.parent, 'Export.csv')
        df = pd.read_csv(file)
        list_famers_infos = ['FMID', 'MarketName', 'Website', 'Facebook', 'Twitter', 'Youtube', 'street',
                             'city', 'County', 'State', 'zip', 'x', 'y']

        list_products = ['FMID', 'Cheese', 'Flowers', 'Eggs', 'Vegetables', 'Meat', 'Trees', 'Wine', 'Coffee', 'Fruits',
                         'Grains']

        df_famers_infos = df[list_famers_infos]
        df_products = df[list_products]
        records_famers_infos = df_famers_infos.values.tolist()
        records_products = df_products.values.tolist()

        sql_insert_famers_infos = '''INSERT INTO public."FamerApp_famersinfos"
         VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''

        sql_insert_products = '''INSERT INTO public."FamerApp_famersproducts" 
        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''

        try:
            self.cur.executemany(sql_insert_famers_infos, records_famers_infos)
            self.db_conn.commit()

            self.cur.executemany(sql_insert_products, records_products)
            self.db_conn.commit()

        except Exception as e:
            self.db_conn.rollback()
            print(e)

        finally:
            print("task is completed")
            self.cur.close()
            self.db_conn.close()


rep = Reports()
rep.saveUploadedInventory()
