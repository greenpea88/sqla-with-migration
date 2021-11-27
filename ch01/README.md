# ch01

## init project

```
$ poetry init
```

## create engine, SessionMaker

```
app/db/__init__.py
```

## declarative base

```
app/db/base.py
```

## create models with base

```
app/db/models.py
```

## create all tables usging base

```
from app.db import engine
from app.base import Base
from app.models import *

Base.metadata.create_all(engine)
```