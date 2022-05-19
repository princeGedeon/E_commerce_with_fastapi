from datetime import datetime

from tortoise import Model, fields
from tortoise.contrib.pydantic import pydantic_model_creator


class User(Model):
    profile=fields.CharField(max_length=200,null=False,default="default.jpg")
    id=fields.IntField(pk=True,index=True)
    username=fields.CharField(max_length=20,null=True,unique=True)
    email=fields.CharField(max_length=200,null=False)
    password=fields.CharField(max_length=100,null=False)
    type=fields.CharField(max_length=100)
    is_verified=fields.BooleanField(default=False)
    join_data=fields.DatetimeField(default=datetime.now)

class Vendeur(Model):
    id=fields.IntField(pk=True,index=True)
    name=fields.CharField(max_length=20,null=False,unique=True)
    city=fields.CharField(max_length=100,null=False,default="Non spécifié")
    region=fields.CharField(max_length=100,null=True,default="Non spécifié")
    logo = fields.CharField(max_length=200, null=False, default="default.jpg")
    user=fields.OneToOneField("models.User",related_name="vendeur")

class Visiteur(Model):
    id=fields.IntField(pk=True,index=True)
    name=fields.CharField(max_length=20,null=False,unique=True)
    city=fields.CharField(max_length=100,null=False,default="Non spécifié")
    region=fields.CharField(max_length=100,null=True,default="Non spécifié")
    logo = fields.CharField(max_length=200, null=False, default="default.jpg")
    user=fields.OneToOneField("models.User",related_name="visiteur")

class Product(Model):
    id=fields.IntField(pk=True,index=True)
    name=fields.CharField(max_length=100)
    category=fields.CharField(max_length=100,index=True)
    price_original=fields.DecimalField(max_digits=12,decimal_places=2)
    price_new=fields.DecimalField(max_digits=12,decimal_places=2)
    offer_expiration=fields.DateField(default=datetime.utcnow)
    product_image=fields.CharField(max_length=200,null=False,default="productDefault.jpg")
    vendeur=fields.ForeignKeyField("models.Vendeur",related_name="products")



#Pydantic

user_pydantic=pydantic_model_creator(User,name="User",exclude=("is_verified"))
user_pydanticIn=pydantic_model_creator(User,name="UserIn",exclude_readonly=True)
user_pydanticOut=pydantic_model_creator(User,name="UserOut",exclude=("password"))

vendeur_pydantic=pydantic_model_creator(Vendeur,name="Vendeur")
vendeur_pydanticIn=pydantic_model_creator(Vendeur,name="VendeurIn",exclude_readonly=True)

visiteur_pydantic=pydantic_model_creator(Visiteur,name="Visiteur")
visiteur_pydanticIn=pydantic_model_creator(Visiteur,name="VisiteurIn",exclude_readonly=True)

product_pydantic=pydantic_model_creator(Product,name="Product")
product_pydanticIn=pydantic_model_creator(Product,name="ProductIn",exclude=("id"))
