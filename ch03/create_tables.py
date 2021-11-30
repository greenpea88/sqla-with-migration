from app.db import engine
from app.db.base import Base
from app.db.models import *

if __name__ == '__main__':
    print('create tables using `Base.metadata`:')
    Base.metadata.create_all(engine)
    print('Done!')
