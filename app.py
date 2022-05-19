from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from routes.user import user

app=FastAPI()
register_tortoise(app,
                  db_url="sqlite://database.sqlite3",
                  modules={"models":["models.models"]},
                  generate_schemas=True,
                  add_exception_handlers=True
                  )

app.include_router(user)
