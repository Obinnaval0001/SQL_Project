
import pandas as pd
from sqlalchemy import create_engine

conn_string = 'postgresql://postgres:admin@localhost/painting'
db = create_engine(conn_string)
conn = db.connect()

