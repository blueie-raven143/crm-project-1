from matplotlib.widgets import Cursor
import numpy as np
import pandas as pd
import uuid
import sqlite3

conn = sqlite3.connect('crm.db')
print("Database connected successfully......")
name = input("Enter ypur name: ")
cursor = conn.cursor()
result = cursor.execute('SELECT * FROM bda WHERE name = \'{}\''.format(name)).fetchone()
if len(result) == 0:
    print(" Wrong name")
else:
    print('welcome',name,'to THE CRM panel')




