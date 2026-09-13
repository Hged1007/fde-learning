from fastapi import APIRouter
from models import Publish

api_publish = APIRouter()

@api_publish.get("/")
async def getPublish():
    publish_obj=await Publish.all()
    print(publish_obj)
    #通过名字过滤获取对象
    name=await Publish.filter(name="广州出版社")
    print(name)
    #通过id过滤获取对象
    id=await Publish.filter(id=1)
    print(id)
    #限制获取几条
    limit=await Publish.all().limit(2)
    print(limit)

    return {"message": "Hello, Publsh!"}
