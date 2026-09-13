#fastapi Request
from fastapi import FastAPI
from fastapi import Request

#web服务器
import uvicorn  # pyright: ignore[reportMissingImports]


app = FastAPI()

#request 请求
@app.get("get_text")
async def get_text(request:Request):
    get_text=request.query_params
    print(get_text)
    return {"message":"get_text"}

#post 异步接收 async await
@app.post("post_text")
async def post_text(request:Request):
    post_text= await request.json()
    print(post_text)
    return {"message":"post_text"}


if __name__ == "__main__":
    uvicorn.run("fastapi1:app", host="127.0.0.1", port=8000)