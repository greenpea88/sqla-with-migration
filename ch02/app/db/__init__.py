from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

my_dsn = "sqlite:///db.sqlite"
engine = create_engine(my_dsn)
Session = sessionmaker(engine)
