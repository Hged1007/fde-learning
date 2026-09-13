#fastapi基础框架
#ip:端口/docs  swagger ui 测试
import imp
from fastapi import FastAPI
from fastapi import Request
from tortoise.contrib.fastapi import register_tortoise  
from settings import TORTOISE_ORM

#跨域
from fastapi.middleware.cors import CORSMiddleware

#web服务器
import uvicorn  # pyright: ignore[reportMissingImports]


from api.book import api_book
from api.publish import api_publish
from api.outdoor import api_outdoor

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],#代表所有客户端
    allow_credentials=True,
    allow_meaths=["GET"],
    allow_headers=["*"]
)

register_tortoise(
    app=app,
    config=TORTOISE_ORM
)

app.include_router(api_book,prefix="/book",tags=["书籍"])
app.include_router(api_publish,prefix="/publish",tags=["出版社"])
app.include_router(api_outdoor,prefix="/outdoor",tags=["户外"])

@app.get("/")
def read_root():
    return {"message": "Hello, World!"} 

@app.put("/items/{item_id}")
def update_item(item_id: int, item: str):
    return {"message": "Item updated: " + item}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"message": "Item deleted: " + item_id}

#request 请求
@app.get("get_text")
async def get_text(request:Request):
    text=request.query_params
    print(text)
    return {"message":"get_text"}

#post 异步接收 async await
@app.post("post_text")
async def post_text(request:Request):
    text= await request.json()
    print(text)
    return {"message":"post_text"}


if __name__ == "__main__":
    uvicorn.run("fastapi1:app", host="127.0.0.1", port=8000)