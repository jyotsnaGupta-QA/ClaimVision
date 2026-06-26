import os

print(os.getcwd())

from sqlalchemy import text
from database.db import engine

try:
    with engine.connect() as conn:
        result = conn.execute(text("SELECT @@VERSION"))
        print("✅ Database Connected Successfully!\n")

        for row in result:
            print(row[0])

except Exception as ex:
    print("Connection Failed")
    print(ex)