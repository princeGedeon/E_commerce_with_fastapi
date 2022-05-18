from fastapi import APIRouter

from config.db import con
from models.users import users

user=APIRouter()

@user.get('/')
async def get_users():
    return con.execute(users.select()).fetchall()