from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

my_dsn = "postgresql+psycopg2://user:password@localhost:5432/sample"
engine = create_engine(my_dsn)
Session = sessionmaker(engine)
