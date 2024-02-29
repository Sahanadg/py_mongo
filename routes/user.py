from fastapi import APIRouter

# from models.user import user
from confi.db  import Conn
# from index import string
from schemas.user import userEntity
from bson import ObjectId

user = APIRouter()
 
@user.get('/')
async def find_all_users():
    print(Conn.local.user.find())
    print(userEntity(Conn.local.user.find()))
    return userEntity(Conn.local.user.find())

@user.post('/')
async def create_user():
    Conn.local.user.insert_one(dict(user))
    return userEntity(Conn.local.user.find())

@user.put('/{id}')
async def update_user(id,user):
    Conn.local.user.find_one_and_update({"_id":ObjectId(id)},{
        "$set":dict(user)
    })
    return userEntity(Conn.local.user.find())
