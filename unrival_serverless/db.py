
from sqlalchemy import create_engine, text
from dotenv import dotenv_values
config = dotenv_values(".env")

engine = create_engine(config["DATABASE_URL"])
conn = engine.connect()

res = conn.execute(text("SELECT now()")).fetchall()
print(res)
