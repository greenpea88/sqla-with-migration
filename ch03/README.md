# ch03
use postgreSQL >> need to change "user" and "password" in 'app > db > __ init__.py > my_dsn'

## add dependencies

```
$ poetry add alembic
$ poetry add psycopg2-binary
```

## init alembic

```
$ alembic init ./migrations
```

## edit `./migrations/env.py`

```
from app.db import my_dsn
from app.base import Base
from app.models import *

# ...
config.set_main_option('sqlalchemy.url', my_dsn)

# ...
target_metadata = Base.metadata
```

## add alembic revisions

```
$ alembic revision --autogenerate
```

## apply alembic migrations

```
$ alembic upgrade head
```