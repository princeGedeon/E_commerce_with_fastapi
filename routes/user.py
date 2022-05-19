from typing import Type,Optional,List

from fastapi import APIRouter
from tortoise import BaseDBAsyncClient
from tortoise.signals import post_save

from models.models import user_pydanticIn, User, user_pydantic, Visiteur, visiteur_pydantic, Vendeur, vendeur_pydantic
from .authentification import (get_hashed_password)

user=APIRouter()
#Signals
@post_save(User)#User declenche
async def create_profil(
        sender:"Type[User]",
        instance:User,
        created:bool,
        using_db:"Optional[BaseDBAsyncClient]",
        update_fields:List[str]
)->None:
    if created:
        if instance.type=="Visiteur":
            visiteur_obj=await Visiteur.create(
                name=instance.username,
                user=instance
            )
            await visiteur_pydantic.from_tortoise_orm(visiteur_obj)
            #send mail
        else:
            vendeur_obj=await  Vendeur.create(
                name=instance.username,
                user=instance
            )
            await vendeur_pydantic.from_tortoise_orm(vendeur_obj)







@user.get('/')
async def index():
    return {'Message':'Heelo'}

@user.post('/registration')
async def user_registration(user:user_pydanticIn):
    user_info=user.dict(exclude_unset=True)

    user_info['password']=get_hashed_password(user_info['password'])
    user_obj=await User.create(**user_info)
    new_user=await user_pydantic.from_tortoise_orm(user_obj)
    return ({
        "status":"ok",
        "data":f"Hello {new_user.username}, Merci d'avoir choisit nos services.Vérifier votre email"
    })