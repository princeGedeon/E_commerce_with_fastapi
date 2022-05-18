from sqlalchemy import Table, Column, Integer, String

from config.db import meta, engine

users=Table("Users",meta,
            Column("id",Integer,primary_key=True),
            Column("name",String(255)),
            Column("email",String(255)),
            Column("password",String(255)))

meta.create_all(engine)